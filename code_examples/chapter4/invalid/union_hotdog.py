from typing import Optional, Union
def get_order():
    order = object()
    order.name = "Bun"

class HotDog:
    pass

class Pretzel:
    pass

def dispense_snack(name: str) -> Union[HotDog, Pretzel, str]:
    return "abc"

def place_order() -> Optional[HotDog]:
    order = get_order()
    result = dispense_snack(order.name)
    if isinstance(result, str):
        print("An error occurred" + result)
        return None
    # Return our HotDog
    return result
