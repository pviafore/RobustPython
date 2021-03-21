from typing import List
BÉCHAMEL = "Béchamel"
VELOUTÉ = "Velouté"
ESPAGNOLE = "Espagnole"
TOMATO = "Tomato"
HOLLANDAISE = "Hollandaise"
MOTHER_SAUCES = (BÉCHAMEL, VELOUTÉ, ESPAGNOLE, TOMATO, HOLLANDAISE)

assert MOTHER_SAUCES[2] ==  "Espagnole"

def create_daughter_sauce(mother_sauce: str, 
                          extra_ingredients: list[str]):
    pass

create_daughter_sauce(MOTHER_SAUCES[0], ["Onions"]) # not super helpful
create_daughter_sauce(BÉCHAMEL, ["Onions"]) # Better
create_daughter_sauce("Hollandaise", ["Horsedradish"])
create_daughter_sauce("Veloute", ["Mustard"])
# Definitely wrong
create_daughter_sauce("Alabama White BBQ Sauce", [])
