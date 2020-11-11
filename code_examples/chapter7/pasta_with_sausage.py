from fractions import Fraction
import time

import code_examples.chapter7.automated_recipe_maker as automated_recipe_maker
from code_examples.chapter7.automated_recipe_maker import Ingredient


# I am purposely not using dataclasses here in order to 
# simulate a more "legacy" codebase. If new code, these should be dataclasses
class Recipe:

    def __init__(self, servings, ingredients):
        self.servings = servings
        self.ingredients = ingredients

    def clear_ingredients(self):
        self.ingredients.clear()

    def get_ingredient(self, name):
        return next(i for i in self.ingredients if i.name == name)
    
# Take a meal recipe and change the number of servings
# recipe is a Recipe class
def adjust_recipe(recipe, servings):
    new_ingredients = list(recipe.ingredients)
    recipe.clear_ingredients()
    for ingredient in new_ingredients:
        ingredient.adjust_proportion(Fraction(servings, recipe.servings))
    return Recipe(servings, new_ingredients)


# Pasta with Sasuage Automated Maker
italian_sausage = Ingredient('Italian Sausage', 4, 'links')
olive_oil = Ingredient('Olive Oil', 1, 'tablespoon')
plum_tomato = Ingredient('Plum Tomato', 6, '')
garlic = Ingredient('Garlic', 4, 'cloves')
black_pepper = Ingredient('Black Pepper', 2, 'teaspoons')
basil = Ingredient('Basil Leaves', 1, 'cup')
pasta = Ingredient('Rigatoni', 1, 'pound')
salt = Ingredient('Salt', 1, 'tablespoon')
water = Ingredient('Water', 6, 'quarts')
cheese = Ingredient('Pecorino Romano', 2, "ounces")
pasta_with_sausage = Recipe(6, [italian_sausage,
                                olive_oil,
                                plum_tomato,
                                garlic,
                                black_pepper,
                                pasta,
                                salt,
                                water,
                                cheese,
                                basil])

class Receptacle:
    '''
    A class that stores various ingredients
    '''

    def __init__(self, name):
        self.name = name
        self.ingredients = []

    def add(self, ingredient):
        self.ingredients.append(ingredient)
        automated_recipe_maker.add_ingredient(self, ingredient)
    
    def remove_ingredients(self, to_ignore=[]):
        names = [ing.name for ing in self.ingredients if ing.name not in to_ignore]
        self.ingredients.clear()
        return Ingredient('/'.join(names), 1, 'Mixture')


        
def make_pasta_with_sausage(servings):
    sauté_pan = Receptacle('Sauté Pan')
    pasta_pot = Receptacle('Stock Pot')
    adjusted_recipe = adjust_recipe(pasta_with_sausage, servings)

    print("Prepping ingredients")
    garlic_and_tomatoes = automated_recipe_maker.dice(adjusted_recipe.get_ingredient('Plum Tomato'),
                                                      adjusted_recipe.get_ingredient('Garlic'))
    grated_cheese = automated_recipe_maker.grate(adjusted_recipe.get_ingredient('Pecorino Romano'))
    sliced_basil = automated_recipe_maker.chiffonade(adjusted_recipe.get_ingredient('Basil Leaves'))

    print("Cooking Pasta")
    pasta_pot.add(adjusted_recipe.get_ingredient('Water'))
    pasta_pot.add(adjusted_recipe.get_ingredient('Salt'))
    automated_recipe_maker.put_receptacle_on_stovetop(pasta_pot, 10)
    pasta_pot.add(adjusted_recipe.get_ingredient('Rigatoni'))
    automated_recipe_maker.set_stir_mode(pasta_pot, ('every minute'))

    print("Cooking Sausage")
    sauté_pan.add(adjusted_recipe.get_ingredient('Olive Oil'))
    medium = automated_recipe_maker.HeatLevel.MEDIUM
    automated_recipe_maker.put_receptacle_on_stovetop(sauté_pan, medium)
    sauté_pan.add(adjusted_recipe.get_ingredient('Italian Sausage'))
    automated_recipe_maker.brown_on_all_sides('Italian Sausage')
    cooked_sausage = sauté_pan.remove_ingredients(to_ignore=['Olive Oil'])

    sliced_sausage = automated_recipe_maker.slice(cooked_sausage, thickness_in_inches=.25)

    print("Making Sauce")
    sauté_pan.add(garlic_and_tomatoes)
    automated_recipe_maker.set_stir_mode(sauté_pan, ('every minute'))
    while automated_recipe_maker.is_not_cooked('Rigatoni'):
        time.sleep(30)
    cooked_pasta = pasta_pot.remove_ingredients(to_ignore=['Water', 'Salt'])

    sauté_pan.add(sliced_sausage)
    while automated_recipe_maker.is_not_cooked('Italian Sausage'):
        time.sleep(30)

    print("Mixing ingredients together")
    sauté_pan.add(sliced_basil)
    sauté_pan.add(cooked_pasta)
    automated_recipe_maker.set_stir_mode(sauté_pan, "once")

    print("Serving")
    dishes = automated_recipe_maker.divide(sauté_pan, servings)
    

    automated_recipe_maker.garnish(dishes, grated_cheese)
    return dishes


make_pasta_with_sausage(3)
