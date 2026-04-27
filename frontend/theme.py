"""Shared design tokens and global style injection.

Inter throughout for legibility, paired with editorial composition —
plate labels, hairline section rules, corner-bracket specimen frames,
parchment + ink + oxblood palette.
"""
import streamlit as st

GLOBAL_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

:root {
  --ink:           #2A1F1F;
  --ink-soft:      #5A4A4A;
  --ink-muted:     #8C7F7B;
  --parchment:     #F4ECDF;
  --parchment-2:   #EADFCB;
  --parchment-3:   #E8DDC9;
  --rose:          #A8344A;
  --rose-soft:     #C77B89;
  --brass:         #A88B5C;
  --hairline:      #C8B8A0;
  --hairline-soft: rgba(168, 52, 74, 0.12);
  --font:          'Inter', system-ui, -apple-system, 'Segoe UI', sans-serif;
}

/* ── Page canvas ─────────────────────────────────────────────────── */

html, body, [data-testid="stAppViewContainer"] {
  background:
    radial-gradient(circle at 8% 10%, rgba(168, 52, 74, 0.05), transparent 38%),
    radial-gradient(circle at 92% 88%, rgba(168, 139, 92, 0.06), transparent 42%),
    var(--parchment) !important;
  color: var(--ink);
  font-family: var(--font);
}

[data-testid="stAppViewContainer"]::before {
  content: "";
  position: fixed;
  inset: 0;
  pointer-events: none;
  z-index: 0;
  background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='240' height='240'><filter id='n'><feTurbulence baseFrequency='0.9' numOctaves='2' seed='5'/><feColorMatrix values='0 0 0 0 0.165  0 0 0 0 0.122  0 0 0 0 0.122  0 0 0 0 0.045 0'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>");
  opacity: 0.45;
  mix-blend-mode: multiply;
}

[data-testid="stHeader"] { background: transparent !important; height: 2.25rem; }
#MainMenu, footer { visibility: hidden; }
.block-container { padding-top: 1.5rem !important; padding-bottom: 4rem !important; max-width: 1180px; }

/* ── Tabs ────────────────────────────────────────────────────────── */

[data-testid="stTabs"] [role="tablist"] {
  border-bottom: 1px solid var(--hairline);
  gap: 0;
  padding: 0;
  margin-bottom: 2rem;
}
[data-testid="stTabs"] [role="tab"] {
  font-family: var(--font) !important;
  font-weight: 500;
  font-size: 0.92rem;
  letter-spacing: 0.005em;
  color: var(--ink-muted) !important;
  padding: 0 !important;
  border-bottom: 1.5px solid transparent !important;
  margin-bottom: -1px;
  transition: color .25s ease, border-color .25s ease, background-color .25s ease;
  background: transparent !important;
  cursor: pointer;
}
[data-testid="stTabs"] [role="tab"] > * {
  display: flex !important;
  align-items: center;
  justify-content: center;
  padding: 1rem 1.8rem !important;
  width: 100%;
  height: 100%;
  cursor: pointer;
}
[data-testid="stTabs"] [role="tab"]:hover {
  color: var(--ink) !important;
  background: rgba(168, 52, 74, 0.04) !important;
}
[data-testid="stTabs"] [role="tab"][aria-selected="true"] {
  color: var(--ink) !important;
  border-bottom-color: var(--rose) !important;
}
[data-testid="stTabs"] [role="tabpanel"] { padding-top: 1.25rem; }

/* ── Body type baseline ──────────────────────────────────────────── */

[data-testid="stMarkdownContainer"] p,
[data-testid="stMarkdownContainer"] li {
  font-family: var(--font);
  font-size: 0.98rem;
  line-height: 1.6;
  color: var(--ink-soft);
}
[data-testid="stMarkdownContainer"] strong { color: var(--ink); font-weight: 600; }

/* ── File uploader (custom-skinned) ──────────────────────────────── */

[data-testid="stFileUploader"] section,
[data-testid="stFileUploaderDropzone"] {
  background: rgba(255, 250, 240, 0.55) !important;
  border: 1px solid var(--hairline) !important;
  border-radius: 0 !important;
  padding: 1.5rem 1.4rem !important;
  position: relative;
}
[data-testid="stFileUploader"] section::before,
[data-testid="stFileUploader"] section::after {
  content: "";
  position: absolute;
  width: 14px; height: 14px;
  border: 1px solid var(--rose);
  pointer-events: none;
}
[data-testid="stFileUploader"] section::before { top: -1px; left: -1px; border-right: none; border-bottom: none; }
[data-testid="stFileUploader"] section::after  { bottom: -1px; right: -1px; border-left: none; border-top: none; }

[data-testid="stFileUploader"] small {
  font-family: var(--font) !important;
  color: var(--ink-muted) !important;
}
[data-testid="stFileUploader"] button {
  font-family: var(--font) !important;
  font-weight: 500 !important;
  letter-spacing: 0 !important;
  text-transform: none !important;
}

/* ── Image rendering ─────────────────────────────────────────────── */

