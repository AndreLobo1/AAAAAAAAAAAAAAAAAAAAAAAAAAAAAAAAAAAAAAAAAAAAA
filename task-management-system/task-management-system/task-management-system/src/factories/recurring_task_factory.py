# src/factories/recurring_task_factory.py

from models.recurring_task import RecurringTask
from factories.task_factory import TaskFactory

class RecurringTaskFactory(TaskFactory):
    def create_task(self, task_type, *args, **kwargs):
        if task_type == 'recurring':
            return RecurringTask(*args, **kwargs)
        raise ValueError("Tipo de tarefa desconhecido")