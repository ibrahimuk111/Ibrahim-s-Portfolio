"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Autonomous_Code_Refactor_Agent
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import ast
import textwrap
from typing import List, Dict, Any
from dataclasses import dataclass, field


@dataclass
class CodeSmell:
    """Represents a detected code quality issue."""
    file_path: str
    line_number: int
    smell_type: str
    description: str
    severity: str = "medium"
    suggestion: str = ""


class ASTAnalyzer:
    """Analyzes Python source code AST for code smells and improvement opportunities."""

    COMPLEXITY_THRESHOLD = 10
    LONG_FUNCTION_LINES = 50
    MAX_PARAMS = 5

    def __init__(self):
        self.smells: List[CodeSmell] = []

    def analyze(self, source_code: str, file_path: str = "<input>") -> List[CodeSmell]:
        """Parse and analyze source code for code smells."""
        self.smells = []
        try:
            tree = ast.parse(source_code)
        except SyntaxError as e:
            self.smells.append(CodeSmell(file_path, e.lineno or 0, "syntax_error",
                                         str(e), "critical"))
            return self.smells

        self._check_function_length(tree, source_code, file_path)
        self._check_parameter_count(tree, file_path)
        self._check_nested_depth(tree, file_path)
        self._check_missing_docstrings(tree, file_path)
        return self.smells

    def _check_function_length(self, tree: ast.AST, source: str, path: str):
        lines = source.splitlines()
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                end = getattr(node, 'end_lineno', node.lineno + self.LONG_FUNCTION_LINES)
                length = end - node.lineno
                if length > self.LONG_FUNCTION_LINES:
                    self.smells.append(CodeSmell(
                        path, node.lineno, "long_function",
                        f"Function '{node.name}' is {length} lines long",
                        "medium", "Consider breaking into smaller functions."))

    def _check_parameter_count(self, tree: ast.AST, path: str):
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                params = len(node.args.args)
                if params > self.MAX_PARAMS:
                    self.smells.append(CodeSmell(
                        path, node.lineno, "too_many_params",
                        f"Function '{node.name}' has {params} parameters",
                        "low", "Consider using a config object or dataclass."))

    def _check_nested_depth(self, tree: ast.AST, path: str, max_depth: int = 4):
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                depth = self._max_nesting(node)
                if depth > max_depth:
                    self.smells.append(CodeSmell(
                        path, node.lineno, "deep_nesting",
                        f"Function '{node.name}' has nesting depth {depth}",
                        "high", "Refactor using early returns or extract methods."))

    def _check_missing_docstrings(self, tree: ast.AST, path: str):
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                if not (node.body and isinstance(node.body[0], ast.Expr)
                        and isinstance(node.body[0].value, (ast.Str, ast.Constant))):
                    self.smells.append(CodeSmell(
                        path, node.lineno, "missing_docstring",
                        f"'{node.name}' is missing a docstring", "low",
                        "Add a descriptive docstring."))

    @staticmethod
    def _max_nesting(node: ast.AST, current: int = 0) -> int:
        max_d = current
        for child in ast.iter_child_nodes(node):
            if isinstance(child, (ast.If, ast.For, ast.While, ast.With, ast.Try)):
                max_d = max(max_d, ASTAnalyzer._max_nesting(child, current + 1))
            else:
                max_d = max(max_d, ASTAnalyzer._max_nesting(child, current))
        return max_d
