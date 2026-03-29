# moreforms

Competitor tracker and Streamlit dashboard for the `moreforms` project.

## Files

- `Agents.md` — operating instructions for the assistant
- `artifacts.md` — overview of product artifacts
- `artifacts/` — dedicated product artifact documents
- `data/competitors.csv` — competitor database
- `data/artifacts.csv` — product artifacts registry
- `app.py` — Streamlit dashboard
- `workspace_template_guide.md` — how to use the AI-first workspace template in `moreforms`
- `references/ai-first-workspace-template` — external reference workspace template as git submodule

## Local run

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/streamlit run app.py
```

## Streamlit Community Cloud

If Community Cloud fails during dependency install, use the repository root `requirements.txt` from this repo and reboot the app after pushing dependency changes.

If you need to choose a Python version in Streamlit Community Cloud, prefer `Python 3.12` or a currently supported version from the deployment UI.

## AI-first Workspace Reference

This project includes the repository `VsevolodUstinov/ai-first-workspace-template` as a git submodule under:

`references/ai-first-workspace-template`

Use it as a reference for AI-first project operations, repository structure, and context management.
The local adaptation guide is in:

`workspace_template_guide.md`
