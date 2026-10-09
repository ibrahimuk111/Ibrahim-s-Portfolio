"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Enterprise_MultiDoc_Copilot
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.copilot_engine import MultiDocCopilot

def main():
    st.set_page_config(page_title="MultiDoc Copilot", page_icon="📄")
    st.title("📄 Enterprise MultiDoc Copilot (PDF/Excel Analyzer)")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    copilot = MultiDocCopilot()
    st.file_uploader("Upload PDF / Excel Files", accept_multiple_files=True)
    q = st.text_input("Ask Copilot", "Summarize key findings across all documents.")
    
    if st.button("Analyze & Generate Citations"):
        res = copilot.process_documents(["Q3_Report.pdf", "Financials.xlsx"], q)
        st.success(res["answer"])
        st.subheader("Document Citations")
        st.json(res["citations"])

if __name__ == "__main__":
    main()
