from abc import abstractmethod
from typing import runtime_checkable, Protocol

Dish = str
Ingredient = str
Recipe = str
Amount = str

@runtime_checkable
class UltimateKitchenAssistantModule(Protocol):
    
    ingredients: list[Ingredient]

    @abstractmethod
    def get_recipes() -> list[Recipe]:
        raise NotImplementedError

    @abstractmethod
    def prepare_dish(inventory: dict[Ingredient, Amount], recipe: Recipe) -> Dish:
        raise NotImplementedError
