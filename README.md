# moreforms

Competitor tracker and Streamlit dashboard for the `moreforms` project.

## Files

- `Agents.md` — operating instructions for the assistant
- `data/competitors.csv` — competitor database
- `app.py` — Streamlit dashboard

## Local run

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/streamlit run app.py
```

## Streamlit Community Cloud

If Community Cloud fails during dependency install, use the repository root `requirements.txt` from this repo and reboot the app after pushing dependency changes.

If you need to choose a Python version in Streamlit Community Cloud, prefer `Python 3.12` or a currently supported version from the deployment UI.
