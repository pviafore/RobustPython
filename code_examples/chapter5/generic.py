
from typing import TypeVar,Union,List
T = TypeVar("T")

class NutritionInfo:
    pass

class Ingredient:
    pass

class Restaurant:
    pass

class APIErrorResponse:
    pass

APIResponse = Union[T, APIErrorResponse]

def get_nutrition_info(recipe: str) -> APIResponse[NutritionInfo]:
     return APIErrorResponse() 

def get_ingredients(recipe: str) -> APIResponse[list[Ingredient]]:
    return []

def get_restaurants_serving(recipe: str) -> APIResponse[list[Restaurant]]:
    return [Restaurant()] 
