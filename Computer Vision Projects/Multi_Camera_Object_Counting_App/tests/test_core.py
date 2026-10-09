"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Multi_Camera_Object_Counting_App
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.multi_camera_counter import MultiCameraCounter

def test_counter():
    c = MultiCameraCounter()
    res = c.process_camera_stream("cam1")
    assert res["current_occupancy"] >= 0
