def dispense_bun():
    return None

def dispense_hotdog():
    return HotDog

def dispense_ketchup():
    return None

def dispense_mustard():
    return None

class HotDog:
    def dispense_in_bun(self, bun):
        pass
    
    def add_condiments(self, *args):
        pass

def print_error_code(text):
    print(text)

def create_hot_dog():
    bun = dispense_bun()
    if bun is None:
        print_error_code("Bun unavailable. Check for bun")
        return None
    hotdog = dispense_hotdog()
    if hotdog is None:
        print_error_code("Hotdog unavailable. Check for hotdog")
        return None
    hotdog.place_in_bun(bun)


    ketchup = dispense_ketchup()
    mustard = dispense_mustard()
    if ketchup is None or mustard is None:
        print_error_code("Check for invalid catsup")
        return None
    hotdog.add_condiments(ketchup, mustard)
    return hotdog

assert create_hot_dog() is None
