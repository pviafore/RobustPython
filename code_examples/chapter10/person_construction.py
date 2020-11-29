from dataclasses import dataclass

class Person:
    name: str = ""
    years_experience: int = 0
    address: str = ""

pat = Person()
pat.name = "Pat"

try:
    pat = Person("Pat", 13, "123 Fake St.") # type: ignore
    assert False
except TypeError:
    pass

assert pat.name == "Pat"

pat_dict = {
    "name": "",
    "years_experience": 0,
    "address": ""
}

@dataclass
class PersonDataclass():
    name: str = ""
    years_experience: int = 0
    address: str = ""


class Person: # type: ignore
    def __init__(self,
                  name: str,
                  years_experience: int,
                  address: str):
        self.name = name
        self.years_experience = years_experience
        self.address = address

pat = Person("Pat", 13, "123 Fake St.") # type: ignore
