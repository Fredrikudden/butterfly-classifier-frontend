import textwrap

import requests
import streamlit as st
from PIL import Image

from data import latin_for

API_URL = st.secrets.get("API_URL", "http://127.0.0.1:8000")


@st.cache_data(ttl=300)
def fetch_classes() -> list[str] | None:
    try:
        r = requests.get(f"{API_URL}/health", timeout=3)
        r.raise_for_status()
        return r.json().get("classes")
    except requests.RequestException:
        return None


def call_predict(file_bytes: bytes, filename: str, content_type: str) -> dict:
    files = {"file": (filename, file_bytes, content_type or "image/jpeg")}
    r = requests.post(f"{API_URL}/predict", files=files, timeout=30)
    r.raise_for_status()
    return r.json()


def pretty(name: str) -> str:
    return name.replace("_", " ").title()


def md(html: str) -> None:
    """Render dedented HTML — strips leading indentation so Streamlit's
    Markdown parser does not interpret it as a code block."""
    st.markdown(textwrap.dedent(html).strip(), unsafe_allow_html=True)


def _section(num: str, label: str) -> str:
    return f'<div class="section-rule"><span class="num">{num}</span><span class="label">{label}</span></div>'


def _candidate(rank: int, entry: dict) -> str:
    name = pretty(entry["class_name"])
    latin = latin_for(entry["class_name"])
    latin_html = f'<span class="latin">{latin}</span>' if latin else ""
    pct = entry["confidence"]
    return (
        f'<div class="candidate">'
        f'<div class="meta">'
        f'<span class="rank">{rank:02d}</span>'
        f'<span class="name">{name}{latin_html}</span>'
        f'<span class="pct">{pct:.1%}</span>'
        f"</div>"
        f'<div class="bar"><div class="bar-fill" style="width:{pct * 100:.2f}%"></div></div>'
        f"</div>"
    )


def render() -> None:
    classes = fetch_classes()

    md("""
        <h1 class="display">The Butterfly <em>Identifier</em></h1>
        <p class="eyebrow">13 classes</p>
        <p class="deck">A fine-tuned convolutional network model that identifies butterfly species. Drop an image of a butterfly from a species listed in the collection below to get a  
  verdict.</p>
    """)

    md(_section("01", "Submit your butterfly image"))

    col_upload, col_result = st.columns([1, 1], gap="large")

    with col_upload:
        uploaded = st.file_uploader(
            "Upload an image",
            type=["jpg", "jpeg", "png", "webp"],
            label_visibility="collapsed",
        )
        if uploaded is not None:
            st.image(Image.open(uploaded), use_container_width=True)

    result = None
    with col_result:
        if uploaded is None:
            md("""
                <div class="empty-frame">
                <p>Awaiting prediction.</p>
                </div>
            """)
        else:
            try:
                with st.spinner("Identifying…"):
                    result = call_predict(
                        uploaded.getvalue(), uploaded.name, uploaded.type
                    )
            except requests.RequestException as exc:
                st.error(
                    f"Could not reach the API at `{API_URL}`. Is the backend running?"
                )
                st.exception(exc)
                st.stop()

            label = pretty(result["prediction"])
            latin = latin_for(result["prediction"])
            latin_html = f'<p class="latin">{latin}</p>' if latin else ""
            conf = result["confidence"]

            specimen = (
                f'<div class="specimen">'
                f'<span class="corner tl"></span>'
                f'<span class="corner tr"></span>'
                f'<span class="corner bl"></span>'
                f'<span class="corner br"></span>'
                f'<p class="eyebrow">Specimen identified</p>'
                f'<h2 class="name">{label}</h2>'
                f"{latin_html}"
                f'<div class="conf-row">'
                f'<span class="conf-label">Confidence</span>'
                f'<span class="conf-value">{conf:.1%}</span>'
                f"</div>"
                f'<div class="conf-bar"><div class="conf-fill" style="width:{conf * 100:.2f}%"></div></div>'
                f"</div>"
            )
            md(specimen)

    if result is not None:
        md(_section("02", "Candidate species"))
        rows = "".join(_candidate(i, e) for i, e in enumerate(result["top_k"], start=1))
        md(f'<div class="candidates">{rows}</div>')

    md(_section("03", "The species collection"))
    if classes:
        items = "".join(
            f'<div class="item"><span>{pretty(cls)}</span><span class="num">{i:02d}</span></div>'
            for i, cls in enumerate(sorted(classes), start=1)
        )
        md(f'<div class="collection">{items}</div>')
    else:
        md(
            f'<p class="footnote">Collection unavailable — backend at <code>{API_URL}</code> did not respond.</p>'
        )

    md(
        '<p class="footnote">Trained on a curated butterfly collection · ConvNeXt-Tiny, fine-tuned</p>'
    )
