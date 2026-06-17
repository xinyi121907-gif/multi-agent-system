from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from orchestrator import run_task

app = FastAPI()

# CORS（必须）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 请求模型
class TaskRequest(BaseModel):
    prompt: str

# 首页
@app.get("/")
def home():
    return {"message": "Multi-Agent System is running 🚀"}

# 单Agent
@app.post("/run")
def run(req: TaskRequest):
    return {"result": run_task(req.prompt)}

# 多Agent
@app.post("/multi-agent")
def multi_agent(req: TaskRequest):
    result = run_task(req.prompt)

    return {
        "input": req.prompt,
        "result": result,
        "mode": "multi-agent"
    }