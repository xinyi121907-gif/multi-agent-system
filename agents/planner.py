from .base import BaseAgent

class PlannerAgent(BaseAgent):

    def __init__(self):
        super().__init__("planner")

    def run(self, task: str) -> str:
        return f"[Planner] 已拆解任务: {task}"