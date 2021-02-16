from pydantic.dataclasses import dataclass
from pydantic import constr, PositiveInt, ValidationError
from typing import List, Literal, Optional, Union
@dataclass
class AccountAndRoutingNumber:
    account_number: constr(min_length=9,max_length=9)
    routing_number: constr(min_length=8,max_length=12)


@dataclass
class BankDetails:
    bank_details: AccountAndRoutingNumber


@dataclass
class Address:
    address: constr(min_length=1)

AddressOrBankDetails = Union[Address, BankDetails]

Position = Literal['Chef', 'Sous Chef', 'Host',
                   'Server', 'Delivery Driver']
@dataclass
class Employee:
    name: str
    position: Position

@dataclass
class Dish:
    name: constr(min_length=1, max_length=16)
    price_in_cents: PositiveInt
    description: constr(min_length=1, max_length=80)
    picture: Optional[str] = None


@dataclass
class Dish:
    name: constr(min_length=1, max_length=16)

from pydantic import conlist,constr
from pydantic import validator
@dataclass
class Restaurant:
    name: constr(regex=r'^[a-zA-Z0-9 ]*$',
                   min_length=1, max_length=16)
    owner: constr(min_length=1)
    address: constr(min_length=1)
    employees: conlist(Employee, min_items=2)
    dishes: conlist(Dish, min_items=3)
    number_of_seats: PositiveInt
    to_go: bool
    delivery: bool

    @validator('employees')
    def check_chef_and_server(cls, employees):
        if (any(e for e in employees if e.position == 'Chef') and 
            any(e for e in employees if e.position == 'Server')):
                return employees
        raise ValueError('Must have at least one chef and one server')
try:
    restaurant = Restaurant(**{
        'name': 'Dine n Dash',
        'owner': 'Pat Viafore',
        'address': '123 Fake St.',
        'employees': [Employee('Pat', 'Chef'), Employee('Joe', 'Chef')],
        'dishes': [Dish('abc'), Dish('def'), Dish('ghi')],
        'number_of_seats': 5,
        'to_go': False,
        'delivery': True
    })
    assert False, "Should not have been able to construct Restaurant"
except ValidationError:
    pass
