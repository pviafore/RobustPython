
from collections import UserList
class Dish():

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def make_vegan(self):
        pass

    def ingredients(self):
        return ["Turkey Burger", "Bun"] 

def create_dish(name):
    return Dish(name)


from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.helpers.hasmethod import hasmethod

def is_vegan(ingredient: str) -> bool:
    return ingredient not in ["Beef Burger"]

class IsVegan(BaseMatcher):

    def _matches(self, dish):
        if not hasmethod(dish, "ingredients"):
            return False
        return all(is_vegan(ingredient) for ingredient in dish.ingredients())

    def describe_to(self, description):
        description.append_text("Expected dish to be vegan")

    def describe_mismatch(self, dish, description):
        message = f"the following ingredients are not vegan: "
        message += ", ".join(ing for ing in dish.ingredients() if not is_vegan(ing))
        description.append_text(message)


def vegan():
    return IsVegan()


from hamcrest import assert_that, is_
def test_vegan_substitution():
    dish = create_dish("Hamburger and Fries")
    dish.make_vegan()
    assert_that(dish, is_(vegan()))
