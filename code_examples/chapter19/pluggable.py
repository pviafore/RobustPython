import itertools
from stevedore import extension


Recipe = str
Dish = str

def get_inventory():
    return {}

def get_all_recipes() -> list[Recipe]:
    mgr = extension.ExtensionManager(
            namespace='ultimate_kitchen_assistant.recipe_maker',
            invoke_on_load=True,
        )

    def get_recipes(extension):
        return extension.obj.get_recipes()

    return list(itertools.chain.from_iterable(mgr.map(get_recipes)))

from stevedore import driver

def make_dish(recipe: Recipe, module_name: str) -> Dish:
    mgr = driver.DriverManager(
        namespace='ultimate_kitchen_assistant.recipe_maker',
        name=module_name,
        invoke_on_load=True,
    )

    return mgr.driver.prepare_dish(get_inventory(), recipe)

assert get_all_recipes() == ["Linguine", "Spaghetti", "Taco"]

assert make_dish("Linguine", "pasta_maker") == "Prepared Linguine"
