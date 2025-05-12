# src/models/task.py

class Task:
    def __init__(self, title, description, assignee, status, priority):
        self.title = title
        self.description = description
        self.assignee = assignee
        self.status = status
        self.priority = priority

    def edit(self, title, description, assignee, status, priority):
        self.title = title
        self.description = description
        self.assignee = assignee
        self.status = status
        self.priority = priority

    def __str__(self):
        return f"[{self.status}] {self.title} (Prioridade: {self.priority}, Responsável: {self.assignee})"