[data-testid="stImage"] img {
  border: 1px solid var(--hairline);
  box-shadow: 0 1px 0 rgba(42, 31, 31, 0.04), 0 8px 24px -16px rgba(42, 31, 31, 0.18);
}

/* ── Alerts ──────────────────────────────────────────────────────── */

[data-testid="stAlert"] {
  border-radius: 2px !important;
  border-left: 2px solid var(--rose) !important;
  background: rgba(255, 250, 240, 0.6) !important;
  font-family: var(--font) !important;
}

/* ── Expander ────────────────────────────────────────────────────── */

[data-testid="stExpander"] details {
  border: 1px solid var(--hairline) !important;
  border-radius: 2px !important;
  background: rgba(255, 250, 240, 0.4) !important;
}
[data-testid="stExpander"] summary {
  font-family: var(--font) !important;
  color: var(--ink) !important;
  font-weight: 500;
}

/* ── Spinner caption ─────────────────────────────────────────────── */

[data-testid="stSpinner"] > div > div {
  font-family: var(--font) !important;
  color: var(--ink) !important;
}

/* ── Custom design components ────────────────────────────────────── */

.plate-label {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-family: var(--font);
  font-size: 0.7rem;
  font-weight: 500;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--ink-muted);
  padding: 0.55rem 0;
  border-top: 1px solid var(--hairline);
  border-bottom: 1px solid var(--hairline);
  margin: 0 0 2.5rem 0;
}
.plate-label .lead::before {
  content: "№ ";
  color: var(--rose);
  letter-spacing: 0;
}
.plate-label .trail { color: var(--ink); }

.eyebrow {
  font-family: var(--font);
  font-size: 0.7rem;
  font-weight: 500;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--ink-muted);
  margin: 0 0 0.7rem 0;
}

.display {
  font-family: var(--font);
  font-weight: 600;
  font-size: clamp(2.2rem, 5vw, 3.6rem);
  line-height: 1.05;
  letter-spacing: -0.022em;
  color: var(--ink);
  margin: 0;
}
.display em {
  font-style: italic;
  color: var(--rose);
  font-weight: 500;
}

.deck {
  font-family: var(--font);
  font-size: 1.02rem;
  line-height: 1.55;
  color: var(--ink-soft);
  font-weight: 400;
  max-width: 52ch;
  margin: 1.1rem 0 0 0;
}

.section-rule {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin: 2.6rem 0 1.4rem 0;
}
.section-rule .num {
  font-family: var(--font);
  font-weight: 500;
  font-size: 0.78rem;
  color: var(--rose);
  letter-spacing: 0.05em;
}
.section-rule .label {
  font-family: var(--font);
  font-size: 0.72rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--ink);
  font-weight: 600;
}
.section-rule::after {
  content: "";
  flex: 1;
  height: 1px;
  background: linear-gradient(to right, var(--hairline) 0%, transparent 100%);
}

.empty-frame {
  position: relative;
  border: 1px solid var(--hairline);
  background: rgba(255, 250, 240, 0.45);
  padding: 4.5rem 2rem;
  text-align: center;
}
.empty-frame::before, .empty-frame::after {
  content: "";
  position: absolute;
  width: 14px; height: 14px;
  border: 1px solid var(--rose);
}
.empty-frame::before { top: -1px; left: -1px; border-right: none; border-bottom: none; }
.empty-frame::after  { bottom: -1px; right: -1px; border-left: none; border-top: none; }
.empty-frame p {
  font-family: var(--font);
  font-size: 0.95rem;
  color: var(--ink-muted);
  margin: 0;
  font-style: italic;
}

/* Specimen card */

.specimen {
  position: relative;
  padding: 2rem 2.2rem 1.8rem;
  background:
    linear-gradient(180deg, rgba(255, 250, 240, 0.78) 0%, rgba(232, 221, 201, 0.42) 100%);
  border: 1px solid var(--hairline);
}
.specimen .corner {
  position: absolute;
  width: 18px; height: 18px;
  border: 1px solid var(--rose);
  pointer-events: none;
}
.specimen .corner.tl { top: -1px; left: -1px; border-right: none; border-bottom: none; }
.specimen .corner.tr { top: -1px; right: -1px; border-left: none; border-bottom: none; }
.specimen .corner.bl { bottom: -1px; left: -1px; border-right: none; border-top: none; }
.specimen .corner.br { bottom: -1px; right: -1px; border-left: none; border-top: none; }

