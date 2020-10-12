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

for sauce in MotherSauce:
    print(f"{sauce.name} {sauce.value}")

def create_daughter_sauce(mother_sauce: MotherSauce, 
                          extra_ingredients: List[str]):
    pass 

create_daughter_sauce(MotherSauce.TOMATO, [])
