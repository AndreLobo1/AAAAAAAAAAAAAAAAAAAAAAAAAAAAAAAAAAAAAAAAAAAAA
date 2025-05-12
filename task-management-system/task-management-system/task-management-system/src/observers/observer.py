# src/observers/observer.py

class Observer:
    def update(self, message):
        raise NotImplementedError("O método 'update' deve ser implementado pela classe filha.")