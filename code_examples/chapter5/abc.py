import collections
import collections.abc
from typing import Set 


def get_nutrition_information(text):
    return "arugula"

def get_aliases(text):
    if text == 'rocket':
        return ['arugula']

class AliasedIngredients(collections.abc.Set):
    def __init__(self, ingredients: set[str]):
        self.ingredients = ingredients
    
    def __contains__(self, value: str):
        return value in self.ingredients or any(alias in self.ingredients for alias in get_aliases(value))

    def __iter__(self):
        return iter(self.ingredients)

    def __len__(self):
        return len(self.ingredients)

ingredients = AliasedIngredients({'arugula', 'eggplant', 'pepper'})
assert ingredients == {'arugula', 'eggplant', 'pepper'}

assert len(ingredients) == 3

assert 'arugula' in ingredients
assert 'rocket' in ingredients
