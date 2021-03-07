import pytest



class Database:
    def add_ingredient(self, *args, **kwargs):
        pass

    def cleanup(self):
        pass

@pytest.fixture
def db_creation():
    # ... snip  set up local sqlite database
    return Database()

def setup_bacon_cheeseburger(**kwargs):
    pass

def get_calories(*args):
    return 1200

@pytest.fixture
def test_database(db_creation):
    # ... snip adding all ingredients and meals
    return db_creation

def test_calorie_calculation_bacon_cheeseburger(test_database):
    test_database.add_ingredient("Bacon", calories_per_pound=2400)
    setup_bacon_cheeseburger(bacon="Bacon")
    
    calories = get_calories("Bacon Cheeseburger w/ Fries")

    assert calories == 1200

    test_database.cleanup()
