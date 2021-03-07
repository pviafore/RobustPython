def add_ingredient_to_database(*args, **kwargs):
    pass

def set_ingredients(*arg, **kwargs):
    pass

def get_calories(*args):
    return 1200

def cleanup_database():
    pass

def test_calorie_calculation():
    
    # arrange
    add_ingredient_to_database("Ground Beef", calories_per_pound=1500)
    add_ingredient_to_database("Bacon", calories_per_pound=2400)
    add_ingredient_to_database("Cheese", calories_per_pound=1800)
    # ... snip ingredients

    set_ingredients("Bacon Cheeseburger w/ Fries",
                    ingredients=["Ground Beef", "Bacon"])
    
    # act
    calories = get_calories("Bacon Cheeseburger w/ Fries")

    # assert
    assert calories == 1200

    #annihilate
    cleanup_database()
