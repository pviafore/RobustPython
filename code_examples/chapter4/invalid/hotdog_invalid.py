from typing import Optional

class HotDog:
    def add_condiments(self, *args):
        return None
class Bun:
    def add_frank(self, *args) -> HotDog:
        return HotDog()

def dispense_frank() -> str:
    return "frank"

def dispense_hot_dog():
    return HotDog()


def dispense_ketchup():
    return "Ketchup"

def dispense_mustard():
    return "Mustard"

def dispense_bun() -> Optional[Bun]:
    if False:
        return None
    return Bun()

def dispense_hot_dog_to_customer(hot_dog):
    pass

def create_hot_dog():
    bun = dispense_bun()
    if bun is None:
        print_error_code("Bun could not be dispensed")
        return

    frank = dispense_frank()
    hot_dog = bun.add_frank(frank)
    ketchup = dispense_ketchup()
    mustard = dispense_mustard()
    hot_dog.add_condiments(ketchup, mustard)
    dispense_hot_dog_to_customer(hot_dog)


create_hot_dog()
