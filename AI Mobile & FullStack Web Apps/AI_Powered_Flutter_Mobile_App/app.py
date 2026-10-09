"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: AI_Powered_Flutter_Mobile_App
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from fastapi import FastAPI
from pydantic import BaseModel
from src.executorch_bridge import ExecuTorchBridge
import uvicorn

app = FastAPI(title="Flutter AI App Gateway", version="1.0.0")
bridge = ExecuTorchBridge()

class PromptRequest(BaseModel):
    prompt: str

@app.post("/api/v1/generate")
def generate(req: PromptRequest):
    return bridge.run_inference(req.prompt)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
