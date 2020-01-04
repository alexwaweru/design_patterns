from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFurnitureFactory(ABC):
    """
    This Abstract Factory interface declares a set of methods that return
    different abstract products/furniture i.e. tables and chairs. These products are
    called a family and are related by a high-level theme or concept i.e. all are furniture.
    Products of one family are usually able to collaborate among themselves.
    A family of products may have several variants, but the products of one variant are
    incompatible with products of another. For instance, you may have victorian and modern
    furniture.
    """
    @abstractmethod
    def create_table(self) -> AbstractTable:
        pass

    @abstractmethod
    def create_chair(self) -> AbstractChair:
        pass


class ConcreteModernFactory(AbstractFurnitureFactory):
    """
    Concrete Factories produce a family of products that belong to a single
    variant. This concrete factory returns only modern tables and chairs.
    The factory guarantees that resulting products are compatible. Note
    that signatures of the Concrete Factory's methods return an abstract
    product, while inside the method a concrete product is instantiated.
    """

    def create_table(self) -> ConcreteModernTable:
        return ConcreteModernTable()

    def create_chair(self) -> ConcreteModernChair:
        return ConcreteModernChair()


class ConcreteVictorianFactory(AbstractFurnitureFactory):
    """
    Each Concrete Factory has a corresponding product variant.
    """

    def create_table(self) -> ConcreteVictorianTable:
        return ConcreteVictorianTable()

    def create_chair(self) -> ConcreteVictorianChair:
        return ConcreteVictorianChair()


class AbstractTable(ABC):
    """
    Each distinct product of a product family should have a base interface. All
    variants of the product must implement this interface. This is a base
    interface for tables.
    """

    @abstractmethod
    def useful_function_a(self) -> str:
        pass


"""
Concrete Products are created by corresponding Concrete Factories.
"""


class ConcreteModernTable(AbstractTable):
    def useful_function_a(self) -> str:
        return "The result of the modern table."


class ConcreteVictorianTable(AbstractTable):
    def useful_function_a(self) -> str:
        return "The result of the victorian table."


class AbstractChair(ABC):
    """
    Here's the the base interface of another product/ chair. All products can interact
    with each other, but proper interaction is possible only between products of
    the same concrete variant.
    """
    @abstractmethod
    def useful_function_b(self) -> None:
        """
        Chair is able to do its own thing...
        """
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractTable) -> None:
        """
        ...but it also can collaborate with the table.

        The Abstract Factory makes sure that all products it creates are of the
        same variant and thus, compatible.
        """
        pass


"""
Concrete Products are created by corresponding Concrete Factories.
"""


class ConcreteModernChair(AbstractChair):
    def useful_function_b(self) -> str:
        return "The result of the chair."

    """
    The variant, modern chair, is only able to work correctly with the variant,
    victorian table. Nevertheless, it accepts any instance of table as an
    argument.
    """

    def another_useful_function_b(self, collaborator: AbstractTable) -> str:
        result = collaborator.useful_function_a()
        return f"The result of the modern chair collaborating with the ({result})"


class ConcreteVictorianChair(AbstractChair):
    def useful_function_b(self) -> str:
        return "The result of the victorian chair."

    def another_useful_function_b(self, collaborator: AbstractTable):
        """
        The variant, victorian chair, is only able to work correctly with the
        variant, Victorian table. Nevertheless, it accepts any instance of
        table as an argument.
        """
        result = collaborator.useful_function_a()
        return f"The result of the victorian chair collaborating with the ({result})"


def client_code(factory: AbstractFurnitureFactory) -> None:
    """
    The client code works with factories and products only through abstract
    types: AbstractFactory and AbstractProduct. This lets you pass any factory
    or product subclass to the client code without breaking it.
    """
    table = factory.create_table()
    chair = factory.create_chair()

    print(f"{table.useful_function_a()}")
    print(f"{chair.another_useful_function_b(table)}", end="")


if __name__ == "__main__":
    """
    The client code can work with any concrete factory class.
    """
    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteModernFactory())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code(ConcreteVictorianFactory())


# Results
'''
Client: Testing client code with the first factory type:
The result of the modern table.
The result of the modern chair collaborating with the (The result of the modern table.)

Client: Testing the same client code with the second factory type:
The result of the victorian table.
The result of the victorian chair collaborating with the (The result of the victorian table.)
'''