"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Multi_Modal_Assistant_Agent
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from typing import List, Dict, Any, Optional
from src.vision_processor import VisionProcessor, VisionResult
from src.voice_processor import VoiceProcessor, TranscriptionResult


class MultiModalAgent:
    """Core agent that orchestrates vision, voice, and text modalities."""

    def __init__(self):
        self.vision = VisionProcessor()
        self.voice = VoiceProcessor()
        self.conversation_history: List[Dict[str, str]] = []

    def process_text(self, text: str) -> str:
        self.conversation_history.append({"role": "user", "content": text})
        response = f"Processed text query: {text}"
        self.conversation_history.append({"role": "assistant", "content": response})
        return response

    def process_image(self, image_bytes: bytes, question: str = "") -> VisionResult:
        result = self.vision.analyze_image(image_bytes, question or "Describe this image")
        self.conversation_history.append({"role": "user", "content": f"[Image + {question}]"})
        self.conversation_history.append({"role": "assistant", "content": result.description})
        return result

    def process_voice(self, audio_bytes: bytes) -> str:
        transcription = self.voice.transcribe(audio_bytes)
        return self.process_text(transcription.text)

    def get_history(self) -> List[Dict[str, str]]:
        return self.conversation_history

    def clear_history(self):
        self.conversation_history.clear()
