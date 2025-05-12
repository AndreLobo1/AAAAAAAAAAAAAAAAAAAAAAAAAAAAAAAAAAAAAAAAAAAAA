# src/models/status.py

class Status:
    PENDING = "Pendente"
    IN_PROGRESS = "Em Andamento"
    COMPLETED = "Concluída"

    @staticmethod
    def get_all():
        return [Status.PENDING, Status.IN_PROGRESS, Status.COMPLETED]