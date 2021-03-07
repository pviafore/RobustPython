import pytest


class Database:
    def add_ingredient(self, *args, **kwargs):
        pass

    def cleanup(self):
        pass

def setup_dish_ingredients(args, **kwargs):
    pass

@pytest.fixture
def db_creation():
    # ... snip  set up local sqlite database
    return Database()


@pytest.fixture
def test_database(db_creation):
    # ... snip adding all ingredients and meals
    return db_creation


def get_calories(dish: str):
    return {
        "Bacon Cheeseburger": 900,
        "Cobb Salad": 1000,
        "Buffalo Wings": 800,
        "Garlicky Brussels Sprouts": 200,
        "Mashed Potatoes": 400
    }[dish]



@pytest.mark.parametrize(
    "extra_ingredients,dish_name,expected_calories", 
    [
        (["Bacon", 2400], "Bacon Cheeseburger", 900),
        ([],  "Cobb Salad", 1000),
        ([],  "Buffalo Wings", 800),
        ([],  "Garlicky Brussels Sprouts", 200),
        ([],  "Mashed Potatoes", 400)
    ]
)
def test_calorie_calculation_bacon_cheeseburger(extra_ingredients,
                                                dish_name, 
                                                expected_calories,
                                                test_database):
    for ingredient in extra_ingredients:
        test_database.add_ingredient(ingredient)

    # assume this function can set up any dish
    # alternatively, dish ingredients could be passed in as a test parameter
    setup_dish_ingredients(dish_name)
    
    calories = get_calories(dish_name)

    assert calories == expected_calories
