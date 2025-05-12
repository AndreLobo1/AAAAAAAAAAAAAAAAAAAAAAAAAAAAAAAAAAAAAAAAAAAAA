# src/models/priority.py

class Priority:
    HIGH = "Alta"
    MEDIUM = "Média"
    LOW = "Baixa"

    @staticmethod
    def get_all():
        return [Priority.HIGH, Priority.MEDIUM, Priority.LOW]