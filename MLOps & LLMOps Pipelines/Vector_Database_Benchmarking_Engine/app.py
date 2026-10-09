"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Vector_Database_Benchmarking_Engine
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.benchmark import VectorDBBenchmarker

def main():
    st.set_page_config(page_title="Vector DB Benchmark", page_icon="⚡")
    st.title("⚡ Vector Database Benchmarking Engine")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    bench = VectorDBBenchmarker()
    count = st.select_slider("Vector Count", options=[1000, 10000, 50000, 100000], value=10000)
    
    if st.button("Run Comparison Benchmark"):
        results = [
            bench.benchmark_db("FAISS", count),
            bench.benchmark_db("ChromaDB", count),
            bench.benchmark_db("Pinecone", count)
        ]
        st.table(results)

if __name__ == "__main__":
    main()
