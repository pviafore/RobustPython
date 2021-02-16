from dataclasses import dataclass
from enum import Enum

import rx

class Direction(Enum):
    NORTH = "NORTH"
    WEST = "WEST"
    SOUTH = "SOUTH"
    EAST = "EAST"

@dataclass
class LocationData:
    x: int
    y: int
    z: int

@dataclass
class BatteryLevel:
    percent: int

@dataclass
class WindData:
    speed: int
    direction: Direction

@dataclass
class CurrentWeight:
    grams: int

def is_close_to_restaurant(*args):
    return False

observable = rx.of(
    LocationData(x=3, y=12, z=40),
    BatteryLevel(percent=95),
    BatteryLevel(percent=94),
    WindData(speed=15, direction=Direction.NORTH),
    LocationData(x=3, y=12, z=35),
    LocationData(x=4, y=12, z=32),
    # ... snip 100s of events
    BatteryLevel(percent=72),
    CurrentWeight(grams=300),
    CurrentWeight(grams=100)
)

val = None
def save_value(x):
    global val
    val = x
    
def save_average_weight(data):
    save_value(data)

def save_max_altitude(data):
    save_value(data)

import rx.operators

get_average_weight = observable.pipe(
    rx.operators.filter(lambda data: isinstance(data, CurrentWeight)),
    rx.operators.map(lambda cw: cw.grams),
    rx.operators.average()
)

get_average_weight.subscribe(save_average_weight)

assert val == 200

get_max_altitude = observable.pipe(
    rx.operators.skip_while(is_close_to_restaurant),
    rx.operators.filter(lambda data: isinstance(data, LocationData)),
    rx.operators.map(lambda loc: loc.z),
    rx.operators.max()
)

get_max_altitude.subscribe(save_max_altitude)

assert val == 40
