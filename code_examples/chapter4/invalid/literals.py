from dataclasses import dataclass
from typing import Literal,Set

@dataclass 
class Error:
    error_code: Literal[1,2,3,4,5]
    disposed_of: bool

@dataclass
class Snack:
    name: Literal["Pretzel", "Hotdog"]
    condiments: Set[Literal["Mustard", "Ketchup"]]

Error(0, False)
Snack("Not Valid", set())
Snack("Pretzel", {"Mustard", "Relish"})
