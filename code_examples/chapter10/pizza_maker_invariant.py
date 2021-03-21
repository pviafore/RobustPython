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

        self.__dough_radius_in_inches = dough_radius_in_inches # <1>
        sauce = sauces[:1]
        self.__toppings = sauce + \
            [t for t in toppings if not is_sauce(t)] # <2>

pizza_spec = PizzaSpecification(dough_radius_in_inches=8, 
                                toppings=['Olive Oil',
                                          'Garlic',
                                          'Sliced Roma Tomatoes',
                                          'Mozzarella'])


pizza_spec = PizzaSpecification(dough_radius_in_inches=8, 
                                toppings=['Olive Oil',
                                          'Garlic',
                                          'Sliced Roma Tomatoes',
                                          'Mozzarella'])

try:
    pizza_spec.__toppings.append('Tomato Sauce') # OOPS
    assert False
except AttributeError:
    pass

assert pizza_spec.__dict__ == { '_PizzaSpecification__toppings': ['Olive Oil',
                                        'Garlic',
                                        'Sliced Roma Tomatoes',
                                        'Mozzarella'],
      '_PizzaSpecification__dough_radius_in_inches': 8 
}


pizza_spec._PizzaSpecification__dough_radius_in_inches = 100 # type: ignore
assert pizza_spec._PizzaSpecification__dough_radius_in_inches == 100 # type: ignore
