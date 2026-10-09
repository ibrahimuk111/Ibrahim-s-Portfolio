"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: LLM_FineTuning_Quantization_Pipeline
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.quantization import ModelQuantizer

def main():
    st.set_page_config(page_title="LLM Fine-Tuning & Quantization", page_icon="⚡")
    st.title("⚡ LLM Fine-Tuning & Quantization Pipeline (QLoRA / GGUF)")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    q = ModelQuantizer()
    model = st.selectbox("Base Model", ["Llama-3-8B", "Mistral-7B", "Qwen2.5-7B"])
    quant = st.selectbox("Quantization Target", ["4bit", "8bit", "GGUF_Q4"])
    
    if st.button("Simulate Quantization & Benchmark VRAM"):
        res = q.simulate_quantization(model, quant)
        c1, c2, c3 = st.columns(3)
        c1.metric("Quantized Size", f"{res['quantized_size_gb']} GB")
        c2.metric("Compression Ratio", f"{res['compression_ratio']}x")
        c3.metric("Required VRAM", f"{res['vram_required_gb']} GB")

if __name__ == "__main__":
    main()
