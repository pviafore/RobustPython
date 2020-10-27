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

def create_hot_dog():
    bun = dispense_bun()
    hotdog = dispense_hotdog()
    hotdog.place_in_bun(bun)
    ketchup = dispense_ketchup()
    mustard = dispense_mustard()
    hotdog.add_condiments(ketchup, mustard)
    return hotdog

assert isinstance(create_hot_dog(), HotDog)
