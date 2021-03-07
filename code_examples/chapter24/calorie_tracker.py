from dataclasses import dataclass
from enum import Enum

@dataclass
class Meal:
    name: str
    calories: int


class WarningType(Enum):
    OVER_CALORIE_LIMIT = 0

warnings = []
checkmarks = []

def display_warning(meal, warning_type):
    warnings.append(meal)

def display_checkmark(meal):
    checkmarks.append(meal)

def clear_warnings():
    warnings.clear()
    checkmarks.clear()

def check_meals_for_calorie_overage(meals: list[Meal], target: int):
    for meal in meals:
        target -= meal.calories
        if target < 0:
            display_warning(meal, WarningType.OVER_CALORIE_LIMIT)
            continue
        display_checkmark(meal)
