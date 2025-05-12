# src/core/app.py

from cli import CLI
from factories.task_factory import TaskFactory
from observers.observer import Observer
from models.task import Task
from models.status import Status
from models.priority import Priority

class App:
    def __init__(self):
        self.tasks = []
        self.task_factories = {
            'simple': SimpleTaskFactory(),
            'deadline': DeadlineTaskFactory(),
            'recurring': RecurringTaskFactory(),
            'subtask': SubtaskFactory()
        }
        self.cli = CLI(self)
        self.observers = []

    def add_observer(self, observer: Observer):
        self.observers.append(observer)

    def notify_observers(self, message: str):
        for observer in self.observers:
            observer.update(message)

    def create_task(self, task_type: str, title: str, description: str, assignee: str, status: str, priority: str, **kwargs):
        factory = self.task_factories.get(task_type)
        if factory:
            task = factory.create_task(task_type, title, description, assignee, status, priority, **kwargs)
            self.tasks.append(task)
            self.notify_observers(f"Nova tarefa criada: {title}")
            return task
        raise ValueError("Tipo de tarefa inválido")

    # ... restante do código ...