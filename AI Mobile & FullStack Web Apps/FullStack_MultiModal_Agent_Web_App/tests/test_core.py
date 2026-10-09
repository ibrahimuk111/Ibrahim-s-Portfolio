"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: FullStack_MultiModal_Agent_Web_App
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.agent_service import MultiModalWebService

def test_multimodal_service():
    s = MultiModalWebService()
    res = s.process_multimodal("Analyze this", True, True)
    assert len(res["processed_modalities"]) == 3
