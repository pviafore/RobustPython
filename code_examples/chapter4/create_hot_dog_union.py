from typing import Union
class HotDog:
    pass

def create_hot_dog() -> HotDog:
    return HotDog()

def are_ingredients_available():
    return True

def order_interrupted():
    return True

def dispense_hotdog() -> Union[HotDog, str]:
    if not are_ingredients_available():
        return "Not all ingredients available"
    if order_interrupted():
        return "Order interrupted"
    return create_hot_dog()

assert dispense_hotdog() == "Order interrupted"
