"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: RAG_Hallucination_Detector
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.evaluator import HallucinationDetector

def main():
    st.set_page_config(page_title="RAG Hallucination Detector", page_icon="🛡️")
    st.title("🛡️ RAG Hallucination & Faithfulness Evaluator")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    detector = HallucinationDetector()
    
    context = st.text_area("Context / Retrieved Documents", "The capital of France is Paris. It is known for the Eiffel Tower.")
    question = st.text_input("User Question", "What is the capital of France?")
    answer = st.text_area("RAG Answer", "Paris is the capital of France and has a population of 2 million people.")
    
    if st.button("Evaluate Response", type="primary"):
        f_res = detector.evaluate_faithfulness(context, answer)
        r_res = detector.evaluate_relevancy(question, answer)
        
        c1, c2 = st.columns(2)
        c1.metric("Faithfulness Score", f"{f_res['faithfulness_score']:.0%}")
        c2.metric("Relevancy Score", f"{r_res['relevancy_score']:.0%}")
        
        if f_res["hallucinated_tokens"]:
            st.warning(f"Potential Hallucinated Words: {f_res['hallucinated_tokens']}")
        else:
            st.success("No ungrounded tokens detected.")

if __name__ == "__main__":
    main()
