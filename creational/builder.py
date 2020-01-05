''from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty
from typing import Any


class AbstractHouseBuilder(ABC):
    """
    This Builder interface specifies methods for creating the different parts of
    the house.
    """

    @abstractmethod
    def add_wall(self) -> None:
        pass

    @abstractmethod
    def add_floor(self) -> None:
        pass

    @abstractmethod
    def add_swimming_pool(self) -> None:
        pass

    @abstractmethod
    def add_balcony(self) -> None:
        pass

    @abstractproperty
    def house(self) -> AbstractHouse:
        pass


class HouseBuilder(AbstractHouseBuilder):

    def __init__(self) -> None:
        self._house = House()

    def add_wall(self, wall=None, component_name="wall") -> None:
        if not wall:
            wall = Wall()
        self._house.add(wall, component_name)

    def add_floor(self, floor=None, component_name="floor") -> None:
        if not floor:
            floor = Floor()
        self._house.add(floor, component_name)

    def add_swimming_pool(self, swimming_pool=None, component_name="swimming_pool") -> None:
        if not swimming_pool:
            swimming_pool = SwimmingPool()
        self._house.add(swimming_pool, component_name)

    def add_balcony(self, balcony=None, component_name="balcony") -> None:
        if not balcony:
            balcony = Balcony()
        self._house.add(balcony, component_name)

    def house(self) -> House:
        return self._house


class AbstractHouse(ABC):

    @abstractmethod
    def add(self, component: Any, component_name: str) -> None:
        pass

    @abstractmethod
    def list_components(self) -> None:
        pass


class House:

    def __init__(self) -> None:
        self._components = {}

    def add(self, component: Any, component_name: str) -> None:
        setattr(component, "identifier", component_name)
        self._components[component_name] = component

    def __getattr__(self, attribute):
        if attribute in self._components.keys():
            return self._components[attribute]

    def list_components(self) -> None:
        return f"House components: {', '.join(self._components.keys())}"


class Wall:

    def __init__(self, width=0, length=0, height=0):
        self.identifier = None
        self.width = width
        self.length = length
        self.height = height

    def __str__(self):
        return f"{self.identifier}  (width: {self.width}, height: {self.height}, length: {self.length})"


class Floor:

    def __init__(self, material=None, color=None, pattern=None):
        self.identifier = None
        self.material = material
        self.color = color
        self.pattern = pattern

    def __str__(self):
        return f"{self.identifier}  (material: {self.material}, color: {self.color}, pattern: {self.pattern})"


class SwimmingPool:

    def __init__(self, width=0, length=0, height=0, slope=0):
        self.identifier = None
        self.width = width
        self.length = length
        self.height = height
        self.slope = slope

    def __str__(self):
        return f"{self.identifier}  (width: {self.width}, length: {self.length}, height: {self.height}," \
               f"slope: {self.slope})"


class Balcony:

    def __init__(self, width=0, length=0, height=0):
        self.identifier = None
        self.width = width
        self.length = length
        self.height = height

    def __str__(self):
        return f"{self.identifier} (width: {self.width}, height: {self.height}, length: {self.length})"


if __name__ == "__main__":

    builder = HouseBuilder()

    print("House 1: ")
    builder.add_wall()
    builder.add_floor()
    builder.add_balcony()
    house = builder.house()
    print(house.wall)
    print(house.floor)
    print(house.balcony)
    print(house.list_components())

    print("\n")

    builder = HouseBuilder()
    print("House 2: ")
    wall = Wall(10,20,2)
    builder.add_wall(wall, "kitchen_wall")
    floor = Floor("wood", "brown", "square")
    builder.add_floor(floor, "kitchen_floor")
    balcony = Balcony(1, 3, 0.5)
    builder.add_balcony(balcony, "main_balcony")
    swimming_pool = SwimmingPool(10, 30, 2.2, 10)
    builder.add_swimming_pool(swimming_pool, "infinity_pool")
    house = builder.house()
    print(house.kitchen_wall)
    print(house.kitchen_floor)
    print(house.main_balcony)
    print(house.infinity_pool)
    print(house.list_components())


# output
'''
House 1:
wall  (width: 0, height: 0, length: 0)
floor  (material: None, color: None, pattern: None)
balcony (width: 0, height: 0, length: 0)
House components: wall, floor, balcony


House 2:
kitchen_wall  (width: 10, height: 2, length: 20)
kitchen_floor  (material: wood, color: brown, pattern: square)
main_balcony (width: 1, height: 0.5, length: 3)
infinity_pool  (width: 10, length: 30, height: 2.2,slope: 10)
House components: kitchen_wall, kitchen_floor, main_balcony, infinity_pool
'''