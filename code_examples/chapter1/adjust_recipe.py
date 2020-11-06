# Take a meal recipe and change the number of servings
# by adjusting each ingredient
# A recipe's first element is the number of servings, and the remainder
# of elements is (name, amount, unit), such as ("flour", 1.5, "cup")

def adjust_recipe(recipe, servings):
    new_recipe = [servings]
    old_servings = recipe[0]
    factor = servings / old_servings
    recipe.pop(0)
    while recipe:
        ingredient, amount, unit = recipe.pop(0)
        # please only use numbers that will be easily measurable
        new_recipe.append((ingredient, amount * factor, unit))
    return new_recipe


def test_adjust_recipe():
    old_recipe = [2, ("flour", 1.5, "cups")]
    adjusted = adjust_recipe(old_recipe, 4)
    assert [4, ("flour", 3, "cups")] == adjusted
    assert old_recipe == []


test_adjust_recipe()
