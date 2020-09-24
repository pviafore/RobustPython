from typing import List, Tuple
# Take a meal recipe and change the number of servings
def adjust_recipe(recipe: List[Tuple[str, float, str]],
                  servings: int):
    old_servings = recipe.pop(0)[1]
    factor = servings / old_servings
    return {"servings": servings} | \
           {ingredient: (amount*factor, unit)
            for ingredient, amount, unit in recipe}

    
def test_adjust_recipe():
    old_recipe = [("servings", 2, ""), ("flour", 1.5, "cups")]
    adjusted = adjust_recipe(old_recipe, 4)
    assert {"servings": 4, "flour": (3, "cups")} == adjusted
    
    # THIS IS WRONG BEHAVIOR, we should have emptied the list
    assert old_recipe != []


test_adjust_recipe()
