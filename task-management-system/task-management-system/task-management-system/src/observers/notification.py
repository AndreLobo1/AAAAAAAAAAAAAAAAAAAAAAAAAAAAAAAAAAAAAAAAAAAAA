# src/observers/notification.py

class Notification:
    def notify_observers(self, observers, message):
        for observer in observers:
            observer.update(message)