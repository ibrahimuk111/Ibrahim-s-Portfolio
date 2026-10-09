"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Multilingual_Translation_Summarization_Engine
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.translation_engine import MultilingualEngine

def test_nlp_engine():
    e = MultilingualEngine()
    res = e.translate_and_summarize("Long document text", "fr")
    assert "translated_summary" in res
