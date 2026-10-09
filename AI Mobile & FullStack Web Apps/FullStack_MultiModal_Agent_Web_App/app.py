"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: FullStack_MultiModal_Agent_Web_App
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from fastapi import FastAPI, UploadFile, File, Form
from src.agent_service import MultiModalWebService
import uvicorn

app = FastAPI(title="FullStack MultiModal Agent API", version="1.0.0")
service = MultiModalWebService()

@app.post("/api/v1/agent/chat")
async def chat(prompt: str = Form(...)):
    return service.process_multimodal(prompt)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
