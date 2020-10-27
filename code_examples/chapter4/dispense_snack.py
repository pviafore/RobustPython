from typing import Union

class HotDog:
    pass
class Pretzel:
    pass

def dispense_hotdog() -> HotDog:
    return HotDog()

def dispense_pretzel() -> Pretzel:
    return Pretzel()

def dispense_snack(user_input: str) -> Union[HotDog, Pretzel, str]:
    if user_input == "Hotdog":
        return dispense_hotdog()
    elif user_input == "Pretzel":
        return dispense_pretzel()
    return "ERROR: Invalid User Input"

assert isinstance(dispense_snack("Hotdog"), HotDog)
assert isinstance(dispense_snack("Pretzel"), Pretzel)
assert dispense_snack("Whoops") == "ERROR: Invalid User Input" 
