import json
import os
import shlex
import subprocess
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


HOST = os.getenv("OPENCLAW_ADAPTER_HOST", "172.17.0.1")
PORT = int(os.getenv("OPENCLAW_ADAPTER_PORT", "18889"))
OPENCLAW_BIN = os.getenv("OPENCLAW_BIN", "/usr/bin/openclaw")
OPENCLAW_RUN_USER = os.getenv("OPENCLAW_RUN_USER", "openclaw")
DEFAULT_AGENT_ID = os.getenv("OPENCLAW_DEFAULT_AGENT_ID", "main")
DEFAULT_THINKING = os.getenv("OPENCLAW_DEFAULT_THINKING", "minimal")
REQUEST_TIMEOUT = int(os.getenv("OPENCLAW_ADAPTER_TIMEOUT_SECONDS", "180"))


def build_command(agent_id: str, message: str) -> list[str]:
    return [
        "sudo",
        "-u",
        OPENCLAW_RUN_USER,
        "-H",
        OPENCLAW_BIN,
        "agent",
        "--agent",
        agent_id or DEFAULT_AGENT_ID,
        "--message",
        message,
        "--json",
        "--thinking",
        DEFAULT_THINKING,
    ]


def extract_text(agent_output: dict) -> str:
    payloads = (
        agent_output.get("result", {})
        .get("payloads", [])
    )
    chunks = []
    for payload in payloads:
        text = payload.get("text")
        if text:
            chunks.append(str(text).strip())
    if chunks:
        return "\n\n".join(chunk for chunk in chunks if chunk)
    return "OpenClaw adapter did not receive text payloads."


class Handler(BaseHTTPRequestHandler):
    def _write_json(self, status: int, payload: dict) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        if self.path == "/health":
            self._write_json(200, {"ok": True})
            return
        if self.path == "/v1/responses":
            self.send_response(405)
            self.send_header("Allow", "POST")
            self.end_headers()
            return
        self._write_json(404, {"error": {"type": "not_found", "message": "Not found"}})

    def do_POST(self) -> None:
        if self.path != "/v1/responses":
            self._write_json(404, {"error": {"type": "not_found", "message": "Not found"}})
            return

        try:
            length = int(self.headers.get("Content-Length", "0"))
            raw_body = self.rfile.read(length)
            payload = json.loads(raw_body.decode("utf-8") or "{}")
            message = str(payload.get("input", "")).strip()
            agent_id = str(
                self.headers.get("x-openclaw-agent-id")
                or payload.get("agent_id")
                or DEFAULT_AGENT_ID
            ).strip()
            if not message:
                self._write_json(400, {"error": {"type": "invalid_request", "message": "Missing input"}})
                return

            command = build_command(agent_id, message)
            completed = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=REQUEST_TIMEOUT,
                check=False,
            )
            if completed.returncode != 0:
                self._write_json(
                    502,
                    {
                        "error": {
                            "type": "openclaw_exec_failed",
                            "message": completed.stderr.strip() or completed.stdout.strip() or "OpenClaw agent failed",
                        }
                    },
                )
                return

            result = json.loads(completed.stdout)
            text = extract_text(result)
            self._write_json(
                200,
                {
                    "output_text": text,
                    "meta": result.get("result", {}).get("meta", {}),
                },
            )
        except subprocess.TimeoutExpired:
            self._write_json(504, {"error": {"type": "timeout", "message": "OpenClaw agent timed out"}})
        except json.JSONDecodeError:
            self._write_json(400, {"error": {"type": "invalid_json", "message": "Invalid JSON body"}})
        except Exception as exc:
            self._write_json(500, {"error": {"type": "internal_error", "message": str(exc)}})

    def log_message(self, format: str, *args) -> None:
        return


def main() -> None:
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    server.serve_forever()


if __name__ == "__main__":
    main()
