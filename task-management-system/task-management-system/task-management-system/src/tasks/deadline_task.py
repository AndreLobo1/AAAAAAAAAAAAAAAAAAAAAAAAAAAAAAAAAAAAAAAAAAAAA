# src/models/deadline_task.py

from models.task import Task

class DeadlineTask(Task):
    def __init__(self, title, description, assignee, status, priority, deadline):
        super().__init__(title, description, assignee, status, priority)
        self.deadline = deadline

    def __str__(self):
        return f"[{self.status}] {self.title} (Deadline: {self.deadline}, Prioridade: {self.priority}, Responsável: {self.assignee})"