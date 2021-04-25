# Take a meal recipe and change the number of servings
# by adjusting each ingredient
# A recipe's first element is the number of servings, and the remainder
# of elements is (name, amount, unit), such as ("flour", 1.5, "cup")
def adjust_recipe(recipe, servings):
    old_servings = recipe.pop(0)
    factor = servings / old_servings
    new_recipe = {ingredient: (amount*factor, unit) 
                  for ingredient, amount, unit in recipe} 
    new_recipe["servings"] = servings
    return new_recipe

    
def test_adjust_recipe():
    old_recipe = [2, ("flour", 1.5, "cups")]
    adjusted = adjust_recipe(old_recipe, 4)
    assert {"servings": 4, "flour": (3, "cups")} == adjusted
    
    # THIS IS WRONG BEHAVIOR, we should have emptied the list
    assert old_recipe != []


test_adjust_recipe()
