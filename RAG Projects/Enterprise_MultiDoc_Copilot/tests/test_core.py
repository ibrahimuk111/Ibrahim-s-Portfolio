"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Enterprise_MultiDoc_Copilot
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.copilot_engine import MultiDocCopilot

def test_copilot():
    c = MultiDocCopilot()
    res = c.process_documents(["test.pdf"], "test query")
    assert len(res["citations"]) > 0
