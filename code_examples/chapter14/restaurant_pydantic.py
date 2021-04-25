import yaml
from pydantic import ValidationError
from pydantic.dataclasses import dataclass
from typing import Literal, List, Optional, TypedDict, Union

@dataclass
class AccountAndRoutingNumber():
    account_number: str
    routing_number: str

@dataclass
class BankDetails:
    bank_details: AccountAndRoutingNumber

@dataclass
class Address:
    address: str

AddressOrBankDetails = Union[Address, BankDetails]

Position = Literal['Chef', 'Sous Chef', 'Host',
                   'Server', 'Delivery Driver']

@dataclass
class Dish:
    name: str
    price_in_cents: int
    description: str
    picture: Optional[str] = None

@dataclass
class Employee:
    name: str
    position: Position
    payment_details: AddressOrBankDetails

@dataclass
class Restaurant:
    name: str
    owner: str
    address: str
    employees: list[Employee]
    dishes: list[Dish]
    number_of_seats: int
    to_go: bool
    delivery: bool


def load_restaurant(filename: str) -> Restaurant:
    with open(filename) as yaml_file:
        data = yaml.safe_load(yaml_file)
        return Restaurant(**data)

try:
    restaurant = load_restaurant("code_examples/chapter14/missing.yaml")
    assert False, "Should have failed"
except ValidationError:
    pass

try:
    restaurant = load_restaurant("code_examples/chapter14/wrong_type.yaml")
    assert False, "Should have failed"
except ValidationError:
    pass
