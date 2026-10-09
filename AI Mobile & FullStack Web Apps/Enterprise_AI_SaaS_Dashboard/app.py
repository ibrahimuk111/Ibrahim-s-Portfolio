"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Enterprise_AI_SaaS_Dashboard
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.saas_engine import EnterpriseSaaSEngine
import uvicorn

app = FastAPI(title="Enterprise AI SaaS Gateway", version="1.0.0")
saas = EnterpriseSaaSEngine()

class UsageRequest(BaseModel):
    user_id: str
    tier: str
    tokens: int

@app.post("/api/v1/saas/consume")
def consume(req: UsageRequest):
    res = saas.verify_and_consume(req.user_id, req.tier, req.tokens)
    if not res["authorized"]:
        raise HTTPException(status_code=429, detail="Quota exceeded for current plan.")
    return res

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
