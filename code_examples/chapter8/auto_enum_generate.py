from enum import auto, Enum
class MotherSauce(Enum):

    def _generate_next_value_(name: str, start, count, last_values): # type: ignore
        return name.capitalize()

    BÉCHAMEL = auto()
    VELOUTÉ = auto()
    ESPAGNOLE = auto()
    TOMATO = auto()
    HOLLANDAISE = auto()

assert repr(list(MotherSauce)) =="[<MotherSauce.BÉCHAMEL: 'Béchamel'>, <MotherSauce.VELOUTÉ: 'Velouté'>, <MotherSauce.ESPAGNOLE: 'Espagnole'>, <MotherSauce.TOMATO: 'Tomato'>, <MotherSauce.HOLLANDAISE: 'Hollandaise'>]"
