
ITALY_CITIES = ['Roma', 'Milano']
GERMAN_CITIES = ['Berlin', 'Frankfurt'] 
US_CITIES = ['Boston', 'Los Angeles']
# Our restaurant is named differently in different
# in different parts of the world
def get_restaurant_name(city: str) -> str:
    if city in ITALY_CITIES:
        return  "Trattoria Viafore"
    if city in GERMAN_CITIES:
        return "Pat's Kantine"
    if city in US_CITIES:
        return "Pat's Place"
    return None


if get_restaurant_name('Boston'):
    print("Location Found!")
