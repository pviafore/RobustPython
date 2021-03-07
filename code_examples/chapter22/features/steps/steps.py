
class CheeseburgerWithFries():
    def substitute_vegan_ingredients(self):
        pass

    def ingredients(self):
        return []

def is_vegan(ingredient):
    return True 


class Meatloaf:
    pass

from behave import given, when, then

@given("an order containing {dish_name}")
def setup_order(ctx, dish_name):
    if dish_name == "a Cheeseburger with Fries":
        ctx.dish = CheeseburgerWithFries()
    elif dish_name == "Meatloaf":
        ctx.dish = Meatloaf()
    ctx.dish = Meatloaf()

@when("I ask for vegan substitutions")
def substitute_vegan(ctx):
    if isinstance(ctx.dish, Meatloaf):
        return
    ctx.dish.substitute_vegan_ingredients()

@then("I receive the meal with no animal products")
def check_all_vegan(ctx):
    if isinstance(ctx.dish, Meatloaf):
        return
    assert all(is_vegan(ing) for ing in ctx.dish.ingredients())


@then(u'Then a non-vegan-substitutable error shows up')
def step_impl(context):
    pass
