# Серверный деплой moreforms

Этот каталог хранит безопасные deploy-артефакты для серверного контура:

- `docker-compose.yml` — контейнеры `streamlit`, `oauth2-proxy`, `caddy`
- `streamlit.Dockerfile` — образ для текущего дашборда
- `Caddyfile` — reverse proxy и автоматический HTTPS
- `.env.example` — шаблон переменных окружения без секретов
- `openclaw_responses_adapter.py` — внутренний HTTP-adapter для вызова `openclaw agent`
- `scripts/server-sync.sh` — pull-and-restart сценарий для сервера

## Целевой контур

`Интернет -> Caddy -> oauth2-proxy (Google) -> Streamlit -> OpenClaw HTTP adapter -> OpenClaw agent`

## Пользовательские URL

- основной дашборд: `https://app.moreforms.ru`
- чат-дашборд: `https://app.moreforms.ru?view=chat`
- generated dashboard: `https://app.moreforms.ru?dashboard=<slug>`

Ключевые принципы:

- публично открыт только `Caddy`
- `Streamlit` живет в docker-сети, а OpenClaw вызывается через внутренний host-level adapter
- доступ в приложение идет только после Google login через `oauth2-proxy`
- реальные секреты не хранятся в git

## Что нужно заполнить на сервере

1. Скопировать шаблон:

```bash
cp deploy/.env.example /srv/moreforms/runtime/.env
```

2. Заполнить в `/srv/moreforms/runtime/.env`:

- `APP_DOMAIN`
- `MAIN_DASHBOARD_PUBLIC_URL`
- `CHAT_DASHBOARD_PUBLIC_URL`
- `OAUTH2_PROXY_CLIENT_ID`
- `OAUTH2_PROXY_CLIENT_SECRET`
- `OAUTH2_PROXY_COOKIE_SECRET`
- `OAUTH2_PROXY_ALLOWED_EMAILS_FILE`
- `OPENCLAW_RESPONSES_URL`
- `OPENCLAW_AGENT_ID`
- `OPENCLAW_CHAT_USER_PREFIX`

3. Создать файл allowlist для Google-логина, по одному email на строку:

```bash
mkdir -p /srv/moreforms/runtime/secrets
cat >/srv/moreforms/runtime/secrets/oauth2-allowed-emails.txt <<'EOF'
you@example.com
teammate@example.com
EOF
chmod 600 /srv/moreforms/runtime/secrets/oauth2-allowed-emails.txt
```

4. Запустить базовый контур:

```bash
cd /srv/moreforms/deploy/repo/deploy
docker compose --env-file /srv/moreforms/runtime/.env up -d --build
```

5. Поднять внутренний OpenClaw adapter на хосте как systemd unit и направить `Streamlit` в:

```bash
http://host.docker.internal:18889/v1/responses
```

## Google OAuth

Для `oauth2-proxy` нужен redirect URI:

```text
https://app.moreforms.ru/oauth2/callback
```

## OpenClaw

Текущий шаблон рассчитывает на host-level adapter endpoint:

```text
http://host.docker.internal:18889/v1/responses
```

Adapter вызывает `openclaw agent --json` от пользователя `openclaw` и возвращает результат в формате, который уже понимает чат в Streamlit.
На VPS это надежнее, чем напрямую интегрироваться с `OpenClaw Gateway /v1/responses`, где есть device/operator auth-слой.

## Git sync

`scripts/server-sync.sh` рассчитан на серверный clone в:

```text
/srv/moreforms/deploy/repo
```

Сценарий:

- делает `git fetch`
- fast-forward на `origin/main`
- перезапускает контейнеры через `docker compose up -d --build`

Его удобно вызывать из webhook handler или по cron.
