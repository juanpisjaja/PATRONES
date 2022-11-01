import copy


class SelfReferencingEntity:
    def __init__(self):
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent


class SomeComponent:
    """
    Python proporciona su propia interfaz de Prototype a través de `copy.copy` y
    Funciones `copy.deepcopy`. Y cualquier clase que quiera implementar.
    """

    def __init__(self, some_int, some_list_of_objects, some_circular_ref):
        self.some_int = some_int
        self.some_list_of_objects = some_list_of_objects
        self.some_circular_ref = some_circular_ref

    def __copy__(self):
        """
        Crea una copia superficial. Este método será llamado cada vez que alguien llame
        `copy.copy` con este objeto y el valor devuelto se devuelve como el
        nueva copia superficial.
        """
        some_list_of_objects = copy.copy(self.some_list_of_objects)
        some_circular_ref = copy.copy(self.some_circular_ref)

        new = self.__class__(
            self.some_int, some_list_of_objects, some_circular_ref
        )
        new.__dict__.update(self.__dict__)

        return new

    def __deepcopy__(self, memo=None):
        """
        Crea una copia profunda. Este método será llamado cada vez que alguien llame
        `copy.deepcopy` con este objeto y el valor devuelto se devuelve como
        la nueva copia profunda.
        """
        if memo is None:
            memo = {}

        some_list_of_objects = copy.deepcopy(self.some_list_of_objects, memo)
        some_circular_ref = copy.deepcopy(self.some_circular_ref, memo)

        new = self.__class__(
            self.some_int, some_list_of_objects, some_circular_ref
        )
        new.__dict__ = copy.deepcopy(self.__dict__, memo)

        return new


if __name__ == "__main__":

    list_of_objects = [1, {1, 2, 3}, [1, 2, 3]]
    circular_ref = SelfReferencingEntity()
    component = SomeComponent(23, list_of_objects, circular_ref)
    circular_ref.set_parent(component)

    shallow_copied_component = copy.copy(component)


    shallow_copied_component.some_list_of_objects.append("otro objeto")
    if component.some_list_of_objects[-1] == "otro objeto":
        print(
            "Añadir elementos a `shallow_copied_component`'s"
            "alguna_lista_de_objetos lo agrega a `component`'s"
            "alguna_lista_de_objetos."
        )
    else:
        print(
            "Añadir elementos a `shallow_copied_component`'s"
            "some_list_of_objects no lo agrega a `component`'s"
            "alguna_lista_de_objetos"
        )

    # Let's change the set in the list of objects.
    component.some_list_of_objects[1].add(4)
    if 4 in shallow_copied_component.some_list_of_objects[1]:
        print(
            "Cambiar objetos en la lista_de_objetos del 'componente'"
            "cambia ese objeto en `shallow_copied_component`'s"
            "alguna_lista_de_objetos"
        )
    else:
        print(
            "Cambiar objetos en la lista_de_objetos del 'componente'"
            "no cambia ese objeto en `shallow_copied_component`'s"
            "alguna_lista_de_objetos"
        )

    deep_copied_component = copy.deepcopy(component)

    # Let's change the list in deep_copied_component and see if it changes in
    # component.
    deep_copied_component.some_list_of_objects.append("un objeto mas")
    if component.some_list_of_objects[-1] == "un objeto mas":
        print(
            "Añadir elementos a `deep_copied_component`'s"
            "alguna_lista_de_objetos lo agrega a `component`'s"
            "alguna_lista_de_objetos"
        )
    else:
        print(
            "Añadir elementos a `deep_copied_component`'s"
            "some_list_of_objects no lo agrega a `component`'s"
            "alguna_lista_de_objetos"
        )

    # Let's change the set in the list of objects.
    component.some_list_of_objects[1].add(10)
    if 10 in deep_copied_component.some_list_of_objects[1]:
        print(
            "Cambiar objetos en la lista_de_objetos del 'componente'"
            "cambia ese objeto en `deep_copied_component`'s"
            "alguna_lista_de_objetos"
        )
    else:
        print(
            "Cambiar objetos en la lista_de_objetos del 'componente'"
            "no cambia ese objeto en `deep_copied_component`'s"
            "alguna_lista_de_objetos"
        )

    print(
        f"id(deep_copied_component.some_circular_ref.parent): "
        f"{id(deep_copied_component.some_circular_ref.parent)}"
    )
    print(
        f"id(deep_copied_component.some_circular_ref.parent.some_circular_ref.parent): "
        f"{id(deep_copied_component.some_circular_ref.parent.some_circular_ref.parent)}"
    )
    print(
        "^^ Esto muestra que los objetos copiados en profundidad contienen la misma referencia, ellos "
        "no se clonan repetidamente"
    )