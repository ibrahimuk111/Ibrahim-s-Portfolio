"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: RealTime_LowLatency_YOLOv10_Tracker
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.tracker import YOLOTracker

def test_tracker():
    t = YOLOTracker()
    res = t.process_frame(1)
    assert res["fps"] > 30
