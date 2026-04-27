# Butterfly Classifier — Frontend

A Streamlit dashboard that talks to the butterfly classifier API and presents predictions in a butterfly-themed editorial layout.

Three tabs:

- **Identifier** — upload an image, see species, confidence, and top-3 candidates
- **Analysis** — comparison of MLP, CNN, and fine-tuned ConvNeXt-Tiny (parameter counts, learning curves, confusion matrices, classification reports)
- **Dataset** — source, license, and notes on the 13-species subset used

## Running locally

Requirements: **Python 3.10+** and a running backend API (see the backend repository).

```bash
python -m venv .venv
source .venv/Scripts/activate     # Git Bash on Windows
# or: .venv\Scripts\activate      # cmd.exe
# or: source .venv/bin/activate   # macOS / Linux

pip install -r requirements.txt
streamlit run streamlit_app.py
```

The app opens at `http://localhost:8501`.

## Configuration

The dashboard reads its API URL from `.streamlit/secrets.toml`. For local development:

```toml
# .streamlit/secrets.toml
API_URL = "http://127.0.0.1:8000"
```

For deployment on Streamlit Community Cloud, set `API_URL` in the **Secrets** UI to the public URL of the deployed backend.

## Project structure

```
.
├── streamlit_app.py        # Entry — defines tabs and dispatches to views
├── theme.py                # Global CSS injection (typography, palette, components)
├── data.py                 # Latin name lookup for class labels
├── views/
│   ├── predict.py          # Identifier tab
│   ├── analysis.py         # Analysis tab
│   └── about.py            # Dataset tab
├── assets/                 # PNG plots (confusion matrices, learning curves, summary)
├── .streamlit/
│   ├── config.toml         # Theme colours
│   └── secrets.toml        # API_URL — gitignored
└── requirements.txt
```

## Design notes

- **Typography** — Inter throughout, loaded from Google Fonts via `@import` inside an injected `<style>` block.
- **Palette** — parchment cream `#F4ECDF`, ink `#2A1F1F`, oxblood rose `#A8344A` as the primary accent.
- **Composition** — section rules with italic numbering, hairline dividers, corner-bracketed specimen frames, dotted-leader spec sheets. The whole thing reads like a contemporary natural-history publication rather than a generic dashboard.

## Deployment

Deployed on [Streamlit Community Cloud](https://streamlit.io/cloud). Connect this repository, set `API_URL` in secrets, and the app rebuilds automatically on every push to `main`.

---

