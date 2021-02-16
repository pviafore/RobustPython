
from ultimate_kitchen_assistant.plugin_spec import UltimateKitchenAssistantModule

Ingredient = str
Amount = str
Recipe = str
Dish = str

class PastaModule(UltimateKitchenAssistantModule):
    def __init__(self):
        self.ingredients = ["Linguine", 
                            "Spaghetti" ]

    def get_recipes(self) -> list[Recipe]:
        return ["Linguine", "Spaghetti"]

    def prepare_dish(self, inventory: dict[Ingredient, Amount], recipe: Recipe) -> Dish:
        assert recipe == "Linguine"
        return "Prepared Linguine"
