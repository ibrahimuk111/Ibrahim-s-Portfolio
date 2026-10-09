"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Enterprise_LLM_Guardrails_API
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.guardrails import SafetyGuardrails
import uvicorn

app = FastAPI(title="Enterprise LLM Guardrails API", version="1.0.0")
guard = SafetyGuardrails()

class RequestModel(BaseModel):
    prompt: str

@app.post("/api/v1/guard")
def guard_prompt(req: RequestModel):
    result = guard.sanitize(req.prompt)
    if not result["is_safe"]:
        raise HTTPException(status_code=400, detail=f"Prompt flagged for toxic content: {result['flagged_keywords']}")
    return result

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
