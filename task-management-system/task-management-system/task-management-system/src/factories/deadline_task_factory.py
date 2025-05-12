# src/factories/deadline_task_factory.py

from models.deadline_task import DeadlineTask
from factories.task_factory import TaskFactory

class DeadlineTaskFactory(TaskFactory):
    def create_task(self, task_type, *args, **kwargs):
        if task_type == 'deadline':
            return DeadlineTask(*args, **kwargs)
        raise ValueError("Tipo de tarefa desconhecido")