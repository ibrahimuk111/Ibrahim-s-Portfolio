"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: VLM_Video_QA_Summarizer
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.vlm_video_qa import VLMVideoQA

def test_vlm_qa():
    v = VLMVideoQA()
    res = v.answer_video_question("test.mp4", "What happened?")
    assert res["confidence"] > 0.8
