# src/models/subtask.py

from models.task import Task

class Subtask(Task):
    def __init__(self, title, description, assignee, status, priority, parent_id):
        super().__init__(title, description, assignee, status, priority)
        self.parent_id = parent_id

    def __str__(self):
        return f"[{self.status}] {self.title} (Subtarefa de ID: {self.parent_id}, Prioridade: {self.priority}, Responsável: {self.assignee})"