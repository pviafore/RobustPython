from collections import namedtuple
NutritionInformation = namedtuple('NutritionInformation', ['calories', 'fat', 'carbohydrates'])
nutrition = NutritionInformation(calories=100, fat=5, carbohydrates=10)
assert nutrition.calories == 100
