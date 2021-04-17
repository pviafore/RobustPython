from typing import List

def is_sauce(t):
    return t in ['Tomato Sauce', "Olive Oil"]

class PizzaException(RuntimeError):
    pass

class PizzaSpecification:
    def __init__(self,
                  dough_radius_in_inches: int,
                  toppings: list[str]):
        assert 6 <= dough_radius_in_inches <= 12, \
            'Dough must be between 6 and 12 inches'
        
        self.__dough_radius_in_inches = dough_radius_in_inches
        self.__toppings: list[str] = []
        for topping in toppings:
            self.add_topping(topping) # <1>


    def add_topping(self, topping: str): # <2>
        '''
        Add a topping to the pizza
        All rules for pizza construction (one sauce, no sauce above 
        cheese, etc.) still apply.
        '''
        if (is_sauce(topping) and 
               any(t for t in self.__toppings if is_sauce(t))):
               raise PizzaException('Pizza may only have one sauce')
        
        if is_sauce(topping):
            self.__toppings.insert(0, topping)
        else:
            self.__toppings.append(topping)
