"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Autonomous_Code_Refactor_Agent
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import pytest
from src.ast_analyzer import ASTAnalyzer, CodeSmell
from src.refactor_engine import RefactorEngine


class TestASTAnalyzer:
    def test_detect_missing_docstring(self):
        code = "def foo():\n    pass"
        analyzer = ASTAnalyzer()
        smells = analyzer.analyze(code)
        types = [s.smell_type for s in smells]
        assert "missing_docstring" in types

    def test_detect_too_many_params(self):
        code = "def foo(a, b, c, d, e, f, g):\n    pass"
        analyzer = ASTAnalyzer()
        smells = analyzer.analyze(code)
        types = [s.smell_type for s in smells]
        assert "too_many_params" in types

    def test_syntax_error_handling(self):
        analyzer = ASTAnalyzer()
        smells = analyzer.analyze("def broken(")
        assert any(s.smell_type == "syntax_error" for s in smells)

    def test_clean_code(self):
        code = '\"\"\"Module.\"\"\"\n\ndef foo(a):\n    \"\"\"Doc.\"\"\"\n    return a'
        analyzer = ASTAnalyzer()
        smells = analyzer.analyze(code)
        critical = [s for s in smells if s.severity == "critical"]
        assert len(critical) == 0


class TestRefactorEngine:
    def test_generates_suggestions(self):
        smells = [CodeSmell("f.py", 1, "missing_docstring", "test", "low")]
        engine = RefactorEngine()
        suggestions = engine.generate_suggestions("def foo():\n    pass", smells)
        assert len(suggestions) > 0

    def test_report_structure(self):
        engine = RefactorEngine()
        report = engine.get_report()
        assert "total_suggestions" in report
