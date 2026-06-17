from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from orchestrator import run_task

app = FastAPI()

# =========================
# CORS（允许前端访问）
# =========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# 请求模型
# =========================
class TaskRequest(BaseModel):
    prompt: str

# =========================
# 1️⃣ 根路由（解决 Not Found）
# =========================
@app.get("/")
def home():
    return {
        "message": "Multi-Agent System is running 🚀",
        "status": "ok"
    }

# =========================
# 2️⃣ 单 Agent
# =========================
@app.post("/run")
def run(req: TaskRequest):
    return {
        "result": run_task(req.prompt)
    }

# =========================
# 3️⃣ 多 Agent
# =========================
@app.post("/multi-agent")
def multi_agent(req: TaskRequest):
    result = run_task(req.prompt)

    return {
        "input": req.prompt,
        "result": result,
        "mode": "multi-agent"
    }