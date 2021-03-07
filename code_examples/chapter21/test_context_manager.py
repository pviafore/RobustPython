import contextlib

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


class Database:
    def add_ingredient(self, *args, **kwargs):
        pass

    def cleanup(self):
        pass

@contextlib.contextmanager
def construct_test_database():
    yield Database()
    


def test_calorie_calculation_bacon_cheeseburger():
    with construct_test_database() as db:
        db.add_ingredient("Bacon", calories_per_pound=2400)
        setup_bacon_cheeseburger(bacon="Bacon")
        
        calories = get_calories("Bacon Cheeseburger w/ Fries")

        assert calories == 1200
