"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: End_To_End_CI_CD_ML_Pipeline
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.pipeline import MLPipelineRunner

def test_pipeline():
    p = MLPipelineRunner()
    res = p.run_pipeline()
    assert res["status"] == "SUCCESS"
