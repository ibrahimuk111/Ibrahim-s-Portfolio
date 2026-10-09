"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Local_vLLM_Inference_Server
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from fastapi import FastAPI
from pydantic import BaseModel
from src.vllm_engine import vLLMEngineServer
import uvicorn

app = FastAPI(title="vLLM Inference Server API", version="1.0.0")
engine = vLLMEngineServer()

class GenRequest(BaseModel):
    prompt: str

@app.post("/v1/completions")
def completions(req: GenRequest):
    return engine.generate_stream(req.prompt)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
