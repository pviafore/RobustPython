def dispense_bun():
    return Bun()

class HotDog:
    
    def add_condiments(self, *args):
        pass

class Bun:
    def add_frank(self, frank: str) -> HotDog:
        return HotDog()

def dispense_ketchup():
    return None

def dispense_mustard():
    return None

def dispense_frank() -> str:
    return "frank"

def dispense_hot_dog_to_customer(hot_dog: HotDog):
    pass

def create_hot_dog():
    bun = dispense_bun()
    frank = dispense_frank()
    hot_dog = bun.add_frank(frank)
    ketchup = dispense_ketchup()
    mustard = dispense_mustard()
    hot_dog.add_condiments(ketchup, mustard)
    dispense_hot_dog_to_customer(hot_dog)
