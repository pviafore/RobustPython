from enum import auto, Enum
class MenuSection(Enum):
    VEGAN_APPETIZERS = auto()
    NONVEGAN_APPETIZERS = auto()
    VEGAN_ENTREES = auto()
    NONVEGAN_ENTREES = auto()
    VEGAN_DESSERTS = auto()
    NONVEGAN_DESSERTS = auto()

assert repr(list(MenuSection)) == "[<MenuSection.VEGAN_APPETIZERS: 1>, <MenuSection.NONVEGAN_APPETIZERS: 2>, <MenuSection.VEGAN_ENTREES: 3>, <MenuSection.NONVEGAN_ENTREES: 4>, <MenuSection.VEGAN_DESSERTS: 5>, <MenuSection.NONVEGAN_DESSERTS: 6>]"
