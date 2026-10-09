"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: The YouTube Summarizer & Study Buddy
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.core import TheYouTubeSummarizer_StudyBuddEngine

def test_engine_execution():
    engine = TheYouTubeSummarizer_StudyBuddEngine()
    res = engine.process("test")
    assert res["status"] == "OPERATIONAL"
    assert res["author"] == "Muhammad Ibrahim"
