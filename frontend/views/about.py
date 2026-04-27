import textwrap

import streamlit as st

# Replace with the actual Kaggle URL of the dataset you used.
DATASET_URL = "https://www.kaggle.com/datasets/gpiosenka/butterfly-images40-species"


def md(html: str) -> None:
    st.markdown(textwrap.dedent(html).strip(), unsafe_allow_html=True)


def _section(num: str, label: str) -> None:
    md(f'<div class="section-rule"><span class="num">{num}</span><span class="label">{label}</span></div>')


def render() -> None:
    md("""
        <h1 class="display">The <em>dataset</em></h1>
        <p class="eyebrow">A subset of 13 classes</p>
        <p class="deck">Where the images come from, what they look like, and how 13 species were chosen from one hundred.</p>
    """)

    # ── Section 01 — Source ──────────────────────────────────────────
    _section("01", "Source")
    md(f"""
        <p>The images come from <a href="{DATASET_URL}" target="_blank" rel="noopener">Butterfly &amp; Moths Image Classification</a> on Kaggle, compiled by gpiosenka. The collection covers a hundred species across 13,594 pre-cropped images and is released into the public domain under CC0.</p>
    """)
    md("""
        <div class="specsheet">
          <div class="row"><span>Author</span><span>gpiosenka · Kaggle</span></div>
          <div class="row"><span>License</span><span>CC0 · Public domain</span></div>
          <div class="row"><span>Coverage</span><span>100 species · butterflies and moths</span></div>
          <div class="row"><span>Format</span><span>224 × 224 · RGB · JPG</span></div>
          <div class="row"><span>Total images</span><span>13,594</span></div>
          <div class="row"><span>Train / Valid / Test</span><span>12,594 / 500 / 500</span></div>
        </div>
    """)

    # ── Section 02 — The subset ──────────────────────────────────────
    _section("02", "The subset")
    md("""
        <p>For this project I used a subset of 13 species carved out of the original hundred. The smaller cut keeps training tractable on a single GPU and concentrates the comparison on a manageable slice — I carefully picked some butterflies that were easily distinguishable, and some that even I could barely tell apart, such as the Monarch and Viceroy butterflies.</p>
    """)
    md("""
        <div class="specsheet">
          <div class="row"><span>Species used</span><span>13</span></div>
          <div class="row"><span>Training images</span><span>1,336</span></div>
          <div class="row"><span>Validation images</span><span>334</span></div>
        </div>
    """)
    md('<p>The full list of species is on the Identifier tab, beneath the prediction.</p>')

    # ── Section 03 — Note on the bundled model ───────────────────────
    _section("03", "On the bundled model")
    md("""
        <p>The Kaggle dataset ships with a pretrained EfficientNetB0. It was not used here. The MLP and CNN in this project were trained from random initialisation on butterflies only; the deployed ConvNeXt-Tiny was fine-tuned from ImageNet weights — never from the bundled checkpoint.</p>
    """)
