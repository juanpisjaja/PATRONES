class estructura():
    def operation(self) -> str:
        pass
class Concreteestructura(estructura):
    def operation(self) -> str:
        return "Concreteestructura"
class Decorator(estructura):
    _estructura: estructura = None
    def __init__(self, estructura: estructura) -> None:
        self._estructura = estructura
    @property
    def estructura(self) -> estructura:
        return self._estructura
    def operation(self) -> str:
        return self._estructura.operation()
class ConcreteDecoratorA(Decorator):
    def operation(self) -> str:
        return f"ConcreteDecoratorA({self.estructura.operation()})"
class ConcreteDecoratorB(Decorator):
    def operation(self) -> str:
        return f"ConcreteDecoratorB({self.estructura.operation()})"
def client_code(estructura: estructura) -> None:
    print(f"RESULT: {estructura.operation()}", end="")
if __name__ == "__main__":
    simple = Concreteestructura()
    print("User: Si tienes una estructura simple es:")
    client_code(simple)
    print("\n")
    decorator1 = ConcreteDecoratorA(simple)
    decorator2 = ConcreteDecoratorB(decorator1)
    print("User: Si tienes una estructura decorada es:")
    client_code(decorator2)