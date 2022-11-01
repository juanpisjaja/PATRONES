from __future__ import annotations
from abc import ABC, abstractmethod
class factoriaabstracta(ABC):
    @abstractmethod
    def create_product_a(self) -> prodcutoabstractoA:
        pass
    @abstractmethod
    def create_product_b(self) -> productoabstractoB:
        pass
class ConcreteFactory1(factoriaabstracta):
    def create_product_a(self) -> prodcutoabstractoA:
        return ConcreteProductA1()

    def create_product_b(self) -> productoabstractoB:
        return ConcreteProductB1()
class ConcreteFactory2(factoriaabstracta):
    def create_product_a(self) -> prodcutoabstractoA:
        return ConcreteProductA2()
    def create_product_b(self) -> productoabstractoB:
        return ConcreteProductB2()
class prodcutoabstractoA(ABC):
    @abstractmethod
    def useful_function_a(self) -> str:
        pass
class ConcreteProductA1(prodcutoabstractoA):
    def useful_function_a(self) -> str:
        return "El resultado del producto A1."
class ConcreteProductA2(prodcutoabstractoA):
    def useful_function_a(self) -> str:
        return "El resultado del producto A2."
class productoabstractoB(ABC):
    @abstractmethod
    def useful_function_b(self) -> None:
        pass
    @abstractmethod
    def another_useful_function_b(self, collaborator: prodcutoabstractoA) -> None:
        pass
class ConcreteProductB1(productoabstractoB):
    def useful_function_b(self) -> str:
        return "El resultado del producto B1."
    def another_useful_function_b(self, collaborator: prodcutoabstractoA) -> str:
        result = collaborator.useful_function_a()
        return f"El resultado de la colaboración del B1 con el ({result})"
class ConcreteProductB2(productoabstractoB):
    def useful_function_b(self) -> str:
        return "El resultado del producto B2."
    def another_useful_function_b(self, collaborator: prodcutoabstractoA):
        result = collaborator.useful_function_a()
        return f"The result of the B2 collaborating with the ({result})"
def User_code(factory: factoriaabstracta) -> None:
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()
    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function_b(product_a)}", end="")
if __name__ == "__main__":
    print("Usuario: Código de usuario de prueba con el primer tipo de fábrica:")
    User_code(ConcreteFactory1())
    print("\n")
    print("User: Probando el mismo código de usuario con el segundo tipo de fábrica:")
    User_code(ConcreteFactory2())