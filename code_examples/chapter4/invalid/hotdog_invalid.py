from typing import Optional
class Bun:
    def place_hotdog(self, *args):
        return None

def dispense_hotdog():
    return HotDog()

class HotDog:
    def add_condiments(self, *args):
        return None

def dispense_ketchup():
    return "Ketchup"

def dispense_mustard():
    return "Mustard"

def dispense_bun() -> Optional[Bun]:
    if False:
        return None
    return Bun()

def create_hot_dog() -> None:
    bun = dispense_bun()
    hotdog = dispense_hotdog()
    bun.place_hotdog()
    ketchup = dispense_ketchup()
    mustard = dispense_mustard()
    hotdog.add_condiments(ketchup, mustard)


create_hot_dog()
