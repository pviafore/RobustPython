
from ultimate_kitchen_assistant.plugin_spec import UltimateKitchenAssistantModule

Ingredient = str
Amount = str
Recipe = str
Dish = str

class TexMexModule(UltimateKitchenAssistantModule):
    def __init__(self):
        self.ingredients = ["Tortilla", 
                            "Beef" ]

    def get_recipes(self) -> list[Recipe]:
        return ["Taco"]

    def prepare_dish(self, inventory: dict[Ingredient, Amount], recipe: Recipe) -> Dish:
        assert False, "No dishes supported in test application"
