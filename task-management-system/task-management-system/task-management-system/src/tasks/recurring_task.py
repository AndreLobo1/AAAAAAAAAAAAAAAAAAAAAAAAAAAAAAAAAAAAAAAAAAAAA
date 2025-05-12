# src/models/recurring_task.py

from models.task import Task

class RecurringTask(Task):
    def __init__(self, title, description, assignee, status, priority, frequency):
        super().__init__(title, description, assignee, status, priority)
        self.frequency = frequency

    def __str__(self):
        return f"[{self.status}] {self.title} (Frequência: {self.frequency}, Prioridade: {self.priority}, Responsável: {self.assignee})"