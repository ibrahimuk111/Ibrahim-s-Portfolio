"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Audio To Text Transcription
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.core import AudioToTextTranscriptionEngine

def test_engine_execution():
    engine = AudioToTextTranscriptionEngine()
    res = engine.process("test")
    assert res["status"] == "OPERATIONAL"
    assert res["author"] == "Muhammad Ibrahim"
