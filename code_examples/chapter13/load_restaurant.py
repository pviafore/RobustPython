from typing import List, Protocol

class Restaurant(Protocol):
    name: str
    address: str
    standard_lunch_entries: List[str]
    other_entries: List[str]

    def render_menu(self) -> str:
        ...

def load_restaurant(restaurant: Restaurant):
    # code to load restaurant
    # ...
    pass

import restaurant
load_restaurant(restaurant)