.specimen .eyebrow { color: var(--rose); margin-bottom: 0.55rem; }
.specimen .name {
  font-family: var(--font);
  font-weight: 600;
  font-size: 2.1rem;
  line-height: 1.1;
  color: var(--ink);
  margin: 0.2rem 0 0.2rem 0;
  letter-spacing: -0.018em;
}
.specimen .latin {
  font-family: var(--font);
  font-style: italic;
  font-size: 0.98rem;
  color: var(--ink-muted);
  margin: 0;
  letter-spacing: 0.005em;
}
.specimen .conf-row {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  margin-top: 1.5rem;
  padding-top: 0.95rem;
  border-top: 1px solid var(--hairline);
}
.specimen .conf-label {
  font-family: var(--font);
  font-size: 0.7rem;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--ink-muted);
  font-weight: 500;
}
.specimen .conf-value {
  font-family: var(--font);
  font-weight: 600;
  font-size: 1.45rem;
  color: var(--ink);
  letter-spacing: -0.01em;
  font-variant-numeric: tabular-nums;
}
.specimen .conf-bar {
  height: 2px;
  background: var(--hairline-soft);
  margin-top: 0.65rem;
  overflow: hidden;
}
.specimen .conf-fill {
  height: 100%;
  background: var(--rose);
  animation: fill-in 0.8s cubic-bezier(0.2, 0.6, 0.2, 1);
}
@keyframes fill-in {
  from { transform: scaleX(0); transform-origin: left; }
  to   { transform: scaleX(1); transform-origin: left; }
}

/* Candidate species rows */

.candidates { margin-top: 0.4rem; }
.candidate {
  padding: 0.8rem 0 0.9rem;
  border-bottom: 1px solid var(--hairline);
}
.candidate:last-child { border-bottom: none; }
.candidate .meta {
  display: grid;
  grid-template-columns: 32px 1fr auto;
  align-items: baseline;
  gap: 1rem;
  margin-bottom: 0.5rem;
}
.candidate .rank {
  font-family: var(--font);
  font-size: 0.82rem;
  font-weight: 500;
  color: var(--rose);
  letter-spacing: 0.04em;
  font-variant-numeric: tabular-nums;
}
.candidate .name {
  font-family: var(--font);
  font-size: 0.98rem;
  font-weight: 500;
  color: var(--ink);
}
.candidate .latin {
  font-family: var(--font);
  font-style: italic;
  font-size: 0.85rem;
  color: var(--ink-muted);
  margin-left: 0.5rem;
  font-weight: 400;
}
.candidate .pct {
  font-family: var(--font);
  font-size: 0.86rem;
  color: var(--ink);
  letter-spacing: 0.01em;
  font-variant-numeric: tabular-nums;
}
.candidate .bar {
  height: 1px;
  background: var(--hairline-soft);
  position: relative;
}
.candidate .bar-fill {
  position: absolute;
  inset: 0 auto 0 0;
  background: var(--rose);
  animation: fill-in 0.7s cubic-bezier(0.2, 0.6, 0.2, 1);
  transform-origin: left;
}

/* Collection grid */

.collection {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  column-gap: 2.2rem;
  row-gap: 0.1rem;
  margin-top: 0.5rem;
}
.collection .item {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  padding: 0.55rem 0;
  border-bottom: 1px dotted var(--hairline);
  font-family: var(--font);
  font-size: 0.94rem;
  color: var(--ink);
  font-weight: 400;
}
.collection .item .num {
  font-family: var(--font);
  font-size: 0.74rem;
  letter-spacing: 0.06em;
  color: var(--ink-muted);
  font-variant-numeric: tabular-nums;
}

/* Links inside body content */

[data-testid="stMarkdownContainer"] a {
  color: var(--rose);
  text-decoration: none;
  border-bottom: 1px solid var(--hairline-soft);
  transition: border-color .2s ease, color .2s ease;
}
[data-testid="stMarkdownContainer"] a:hover {
  border-bottom-color: var(--rose);
}

/* Spec sheet — key/value rows with dotted leader (used on Dataset tab) */

.specsheet {
  display: grid;
  grid-template-columns: 1fr;
  margin: 1.1rem 0 1.6rem 0;
  max-width: 58ch;
}
.specsheet .row {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: 1rem;
  padding: 0.6rem 0;
  border-bottom: 1px dotted var(--hairline);
}
.specsheet .row:last-child { border-bottom: none; }
.specsheet .row > span:first-child {
  font-family: var(--font);
  color: var(--ink-muted);
  letter-spacing: 0.08em;
  font-size: 0.74rem;
  text-transform: uppercase;
  font-weight: 500;
}
.specsheet .row > span:last-child {
  font-family: var(--font);
  color: var(--ink);
  font-size: 0.96rem;
  font-weight: 500;
  text-align: right;
}

/* Model blurb (used on the Analysis tab beneath each section rule) */

.model-blurb {
  font-family: var(--font);
  font-size: 0.96rem;
  line-height: 1.55;
  color: var(--ink-soft);
  max-width: 62ch;
  margin: 0 0 1.4rem 0;
  font-style: italic;
}

/* Footnote */

.footnote {
  font-family: var(--font);
  font-size: 0.82rem;
  color: var(--ink-muted);
  text-align: center;
  margin-top: 3rem;
  padding-top: 1.2rem;
  border-top: 1px solid var(--hairline);
  letter-spacing: 0.02em;
}

@media (max-width: 720px) {
  .collection { grid-template-columns: 1fr; }
  .specimen .name { font-size: 1.7rem; }
}
</style>
"""


def inject_styles() -> None:
    """Inject the global stylesheet. Call once at the top of the entry script."""
    st.markdown(GLOBAL_CSS, unsafe_allow_html=True)
