from dataclasses import dataclass
from enum import Enum

@dataclass
class Meal:
    name: str
    calories: int

class Recommendation(Enum):
    BY_CALORIES = 0

def is_appetizer(dish):
    return dish.name in ["Spring Roll"]

def is_salad(dish):
    return dish.name in ["Green Papaya Salad"]

def is_main_dish(dish):
    return dish.name in ["Larb Chicken"]

from hypothesis import given, example
from hypothesis.strategies import integers


def get_recommended_meal(Recommendation, calories: int) -> list[Meal]:
    return [Meal("Spring Roll", 120),
            Meal("Green Papaya Salad", 230),
            Meal("Larb Chicken", 500)]

@given(integers(min_value=900))
def test_meal_recommendation_under_specific_calories(calories):
    meals = get_recommended_meal(Recommendation.BY_CALORIES, calories)
    assert len(meals) == 3
    assert is_appetizer(meals[0])
    assert is_salad(meals[1])
    assert is_main_dish(meals[2])
    assert sum(meal.calories for meal in meals) < calories
