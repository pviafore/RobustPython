from enum import IntEnum
class ImperialLiquidMeasure(IntEnum):
    CUP = 8
    PINT = 16
    QUART = 32
    GALLON = 128

assert ImperialLiquidMeasure.CUP == 8
assert ImperialLiquidMeasure.CUP.value == 8

class Kitchenware(IntEnum):
    # Note to future programmers: these numbers are customer-defined 
     # and apt to change
     PLATE = 7
     CUP = 8
     UTENSILS = 9

def pour_into_larger_vessel():
    pass
def pour_into_smaller_vessel():
    pass

def pour_liquid(volume: ImperialLiquidMeasure):
    if volume == Kitchenware.CUP:
        pour_into_smaller_vessel()
    else:
        pour_into_larger_vessel()

pour_liquid(ImperialLiquidMeasure.CUP)
