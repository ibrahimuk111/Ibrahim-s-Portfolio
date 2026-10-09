"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: End_To_End_CI_CD_ML_Pipeline
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from fastapi import FastAPI
from src.pipeline import MLPipelineRunner

app = FastAPI(title="CI/CD ML Pipeline API", version="1.0.0")
runner = MLPipelineRunner()

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/api/v1/trigger-pipeline")
def trigger():
    return runner.run_pipeline()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
