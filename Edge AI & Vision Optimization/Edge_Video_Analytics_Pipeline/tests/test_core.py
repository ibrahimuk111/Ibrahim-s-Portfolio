"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Edge_Video_Analytics_Pipeline
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.analytics import VideoAnalyticsEngine

def test_analytics():
    e = VideoAnalyticsEngine()
    res = e.analyze_stream("cam_1")
    assert res["people_count"] >= 0
