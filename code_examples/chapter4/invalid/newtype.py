from typing import NewType

class Bun:
    def add_frank(frank: str):
        pass

def dispense_bun() -> Bun:
    return Bun()


def dispense_ketchup():
    return None

def dispense_mustard():
    return None

class HotDog:
    
    def add_condiments(self, *args):
        pass

def dispense_hot_dog_to_customer(hot_dog: HotDog):
    pass

def dispense_frank() -> str:
    return "Frank"

def serve_to_customer(*args):
    pass

ReadyToServeHotDog = NewType("ReadyToServeHotDog", HotDog)
def create_hot_dog():
    bun = dispense_bun()
    frank = dispense_frank()
    hot_dog = bun.add_frank(frank)
    ketchup = dispense_ketchup()
    mustard = dispense_mustard()
    hot_dog.add_condiments(ketchup, mustard)
    dispense_hot_dog_to_customer(hot_dog)

def make_snack():
    serve_to_customer(ReadyToServeHotDog(HotDog()))

make_snack()
