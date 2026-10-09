"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Multi_Agent_Research_Engine
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import os
import streamlit as st
from src.orchestrator import MultiAgentOrchestrator


def main():
    st.set_page_config(page_title="Multi-Agent Research Engine", page_icon="ðŸ”¬", layout="wide")
    st.title("ðŸ”¬ Multi-Agent Research Engine")
    st.caption("Powered by LangGraph + Tavily | Author: Muhammad Ibrahim")

    with st.sidebar:
        st.header("Configuration")
        api_key = st.text_input("Tavily API Key", type="password",
                                value=os.getenv("TAVILY_API_KEY", ""))
        max_results = st.slider("Max Search Results", 1, 10, 5)
        max_iterations = st.slider("Max Review Iterations", 1, 5, 3)

    topic = st.text_input("Enter Research Topic", placeholder="e.g., Recent advances in quantum computing")

    if st.button("ðŸš€ Start Research", type="primary"):
        if not topic:
            st.warning("Please enter a research topic.")
            return
        orchestrator = MultiAgentOrchestrator(tavily_key=api_key)
        with st.spinner("Agents working..."):
            result = orchestrator.run_pipeline(topic, max_results, max_iterations)

        col1, col2, col3 = st.columns(3)
        col1.metric("Findings", result["findings_count"])
        col2.metric("Iterations", result["iterations"])
        col3.metric("Quality Score", result["review"]["quality_score"])

        st.markdown(result["report"])
        with st.expander("Review Details"):
            st.json(result["review"])


if __name__ == "__main__":
    main()
