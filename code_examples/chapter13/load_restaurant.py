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

#mypy does not support modules as protocols yet
load_restaurant(restaurant) # type: ignore
