from calorie_tracker import check_meals_for_calorie_overage, checkmarks, clear_warnings, Meal, warnings

def assert_no_warnings_displayed_on_meal(meal_name):
    assert all(m.name != meal_name for m in warnings)

def assert_checkmark_on_meal(meal_name):
    assert any(m.name == meal_name for m in checkmarks)

def assert_meal_is_over_calories(meal_name):
    assert any(m.name == meal_name for m in warnings)


def test_no_warnings_if_under_calories():
    clear_warnings()
    meals = [Meal("Fish 'n' Chips", 1000)]
    check_meals_for_calorie_overage(meals, 1200)
    assert_no_warnings_displayed_on_meal("Fish 'n' Chips")
    assert_checkmark_on_meal("Fish 'n' Chips")

def test_no_exception_thrown_if_no_meals():
    clear_warnings()
    check_meals_for_calorie_overage([], 1200)
    # no explicit assert, just checking for no exceptions

def test_meal_is_marked_as_over_calories():
    clear_warnings()
    meals = [Meal("Fish 'n' Chips", 1000)]
    check_meals_for_calorie_overage(meals, 900)
    assert_meal_is_over_calories("Fish 'n' Chips")

def test_meal_going_over_calories_does_not_conflict_with_previous_meals():
    clear_warnings()
    meals = [Meal("Fish 'n' Chips", 1000), Meal("Banana Split", 400)]
    check_meals_for_calorie_overage(meals, 1200)
    assert_no_warnings_displayed_on_meal("Fish 'n' Chips")
    assert_checkmark_on_meal("Fish 'n' Chips")
    assert_meal_is_over_calories("Banana Split")    
