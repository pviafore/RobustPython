from typing import List


class Coordinates:
    pass

class Employee:
    pass

class Ingredient:
    pass

class Menu:
    def contains(self, ingredient: Ingredient) -> bool:
        return True

class Finances:
    pass

class Dish:
    pass

class RestaurantData:
    pass

class Restaurant:
    def __init__(self,
                 name: str,
                 location: Coordinates,
                 employees: list[Employee],
                 inventory: list[Ingredient],
                 menu:  Menu,
                 finances: Finances):
        self.name = name
        self.location = location,
        self.employees = employees
        self.inventory = inventory
        self.menu = menu
        self.finances = finances


    def transfer_employees(self,
                           employees: list[Employee],
                           restaurant: 'Restaurant'):
        pass

    def order_dish(self, dish: Dish):
        pass

    def add_inventory(self, ingredients: list[Ingredient], cost_in_cents: int):
        pass

    def register_hours_employee_worked(self, 
                                       employee: Employee,
                                       minutes_worked: int):
        pass

    def get_restaurant_data(self) -> RestaurantData:
        return RestaurantData()

    def change_menu(self, menu: Menu):
        self.__menu = menu

    def move_location(self, new_location: Coordinates):
        pass

class GPS:
    def get_coordinates(self) -> Coordinates:
        return Coordinates()

def initialize_gps():
    return GPS()

def schedule_auto_driving_task(location: Coordinates):
    pass

class FoodTruck(Restaurant):
    def __init__(self, 
                 name: str,
                 location: Coordinates,
                 employees: list[Employee],
                 inventory: list[Ingredient],
                 menu:  Menu,
                 finances: Finances):
        super().__init__( name, location, employees,inventory, menu, finances)
        self.__gps = initialize_gps()
    
    def move_location(self, new_location: Coordinates):
        # schedule a task to drive us to our new location
        schedule_auto_driving_task(new_location)    
        super().move_location(new_location)

    def get_current_location(self) -> Coordinates:
        return self.__gps.get_coordinates()

class PopUpStall(Restaurant):
    pass

# this should all type check just fine
food_truck = FoodTruck("Pat's Food Truck", Coordinates(), [], [], Menu(), Finances())
food_truck.order_dish(Dish())
food_truck.move_location(Coordinates())

def display_restaurant_data(restaurant: Restaurant):
    data = restaurant.get_restaurant_data()
    # ... snip drawing code here ...

restaurants: list[Restaurant] = [food_truck]
for restaurant in restaurants:
    display_restaurant_data(restaurant)


class RestrictedMenuRestaurant(Restaurant):

    def __init__(self,
                 name: str,
                 location: Coordinates,
                 employees: list[Employee],
                 inventory: list[Ingredient],
                 menu: Menu,
                 finances: Finances,
                 restricted_items: list[Ingredient]):
        super().__init__(name,location,employees,inventory,menu,finances)
        self.__restricted_items = restricted_items

    def change_menu(self, menu: Menu):
        if any(not menu.contains(ingredient) for ingredient in self.__restricted_items):
            # new menus MUST contain restricted ingredients
            return super().change_menu(menu)

RestrictedMenuRestaurant("Name", Coordinates(), [], [], Menu(), Finances(), []).change_menu(Menu())
