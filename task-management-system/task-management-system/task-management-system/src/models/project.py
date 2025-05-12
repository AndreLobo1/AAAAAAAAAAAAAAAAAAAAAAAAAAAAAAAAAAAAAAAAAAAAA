# src/models/project.py

class Project:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"Projeto: {self.name}"