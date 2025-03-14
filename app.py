
import streamlit as st
from pathlib import Path

PAGES = Path(__file__).parent / "_pages"

pg = st.navigation([
    st.Page(PAGES / "000_index.py", title="Home", icon="🏠"),
    st.Page(PAGES / "100_markdown_typst.py", title="Markdown ↔ Typst", icon="♻️"),
])

pg.run()
