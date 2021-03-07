import pytest



class Database:
    def add_ingredient(self, *args, **kwargs):
        pass

    def cleanup(self):
        pass

def setup_bacon_cheeseburger(**kwargs):
    pass

def get_calories(*args):
    return 1200


@pytest.fixture
def db_creation():
    # ... snip  set up local sqlite database
    return Database()

@pytest.fixture
def test_database(db_creation):
    # ... snip adding all ingredients and meals
    try:
        yield db_creation
    finally:
        db_creation.cleanup()

def test_calorie_calculation_bacon_cheeseburger(test_database):
    test_database.add_ingredient("Bacon", calories_per_pound=2400)
    setup_bacon_cheeseburger(bacon="Bacon")
    
    calories = get_calories("Bacon Cheeseburger w/ Fries")

    assert calories == 1200, "Calories for Bacon Cheeseburger were wrong"
