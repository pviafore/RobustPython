def add_base_ingredients_to_database():
    pass

def add_ingredient_to_database(*args, **kwargs):
    pass


calories = 0 

def setup_bacon_cheeseburger(bacon):
    global calories
    calories = 1100 if "Turkey" in bacon else 1200

def get_calories(*args):
    return calories

def cleanup_database():
    pass


def test_calorie_calculation_bacon_cheeseburger():
    add_base_ingredients_to_database()
    add_ingredient_to_database("Bacon", calories_per_pound=2400)
    setup_bacon_cheeseburger(bacon="Bacon")
    
    calories = get_calories("Bacon Cheeseburger w/ Fries")

    assert calories == 1200

    cleanup_database()

def test_calorie_calculation_bacon_cheeseburger_with_substitution():
    add_base_ingredients_to_database()
    add_ingredient_to_database("Turkey Bacon", calories_per_pound=1700)
    setup_bacon_cheeseburger(bacon="Turkey Bacon")
    
    calories = get_calories("Bacon Cheeseburger w/ Fries")

    assert calories == 1100

    cleanup_database()
