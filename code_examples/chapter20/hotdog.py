from typing import NewType

class HotDog:
    pass

PreparedHotDog = NewType("PreparedHotDog", HotDog)

def create_hot_dog() -> PreparedHotDog:
    hotdog = HotDog()
    return PreparedHotDog(hotdog)

def create(): 
    hot_dog=PreparedHotDog(HotDog())
