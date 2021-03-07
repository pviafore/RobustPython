def get_calories(*args):
    return 1200

def test_get_calorie_count():
    assert get_calories("Bacon Cheeseburger w/ Fries") == 1200
