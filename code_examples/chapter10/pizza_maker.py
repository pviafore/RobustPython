from typing import List

def is_sauce(t):
    return t in ['Tomato Sauce', "Olive Oil"]

class PizzaSpecification:
    def __init__(self,
                  dough_radius_in_inches: int,
                  toppings: list[str]):
        assert 6 <= dough_radius_in_inches <= 12, \
            'Dough must be between 6 and 12 inches'
        sauces = [t for t in toppings if is_sauce(t)]
        assert len(sauces) < 2, \
            'Can only have at most one sauce'

        self.dough_radius_in_inches = dough_radius_in_inches
        sauce = sauces[:1]
        self.toppings = sauce + \
            [t for t in toppings if not is_sauce(t)]

PizzaSpecification(10, ['Tomato Sauce', 'Basil'])


import contextlib

@contextlib.contextmanager
def create_pizza_specification(dough_radius_in_inches: int,
    toppings):
    pizza_spec = PizzaSpecification(dough_radius_in_inches, toppings)
    yield pizza_spec
    assert 6 <= pizza_spec.dough_radius_in_inches <= 12
    sauces = [t for t in pizza_spec.toppings if is_sauce(t)]
    assert len(sauces) < 2
    if sauces:
        assert pizza_spec.toppings[0] == sauces[0]

    # check that we assert order of all non sauces 
    # keep in mind, no invariant is specified that we can't add
    # toppings at a later date, so we only check against what was
    # passed in
    non_sauces = [t for t in pizza_spec.toppings if t not in sauces]
    expected_non_sauces = [t for t in toppings if t not in sauces]
    for expected, actual in zip(expected_non_sauces, non_sauces):
        assert expected == actual
    

def test_pizza_operations():
    with create_pizza_specification(8, ["Tomato Sauce", "Peppers"]) \
        as pizza_spec:
        
        assert pizza_spec.toppings == ["Tomato Sauce", "Peppers"] 

test_pizza_operations


pizza_spec = PizzaSpecification(dough_radius_in_inches=8, 
                                toppings=['Olive Oil',
                                          'Garlic',
                                          'Sliced Roma Tomatoes',
                                          'Mozzarella'])

pizza_spec.dough_radius_in_inches = 100  # BAD!
assert pizza_spec.dough_radius_in_inches == 100
pizza_spec.toppings.append('Tomato Sauce')  # Second Sauce, oh no
