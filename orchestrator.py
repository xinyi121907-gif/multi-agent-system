from typing import Dict, List


# =========================
# Planner Agent
# =========================
def planner_agent(prompt: str) -> Dict:
    return {
        "tasks": [
            f"分析需求：{prompt}",
            "设计系统架构",
            "生成核心代码",
            "优化与检查"
        ]
    }


# =========================
# Worker Agents（模拟不同智能体）
# =========================
def coder_agent(task: str) -> str:
    return f"[Coder] {task} → 已实现代码"


def designer_agent(task: str) -> str:
    return f"[Designer] {task} → 已完成设计"


def optimizer_agent(task: str) -> str:
    return f"[Optimizer] {task} → 已优化结构"


# =========================
# Agent Router（模拟分工）
# =========================
def dispatch_agent(task: str, idx: int) -> str:

    agents = [
        coder_agent,
        designer_agent,
        coder_agent,
        optimizer_agent
    ]

    agent = agents[idx % len(agents)]
    return agent(task)


# =========================
# Critic Agent
# =========================
def critic_agent(results: List[str]) -> str:
    return " | ".join(results) + " → [系统已完成评审优化]"


# =========================
# Orchestrator（核心）
# =========================
def run_task(prompt: str) -> Dict:

    # 1. 规划
    plan = planner_agent(prompt)

    # 2. 分发执行（模拟多智能体）
    results = []
    for i, task in enumerate(plan["tasks"]):
        results.append(dispatch_agent(task, i))

    # 3. 评审
    final = critic_agent(results)

    # 4. 输出
    return {
        "input": prompt,
        "plan": plan,
        "raw_results": results,
        "final": final,
        "mode": "multi-agent-v2"
    }