from __future__ import annotations
class Facade:
    def __init__(self, subsystem1: Subsystem1, subsystem2: Subsystem2) -> None:
        self._subsystem1 = subsystem1 or Subsystem1()
        self._subsystem2 = subsystem2 or Subsystem2()
    def operation(self) -> str:
        results = []
        results.append("Facade inicializa subsistemas:")
        results.append(self._subsystem1.operation1())
        results.append(self._subsystem2.operation1())
        results.append("Facade ordena subsistemas para realizar la acción:")
        results.append(self._subsystem1.operation_n())
        results.append(self._subsystem2.operation_z())
        return "\n".join(results)
class Subsystem1:
    def operation1(self) -> str:
        return "Subsistema1: _Active_"
    def operation_n(self) -> str:
        return "Subsistema1: _Ready_"
class Subsystem2:
    def operation1(self) -> str:
        return "Subsistema2: _Ready_"
    def operation_z(self) -> str:
        return "Subsistema2: _Danger!_"
def client_code(facade: Facade) -> None:
    print(facade.operation(), end="")
if __name__ == "__main__":
    subsystem1 = Subsystem1()
    subsystem2 = Subsystem2()
    facade = Facade(subsystem1, subsystem2)
    client_code(facade)