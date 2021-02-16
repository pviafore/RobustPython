from dataclasses import dataclass
from typing import Callable

import itertools

Meal = str

@dataclass
class RecommendationPolicy:
    meals: list[str]
    initial_sorting_criteria: Callable
    grouping_criteria: Callable
    secondary_sorting_criteria: Callable
    selection_criteria: Callable
    desired_number_of_recommendations: int

def recommend_meal(policy: RecommendationPolicy) -> list[Meal]:
    meals = policy.meals
    sorted_meals = sorted(meals, key=policy.initial_sorting_criteria, reverse=True)
    grouped_meals = itertools.groupby(sorted_meals, key=policy.grouping_criteria)
    _, top_grouped = next(grouped_meals)
    secondary_sorted = sorted(top_grouped, key=policy.secondary_sorting_criteria, reverse=True)
    candidates = itertools.takewhile(policy.selection_criteria, secondary_sorted)
    return list(candidates)[:policy.desired_number_of_recommendations]


# dummy functions to get code to run
def get_specials():
    return ["abc", "d", "efghi", "jk", "l", "mno", "p"]

def get_proximity_to_surplus_ingredients(meal):
    return len(meal)

get_proximity_to_last_meal = get_proximity_to_surplus_ingredients

def proximity_greater_than_75_percent(meal):
    return len(meal) > .75


meal = recommend_meal(RecommendationPolicy(
    meals=get_specials(),
    initial_sorting_criteria=get_proximity_to_surplus_ingredients,
    grouping_criteria=get_proximity_to_surplus_ingredients,
    secondary_sorting_criteria=get_proximity_to_last_meal,
    selection_criteria=proximity_greater_than_75_percent,
    desired_number_of_recommendations=3)
)

assert meal == ["efghi"]
