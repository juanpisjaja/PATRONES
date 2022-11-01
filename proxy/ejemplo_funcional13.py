from abc import ABC, abstractmethod  # abstractmethod() se puede utilizar para declarar métodos abstractos para propiedades y descriptores.


class Subject(ABC):

    @abstractmethod
    def request(self) -> None:
        pass


class RealSubject(Subject):
    """
    RealSubjects son capaz de hacer algún trabajo útil que también puede ser muy lento o sensible -
    p.ej. corregir los datos de entrada. Un Proxy puede resolver estos problemas sin ningún
    cambios en el código de RealSubject.
    """

    def request(self) -> None:
        print("RealSubject: Solicitud de manejo.")


class Proxy(Subject):
    """
    El Proxy tiene una interfaz idéntica a RealSubject.
    """

    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject

    def request(self) -> None:

        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self) -> bool:
        print("Proxy: Comprobación de acceso antes de disparar una solicitud real.")
        return True

    def log_access(self) -> None:
        print("Proxy: Registro de la hora de la solicitud.", end="")


def client_code(subject: Subject) -> None:

    # ...

    subject.request()

    # ...


if __name__ == "__main__":
    print("Cliente: Ejecutando el código del cliente con un sujeto real:")
    real_subject = RealSubject()
    client_code(real_subject)

    print("")

    print("Cliente: Ejecutar el mismo código de cliente con un proxy:")
    proxy = Proxy(real_subject)
    client_code(proxy)