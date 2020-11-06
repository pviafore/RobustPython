from typing import TypedDict


recipe_name = 'Pasta Bolognese'
def get_nutrition_from_spoonacular(recipe: str):
    return RecipeNutritionInformation({
        'recipes_used': 1,
        "calories": {
            'value': 1,
            'unit': 'g',
            'confidenceRange95Percent': {
                'min': 1,
                'max': 2
            },
            'standardDeviation': 3.5
        },
        "fat": {
            'value': 1,
            'unit': 'g',
            'confidenceRange95Percent': {
                'min': 1,
                'max': 2
            },
            'standardDeviation': 3.5
        },
        "protein": {
            'value': 1,
            'unit': 'g',
            'confidenceRange95Percent': {
                'min': 1,
                'max': 2
            },
            'standardDeviation': 3.5
        },
        "carbs": {
            'value': 1,
            'unit': 'g',
            'confidenceRange95Percent': {
                'min': 1,
                'max': 2
            },
            'standardDeviation': 3.5
        }
    })

class Range(TypedDict):
    min: float
    max: float

class NutritionInformation(TypedDict):
    value: int
    unit: str
    confidenceRange95Percent: Range
    standardDeviation: float

class RecipeNutritionInformation(TypedDict):
    recipes_used: int
    calories: NutritionInformation
    fat: NutritionInformation
    protein: NutritionInformation
    carbs: NutritionInformation

nutrition_information:RecipeNutritionInformation = get_nutrition_from_spoonacular(recipe_name)
