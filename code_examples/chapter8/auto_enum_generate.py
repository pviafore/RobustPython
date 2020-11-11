from enum import auto, Enum
class MenuSection(Enum):

    def _generate_next_value_(name, start, count, last_values):
        return name.capitalize()

    VEGAN_APPETIZERS = auto()
    NONVEGAN_APPETIZERS = auto()
    VEGAN_ENTREES = auto()
    NONVEGAN_ENTREES = auto()
    VEGAN_DESSERTS = auto()
    NONVEGAN_DESSERTS = auto()

assert repr(list(MenuSection)) == "[<MenuSection.VEGAN_APPETIZERS: 'Vegan_appetizers'>, <MenuSection.NONVEGAN_APPETIZERS: 'Nonvegan_appetizers'>, <MenuSection.VEGAN_ENTREES: 'Vegan_entrees'>, <MenuSection.NONVEGAN_ENTREES: 'Nonvegan_entrees'>, <MenuSection.VEGAN_DESSERTS: 'Vegan_desserts'>, <MenuSection.NONVEGAN_DESSERTS: 'Nonvegan_desserts'>]"
