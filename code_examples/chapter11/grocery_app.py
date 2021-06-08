import decimal
from dataclasses import dataclass
from enum import auto, Enum
from typing import Dict, Iterable, List, Tuple

class ImperialMeasure(Enum):
    TEASPOON = auto()
    TABLESPOON = auto()
    CUP = auto()

@dataclass(frozen=True)
class Ingredient:
    name: str
    brand: str
    amount: float = 1
    units: ImperialMeasure = ImperialMeasure.CUP

    def __add__(self, rhs: 'Ingredient'):
        # make sure we are adding the same ingredient
        assert (self.name, self.brand) == (rhs.name, rhs.brand)
        # build up conversion chart (lhs, rhs): multiplication factor
        conversion: dict[tuple[ImperialMeasure, ImperialMeasure], float] = {
            (ImperialMeasure.CUP, ImperialMeasure.CUP): 1,
            (ImperialMeasure.CUP, ImperialMeasure.TABLESPOON): 16,
            (ImperialMeasure.CUP, ImperialMeasure.TEASPOON): 48,
            (ImperialMeasure.TABLESPOON, ImperialMeasure.CUP): 1/16,
            (ImperialMeasure.TABLESPOON, ImperialMeasure.TABLESPOON): 1,
            (ImperialMeasure.TABLESPOON, ImperialMeasure.TEASPOON): 3,
            (ImperialMeasure.TEASPOON, ImperialMeasure.CUP): 1/48,
            (ImperialMeasure.TEASPOON, ImperialMeasure.TABLESPOON): 1/3,
            (ImperialMeasure.TEASPOON, ImperialMeasure.TEASPOON): 1
        }

        return Ingredient(rhs.name,
                          rhs.brand,
                          rhs.amount + self.amount * conversion[(rhs.units, self.units)],
                          rhs.units)


@dataclass
class Recipe:
    name: str
    ingredients: list[Ingredient]
    servings: int

from dataclasses import dataclass

@dataclass(frozen=True)
class Coordinates:
    lat: float
    lon: float

@dataclass(frozen=True)
class Store:
    coordinates: Coordinates
    name: str


@dataclass
class Item:
    name: str
    brand: str
    measure: ImperialMeasure
    price_in_cents: decimal.Decimal
    amount: float

Inventory = dict[Store, list[Item]]

spaghetti = Item(
    "Spaghetti",
    "Pat's Homemade",
    ImperialMeasure.CUP,
    amount=4,
    price_in_cents=decimal.Decimal(160)
)
reserved_items: list[Item] = []
delivered_items: list[Item] = []
def get_grocery_inventory() -> Inventory:
    # reach out to APIs and populate the dictionary
    return {
        Store(Coordinates(0,0), "Pat's Market") : [spaghetti]
    }

def reserve_items(store: Store, items: Iterable[Item]) -> bool:
    return True

def unreserve_items(store: Store, items: Iterable[Item]) -> bool:
    return True

def order_items(store: Store, items: Iterable[Item]) -> bool:
    return True


from typing import Iterable, Optional, Set
from copy import deepcopy
class Order:
    ''' An Order class that represents a list of ingredients '''
    def __init__(self, recipes: Iterable[Recipe]):
        self.__confirmed = False
        self.__ingredients: set[Ingredient] = set()
        for recipe in recipes:
            for ingredient in recipe.ingredients:
                self.add_ingredient(ingredient)

    def get_ingredients(self) -> list[Ingredient]:
        ''' Return a alphabetically sorted list of ingredients '''
        # return a copy so that users won't inadvertently mess with
        # our internal data
        return sorted(deepcopy(self.__ingredients),
                         key=lambda ing: ing.name)

    def _get_matching_ingredient(self,
                                 ingredient: Ingredient) -> Optional[Ingredient]:
        try:
            return next(ing for ing in self.__ingredients if
                        ((ing.name, ing.brand) ==
                         (ingredient.name, ingredient.brand)))
        except StopIteration:
            return None

    def add_ingredient(self, ingredient: Ingredient):
        ''' adds the ingredient if it's not already added,
            or increases the amount if it has
        '''
        target_ingredient = self._get_matching_ingredient(ingredient)
        if target_ingredient is None:
            # ingredient for the first time - add it
            self.__ingredients.add(ingredient)
        else:
            # add ingredient to existing set
            target_ingredient += ingredient

    def confirm(self):
        self.__confirmed = True

    def unconfirm(self):
        self.__confirmed = False

    def is_confirmed(self):
        return self.__confirmed

def display_order(order: Order):
    pass
def wait_for_user_order_confirmation(order: Order):
    order.confirm()
    pass

class _GroceryList:
    def __init__(self, order: Order, grocery_inventory: Inventory):
        self.order = order
        self.inventory = grocery_inventory

    def is_confirmed(self):
        return True

    def order_and_unreserve_items(self):
        pass

    def reserve_items_from_stores(self):
        pass

    def unreserve_items(self):
        pass

    def has_reserved_items(self):
        pass

    def get_grocery_order(self) -> list[Item]:
        return [spaghetti]

def wait_for_user_grocery_confirmation(grocery_list: _GroceryList):
    pass

def deliver_ingredients(grocery_list: _GroceryList):
    global delivered_items
    delivered_items += grocery_list.get_grocery_order()

from contextlib import contextmanager

@contextmanager
def create_grocery_list(order: Order, inventory: Inventory):
    grocery_list = _GroceryList(order, inventory)
    try:
        yield grocery_list
    finally:
        if grocery_list.has_reserved_items():
            grocery_list.unreserve_items()

def make_order(recipes):
    order = Order(recipes)
    # the user can make changes if needed
    display_order(order)
    wait_for_user_order_confirmation(order)
    if order.is_confirmed():
        grocery_inventory = get_grocery_inventory()
        with create_grocery_list(order, grocery_inventory) as grocery_list:
            grocery_list.reserve_items_from_stores()
            wait_for_user_grocery_confirmation(grocery_list)
            if grocery_list.is_confirmed():
                grocery_list.order_and_unreserve_items()
                deliver_ingredients(grocery_list)

def test_order():
    make_order([Recipe(name="Pasta", ingredients=[Ingredient(
        "Spaghetti",
        "Pat's Homemade",
        units=ImperialMeasure.CUP,
        amount=2)], servings=1)])
    assert reserved_items == []
    assert delivered_items == [spaghetti]

if __name__ == "__main__":
    test_order()
