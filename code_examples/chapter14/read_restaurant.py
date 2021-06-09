import yaml

with open('code_examples/chapter14/restaurant.yaml') as yaml_file:
    restaurant = yaml.safe_load(yaml_file)

assert restaurant == {
    "name": "Viafore's",
    "owner": "Pat Viafore",
    "address": "123 Fake St. Fakington, FA 01234",
    "employees": [{
        "name": "Pat Viafore",
        "position": "Chef",
        "payment_details": {
            "bank_details": {
                "routing_number": '123456789',
                "account_number": '123456789012'
            }
        }
    },
    {
        "name": "Made-up McGee",
        "position": "Server",
        "payment_details": {
            "bank_details": {
                "routing_number": '123456789',
                "account_number": '123456789012'
            }
        }
    },
    {
        "name": "Fabricated Frank",
        "position": "Sous Chef",
        "payment_details": {
            "bank_details": {
                "routing_number": '123456789',
                "account_number": '123456789012'
            }
        }
    },
    {
        "name": "Illusory Ilsa",
        "position": "Host",
        "payment_details": {
            "bank_details": {
                "routing_number": '123456789',
                "account_number": '123456789012'
            }
        }
    }],
    "dishes": [{
        "name": "Pasta And Sausage",
        "price_in_cents": 1295,
        "description": "Rigatoni and Sausage with a Tomato-Garlic-Basil Sauce"
    },
    {
        "name": "Pasta Bolognese",
        "price_in_cents": 1495,
        "description": "Spaghetti with a rich Tomato and Beef Sauce"
    },
    {
        "name": "Caprese Salad",
        "price_in_cents": 795,
        "description": "Tomato, Buffalo Mozzarella and Basil",
        "picture": "caprese.png"
    }],
    'number_of_seats': 12,
    "to_go": True,
    "delivery": False
}

from typing import Literal,TypedDict,Union
class AccountAndRoutingNumber(TypedDict):
    account_number: str
    routing_number: str

class BankDetails(TypedDict):
    bank_details: AccountAndRoutingNumber

class Address(TypedDict):
    address: str

AddressOrBankDetails = Union[Address, BankDetails]

Position = Literal['Chef', 'Sous Chef', 'Host',
                   'Server', 'Delivery Driver']

class Dish(TypedDict):
    name: str
    price_in_cents: int
    description: str

class DishWithOptionalPicture(Dish, TypedDict, total=False):
    picture: str

class Employee(TypedDict):
    name: str
    position: Position
    payment_details: AddressOrBankDetails

class Restaurant(TypedDict):
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
        return yaml.safe_load(yaml_file)

load_restaurant('code_examples/chapter14/restaurant.yaml')
