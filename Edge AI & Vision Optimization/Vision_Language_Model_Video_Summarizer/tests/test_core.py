"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Vision_Language_Model_Video_Summarizer
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.vlm_summarizer import VLMVideoSummarizer

def test_vlm():
    v = VLMVideoSummarizer()
    res = v.summarize_video_events("test.mp4")
    assert len(res["keyframe_summaries"]) > 0
