import copy

from dataclasses import dataclass
from fractions import Fraction
from typing import List

@dataclass
class Ingredient:
    name: str
    amount: Fraction
    units: str

    def adjust_proportion(self, factor: Fraction):
        self.amount *= factor

@dataclass
class Recipe:
    servings: int
    ingredients: list[Ingredient]

    def clear_ingredients(self):
        self.ingredients.clear()

    def get_ingredients(self):
        return self.ingredients
    
# Take a meal recipe and change the number of servings
# recipe is a Recipe class
def adjust_recipe(recipe, servings):
    # create a copy of the ingredients
    new_ingredients = list(recipe.get_ingredients())
    recipe.clear_ingredients()
    for ingredient in new_ingredients:
        ingredient.adjust_proportion(Fraction(servings, recipe.servings))
    return Recipe(servings, new_ingredients)


def test_adjust_recipe():
    old_recipe = Recipe(2, [Ingredient('flour', 1.5, 'cups')])
    adjusted = adjust_recipe(old_recipe, 4)
    assert Recipe(4, [Ingredient('flour', 3, 'cups')]) == adjusted
    assert old_recipe.ingredients == []


test_adjust_recipe()
