import os

def create_recipe_on_disk(recipe):
    command = "touch ~/food_data/{}.json".format(recipe)
    return os.system(command)

def create_recipe():
    recipe = input("Enter in recipe")
    create_recipe_on_disk(recipe)
