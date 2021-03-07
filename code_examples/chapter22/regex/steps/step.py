from behave import use_step_matcher

use_step_matcher("re")

def create_dish(dish_name):
    pass

@given("an order containing [a |an ]?(?P<dish_name>.*)")
def setup_order(context, dish_name):
    context.dish = create_dish(dish_name)
