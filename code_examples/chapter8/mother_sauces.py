from typing import List

from enum import Enum
class MotherSauce(Enum):
    BÉCHAMEL = "Béchamel"
    VELOUTÉ = "Velouté"
    ESPAGNOLE = "Espagnole"
    TOMATO = "Tomato"
    HOLLANDAISE = "Hollandaise"


MotherSauce.BÉCHAMEL
MotherSauce.HOLLANDAISE



MotherSauce("Hollandaise") # OKAY

try:
    MotherSauce("Alabama White BBQ Sauce")
    assert False, "Should not consider BBQ sauce a mother sauce"
except:
    pass

print(list(enumerate(MotherSauce, start=1)))
assert list(enumerate(MotherSauce, start=1)) == [(1, MotherSauce.BÉCHAMEL), (2, MotherSauce.VELOUTÉ), (3, MotherSauce.ESPAGNOLE),
                                                 (4, MotherSauce.TOMATO), (5,MotherSauce.HOLLANDAISE)]
def create_daughter_sauce(mother_sauce: MotherSauce, 
                          extra_ingredients: list[str]):
    pass 

create_daughter_sauce(MotherSauce.TOMATO, [])
