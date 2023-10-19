from abc import ABC, abstractmethod


class Observable(ABC):

    def __init__(self):
        self.observers = []
    def register_observer(self, observer: "Observer"):
        self.observers.append(observer)
    def notify_observers(self):
        for observer in self.observers:
            observer.update()

class Observer(ABC):

    @abstractmethod
    def update(self):
        pass