"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Autonomous_Code_Refactor_Agent
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

﻿"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Autonomous_Code_Refactor_Agent
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from typing import List, Dict, Any
from dataclasses import dataclass
from src.ast_analyzer import CodeSmell


@dataclass
class RefactorSuggestion:
    """A suggested code refactoring."""
    original_code: str
    refactored_code: str
    smell: CodeSmell
    confidence: float
    explanation: str


class RefactorEngine:
    """Engine that generates refactoring suggestions based on detected code smells."""

    def __init__(self):
        self.suggestions: List[RefactorSuggestion] = []

    def generate_suggestions(self, source_code: str,
                              smells: List[CodeSmell]) -> List[RefactorSuggestion]:
        """Generate refactoring suggestions for detected smells."""
        self.suggestions = []
        lines = source_code.splitlines()

        for smell in smells:
            if smell.smell_type == "missing_docstring":
                self.suggestions.append(RefactorSuggestion(
                    original_code=lines[smell.line_number - 1] if smell.line_number <= len(lines) else "",
                    refactored_code=f'    \"\"\"TODO: Add docstring for {smell.description}.\"\"\"',
                    smell=smell, confidence=0.95,
                    explanation="Adding docstring improves code documentation and maintainability."
                ))
            elif smell.smell_type == "too_many_params":
                self.suggestions.append(RefactorSuggestion(
                    original_code="", refactored_code="# Use @dataclass Config pattern",
                    smell=smell, confidence=0.80,
                    explanation="Extract parameters into a configuration dataclass."
                ))
            elif smell.smell_type == "long_function":
                self.suggestions.append(RefactorSuggestion(
                    original_code="", refactored_code="# Extract helper methods",
                    smell=smell, confidence=0.70,
                    explanation="Break long function into smaller, focused helper methods."
                ))

        return self.suggestions

    def get_report(self) -> Dict[str, Any]:
        """Generate a summary report of all suggestions."""
        return {
            "total_suggestions": len(self.suggestions),
            "high_confidence": sum(1 for s in self.suggestions if s.confidence >= 0.8),
            "by_type": self._group_by_type()
        }

    def _group_by_type(self) -> Dict[str, int]:
        groups: Dict[str, int] = {}
        for s in self.suggestions:
            t = s.smell.smell_type
            groups[t] = groups.get(t, 0) + 1
        return groups
