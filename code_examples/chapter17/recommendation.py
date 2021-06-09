
Meal = str
Ingredient = str

# dummy functions to get code to run
def get_proximity(meal, _ ):
    return len(meal)

def get_daily_specials():
    return ["abc", "d", "efghi", "jk", "l", "mno", "p"]

def recommend_meal(last_meal: Meal,
                   specials: list[Meal],
                   surplus: list[Ingredient]) -> list[Meal]:
    highest_proximity = 0
    for special in specials:
        if (proximity := get_proximity(special, surplus)) > highest_proximity:
            highest_proximity = proximity

    grouped_by_surplus_matching = []
    for special in specials:
        if get_proximity(special, surplus) == highest_proximity:
            grouped_by_surplus_matching.append(special)

    filtered_meals = []
    for meal in grouped_by_surplus_matching:
        if get_proximity(meal, last_meal) > .75:
            filtered_meals.append(meal)
    
    sorted_meals = sorted(filtered_meals,
                          key=lambda meal: get_proximity(meal, last_meal),
                          reverse=True)

    return sorted_meals[:3]

assert recommend_meal("def", get_daily_specials(), ["fgh"]) == ["efghi"]
