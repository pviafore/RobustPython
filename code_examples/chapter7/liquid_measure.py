from enum import Enum
class ImperialLiquidMeasure(Enum):
    CUP = 8
    PINT = 16
    QUART = 32
    GALLON = 128

assert ImperialLiquidMeasure.CUP != 8
