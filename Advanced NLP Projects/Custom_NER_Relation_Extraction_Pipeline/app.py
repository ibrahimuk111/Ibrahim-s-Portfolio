"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Custom_NER_Relation_Extraction_Pipeline
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.ner_extractor import CustomNERPipeline

def main():
    st.set_page_config(page_title="Custom NER & Relation Extractor", page_icon="🏷️")
    st.title("🏷️ Custom NER & Relation Extraction Pipeline (spaCy/PyTorch)")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    ner = CustomNERPipeline()
    txt = st.text_area("Input Text", "Muhammad Ibrahim maintains open source repositories on GitHub.")
    
    if st.button("Extract Entities & Relations"):
        res = ner.extract_entities_and_relations(txt)
        st.subheader("Named Entities")
        st.json(res["entities"])
        st.subheader("Extracted Relations")
        st.json(res["relations"])

if __name__ == "__main__":
    main()
