from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List
class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass
    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass
    @abstractmethod
    def notify(self) -> None:
        pass
class ConcreteSubject(Subject):
    _state: int = None
    _observers: List[Observer] = []
    def attach(self, observer: Observer) -> None:
        print("Asunto: Adjunto un observador.")
        self._observers.append(observer)
    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)
    def notify(self) -> None:
        print("Asunto: Notificación a las observadoras ...")
        for observer in self._observers:
            observer.update(self)
    def some_business_logic(self) -> None:
        print("\nAsunto: Estoy haciendo algo importante")
        self._state = randrange(0, 10)
        print(f"Asunto: Mi estado acaba de cambiar a: {self._state}")
        self.notify()
class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass
class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state < 3:
            print("ConcreteObserverA: reaccionó al evento")
class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 0 or subject._state >= 2:
            print("ConcreteObserverA: reaccionó al evento")
if __name__ == "__main__":
    subject = ConcreteSubject()
    observer_a = ConcreteObserverA()
    subject.attach(observer_a)
    observer_b = ConcreteObserverB()
    subject.attach(observer_b)
    subject.some_business_logic()
    subject.some_business_logic()
    subject.detach(observer_a)
    subject.some_business_logic()