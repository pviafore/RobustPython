from typing import NewType

def dispense_bun():
    return None


def dispense_ketchup():
    return None

def dispense_mustard():
    return None

class HotDog:
    def place_in_bun(self, bun):
        pass
    
    def add_condiments(self, *args):
        pass

def dispense_hotdog() -> HotDog:
    return HotDog()

PreparedHotDog = NewType("PreparedHotDog", HotDog)
def create_hot_dog() -> HotDog:
    bun = dispense_bun()
    hotdog = dispense_hotdog()
    hotdog.place_in_bun(bun)
    ketchup = dispense_ketchup()
    mustard = dispense_mustard()
    hotdog.add_condiments(ketchup, mustard)
    return PreparedHotDog(hotdog)


def place_on_plate(hotdog: PreparedHotDog):
    pass

place_on_plate(HotDog())
