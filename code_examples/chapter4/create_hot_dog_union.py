from typing import Optional, Union

class HotDog:
    pass

class Pretzel:
    pass

def dispense_hot_dog() -> HotDog:
    return HotDog()

def dispense_pretzel() -> Pretzel:
    return Pretzel()

from typing import Union
def dispense_snack(user_input: str) -> Union[HotDog, Pretzel]:
    if user_input == "Hot Dog":
        return dispense_hot_dog()
    elif user_input == "Pretzel":
        return dispense_pretzel()
    raise RuntimeError("Should never reach this code, as an invalid input has been")
