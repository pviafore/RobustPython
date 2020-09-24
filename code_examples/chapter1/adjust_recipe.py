from typing import List, Tuple
# Take a meal recipe and change the number of servings
def adjust_recipe(recipe: List[Tuple[str, float, str]],
                  servings: int):
    new_recipe = [("servings", float(servings), "")]
    old_servings = recipe[0][1]
    factor = servings / old_servings
    recipe.pop(0)
    while recipe:
        ingredient, amount, unit = recipe.pop(0)
        # please only use numbers that will be easily measurable
        new_recipe.append((ingredient, amount * factor, unit))
    return new_recipe


def test_adjust_recipe():
    old_recipe = [("servings", 2, ""), ("flour", 1.5, "cups")]
    adjusted = adjust_recipe(old_recipe, 4)
    assert [("servings", 4, ""), ("flour", 3, "cups")] == adjusted
    assert old_recipe == []


test_adjust_recipe()
