# src/factories/task_factory.py

from abc import ABC, abstractmethod
from models.task import Task

class TaskFactory(ABC):
    @abstractmethod
    def create_task(self, task_type, *args, **kwargs):
        pass

class SimpleTaskFactory(TaskFactory):
    def create_task(self, task_type, *args, **kwargs):
        if task_type == 'simple':
            return Task(*args, **kwargs)
        raise ValueError("Tipo de tarefa desconhecido")