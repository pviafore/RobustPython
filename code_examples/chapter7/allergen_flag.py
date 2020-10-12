from enum import auto, Flag

class Allergen(Flag):
    FISH = auto()
    SHELLFISH = auto()
    TREE_NUTS = auto()
    PEANUTS = auto()
    GLUTEN = auto()
    SOY = auto()
    DAIRY = auto()
    SEAFOOD = FISH | SHELLFISH
    ALL_NUTS = TREE_NUTS | PEANUTS

allergens = Allergen.FISH | Allergen.SHELLFISH

assert repr(allergens) == "<Allergen.SEAFOOD: 3>"
assert allergens & Allergen.FISH
