from abc import ABC, abstractmethod

class BaseAgent(ABC):

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def run(self, task: str) -> str:
        """
        所有 agent 必须实现这个方法
        """
        pass