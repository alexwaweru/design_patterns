from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractPizzaStore(ABC):

    @abstractmethod
    def create_pizza(self) -> AbstractPizza:
        """ 
        This is factory method
        """
        pass

    def order_pizza(self) -> AbstractPizza:

        # Call the factory method to create a pizza object.
        pizza = self.create_pizza()

        return pizza


class ChicagoPizzaStore(AbstractPizzaStore):

    def create_pizza(self) -> ChicagoStylePizza:
        return ChicagoStylePizza()


class SeattlePizzaStore(AbstractPizzaStore):

    def create_pizza(self) -> SeattleStylePizza:
        return SeattleStylePizza()


class AbstractPizza(ABC):

    @abstractmethod
    def style(self) -> str:
        pass

    def size(self) -> str:
        return "pizza size is jumbo"


class ChicagoStylePizza(AbstractPizza):
    def style(self) -> str:
        return "pizza style is chicago"


class SeattleStylePizza(AbstractPizza):
    def style(self) -> str:
        return "pizza style is seattle"


def client_code(pizza_store: AbstractPizzaStore) -> None:

    print(f"Client: I'm not aware of the pizza store, but it still works.\n"
          f"{pizza_store.create_pizza().style()}.\n"
          f"{pizza_store.create_pizza().size()}.", end="")


if __name__ == "__main__":
    print("Pizza Delivery App: Launched in Seattle.")
    client_code(SeattlePizzaStore())
    print("\n")

    print("Pizza Delivery App: Launched in Chicago.")
    client_code(ChicagoPizzaStore())


# output
"""
Pizza Delivery App: Launched in Seattle.
Client: I'm not aware of the pizza store, but it still works.
pizza style is seattle.
pizza size is jumbo.

Pizza Delivery App: Launched in Chicago.
Client: I'm not aware of the pizza store, but it still works.
pizza style is chicago.
pizza size is jumbo.
"""
