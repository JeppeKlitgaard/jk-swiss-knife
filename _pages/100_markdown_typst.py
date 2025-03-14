import streamlit as st
from streamlit_monaco import st_monaco
import pypandoc

st.set_page_config(
    layout="wide",
)

st.markdown("""
# ♻️ Markdown ↔ Typst

This is a little applet that converts between Markdown and Typst.
It uses `pandoc` under the hood.
""")

EDITOR_THEME = "vs-dark"
EDITOR_HEIGHT = 300


state = {
    "markdown": st.session_state.get("markdown", ""),
    "typst": st.session_state.get("typst", ""),
}

_MARKDOWN_EXTENSIONS = [
    "task_lists",
    "pipe_tables",
    "tex_math_dollars",
    "strikeout",
    "raw_html",
    "footnotes",
]

KEY_TO_FORMAT = {
    "markdown": "+".join(["commonmark"] + _MARKDOWN_EXTENSIONS),
    "typst": "typst",
}


def do_conversion(source: str, target: str):
    """
    Convert between Markdown and Typst.
    """
    print("Converting...")

    src_content = state[source]
    target_content = state[target]
    # In case of error preserve data
    st.session_state[source] = src_content
    st.session_state[target] = target_content


    if src_content == "":
        st.error(f"Please enter some {source} content.")
        return

    from_format = KEY_TO_FORMAT[source]
    to_format = KEY_TO_FORMAT[target]
    output = pypandoc.convert_text(src_content, to=to_format, format=from_format)

    st.session_state[target] = output


def md_to_typst():
    do_conversion(source="markdown", target="typst")


def typst_to_md():
    do_conversion(source="typst", target="markdown")


state["markdown"] = st_monaco(
    value=state["markdown"],
    language="markdown",
    theme=EDITOR_THEME,
    height=EDITOR_HEIGHT,
)

col1, col2, col3, col4 = st.columns([1, 2, 2, 1])
with col2:
    st.button("↓ Convert to Typst ↓", key="to_typst", on_click=md_to_typst)

with col3:
    st.button("↑ Convert to Markdown ↑", key="to_markdown", on_click=typst_to_md)

state["typst"] = st_monaco(
    value=state["typst"],
    language="typst",
    theme=EDITOR_THEME,
    height=EDITOR_HEIGHT,
)
