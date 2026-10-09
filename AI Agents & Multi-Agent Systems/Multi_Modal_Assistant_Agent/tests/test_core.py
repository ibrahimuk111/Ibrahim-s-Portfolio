"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Multi_Modal_Assistant_Agent
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import pytest
from src.agent_core import MultiModalAgent
from src.vision_processor import VisionProcessor
from src.voice_processor import VoiceProcessor


class TestMultiModalAgent:
    def test_process_text(self):
        agent = MultiModalAgent()
        response = agent.process_text("Hello")
        assert isinstance(response, str)
        assert len(agent.get_history()) == 2

    def test_process_image(self):
        agent = MultiModalAgent()
        result = agent.process_image(b"fake_image_data", "What is this?")
        assert result.confidence > 0

    def test_process_voice(self):
        agent = MultiModalAgent()
        response = agent.process_voice(b"fake_audio_data")
        assert isinstance(response, str)

    def test_clear_history(self):
        agent = MultiModalAgent()
        agent.process_text("test")
        agent.clear_history()
        assert len(agent.get_history()) == 0


class TestVisionProcessor:
    def test_encode_image(self):
        vp = VisionProcessor()
        encoded = vp.encode_image(b"test")
        assert isinstance(encoded, str)


class TestVoiceProcessor:
    def test_transcribe(self):
        vp = VoiceProcessor()
        result = vp.transcribe(b"audio_data")
        assert result.language == "en"
