from enum import IntEnum

# specifically using IntEnum for legacy reasons
# in new code, Enum would be better
class HeatLevel(IntEnum):
    LOW = 1
    MEDIUM_LOW = 3
    MEDIUM = 5
    MEDIUM_HIGH = 7
    HIGH = 10

class Ingredient:

    def __init__(self, name, amount, units):
        self.name = name
        self.amount = amount
        self.units = units 

    def adjust_proportion(self, factor):
        self.amount *= factor


# These funcitons are "fake" instructions, they don't actually control a robot, but
# will print out what they are doing.
def put_receptacle_on_stovetop(receptacle, heat_level):
    print(f"Putting {receptacle.name} on {heat_level}")

def add_ingredient(receptacle, ingredient):
    print(f"Adding {ingredient.amount} {ingredient.units} of {ingredient.name} to {receptacle.name}")

def brown_on_all_sides(ingredient_name):
    print(f"Browning {ingredient_name} on all sides")

def slice(ingredient, *ingredients, thickness_in_inches, to_ignore=[]):
    names = [ing.name for ing in ([ingredient] + list(ingredients)) if ing.name not in to_ignore]
    print(f"Slicing {','.join(names)} in {thickness_in_inches} inches")
    return Ingredient('Sliced '+','.join(names), 1, 'group')

def dice(ingredient, *ingredients, to_ignore=[]):
    names = [ing.name for ing in ([ingredient] + list(ingredients)) if ing.name not in to_ignore]
    print(f"Dicing {','.join(names)}")
    return Ingredient('Diced '+','.join(names), 1, 'group')

def is_not_cooked(_):
    return False

def chiffonade(ingredient):
    print(f"Slicing {ingredient.name} into ribbons")
    return Ingredient('Chiffonade ' + ingredient.name, ingredient.amount, ingredient.units)

def set_stir_mode(receptacle, frequency):
    print(f"Stirring {receptacle.name} {frequency}")


class Dish:
    pass

def divide(receptacle, servings):
    print(f"Dividing contents of {receptacle.name} into {servings} servings")
    return [Dish() for _ in range(servings)]

def grate(ingredient):
    print(f"Grating {ingredient.name}")
    return ingredient

def garnish(dishes, ingredient):
    print(f"Garnishing each dish with {ingredient.amount / len(dishes)} {ingredient.units} of {ingredient.name}")
