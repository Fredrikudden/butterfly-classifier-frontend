import textwrap
from pathlib import Path

import streamlit as st

ASSETS = Path(__file__).resolve().parent.parent / "assets"


def md(html: str) -> None:
    st.markdown(textwrap.dedent(html).strip(), unsafe_allow_html=True)


def _section(num: str, label: str) -> None:
    md(f'<div class="section-rule"><span class="num">{num}</span><span class="label">{label}</span></div>')


def _model_block(num: str, label: str, blurb: str, matrix: str, report: str) -> None:
    _section(num, label)
    md(f'<p class="model-blurb">{blurb}</p>')
    col_matrix, col_report = st.columns([1, 1], gap="large")
    with col_matrix:
        st.image(str(ASSETS / matrix), use_container_width=True)
    with col_report:
        st.image(str(ASSETS / report), use_container_width=True)


def render() -> None:
    md("""
        <h1 class="display">Models in <em>comparison</em></h1>
        <p class="eyebrow">Three architectures · one collection</p>
        <p class="deck">A side-by-side examination of three networks trained on the same butterflies — a MLP network, a convolutional network from scratch, and a fine-tuned ConvNeXt.</p>
    """)

    # ── Section 01 — summary ─────────────────────────────────────────
    _section("01", "Summary")
    md('<p class="model-blurb">Parameter counts, best validation accuracy and best validation loss across the three architectures.</p>')
    left, mid, right = st.columns([1, 3, 1])
    with mid:
        st.image(str(ASSETS / "summary_report.png"), use_container_width=True)

    # ── Section 02 — learning curves ─────────────────────────────────
    _section("02", "Learning curves")
    md('<p class="model-blurb">Training and validation curves for all three models, plotted on a shared axis.</p>')
    st.image(str(ASSETS / "accuracy_and_loss_charts.png"), use_container_width=True)

    # ── Sections 03–05 — per-model breakdown ─────────────────────────
    _model_block(
        "03", "MLP from scratch",
        "A baseline MLP - augmentation and normalization applied, but the architecture itself ignores spatial structure once the image is flattened.",
        "mlp_confusion_matrix.png",
        "mlp_report.png",
    )

    _model_block(
        "04", "CNN from scratch",
        "Stacked Conv → BatchNorm → ReLU blocks with stride-2 downsampling. Far fewer parameters than the MLP, yet a substantial accuracy lift. Huge improvement compared to the MLP.",
        "cnn_confusion_matrix.png",
        "cnn_report.png",
    )

    _model_block(
        "05", "ConvNeXt-Tiny, fine-tuned",
        "ImageNet-pretrained backbone, two-phase fine-tune. Phase 1 trains a fresh head with the backbone frozen, phase 2 unfreezes everything and continues with a OneCycle schedule peaking at 5e-5. The deployed model.",
        "convnext_confusion_matrix.png",
        "convnext_report.png",
    )
