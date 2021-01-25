import itertools
from typing import Union,NewType

Preferences = str


class Family(str):
    pass

class Worker(str):
    pass

def within_radius(*args):
    return True

class Restaurant:

    def __init__(self, name):
        self.name = name

    def has_tables_available(self):
        return True

    def __eq__(self, rhs):
        return self.name == rhs.name

def get_all_restaurants() -> list[Restaurant]:
    return [Restaurant("rest1"), Restaurant("rest2")]

class FamilyRestModel:
    def __init__(self, weighted_values, restaurant):
        self.score = weighted_values

WorkerRestModel = FamilyRestModel

def by_tier_and_score_for_family(score_restaurant: tuple[int, Restaurant]):
    score, restaurant = score_restaurant
    return (restaurant.name, score)

def by_tier_for_family(score_restaurant: tuple[int, Restaurant]):
    score, restaurant = score_restaurant
    return restaurant.name

by_tier_and_score_for_worker = by_tier_and_score_for_family
by_tier_for_worker = by_tier_for_family


def strip_scores(restaurants) -> list[Restaurant]:
    return [r for s,r in restaurants]

ScoredRestaurant = tuple[int, Restaurant]
def rank_restaurants(searcher: Union[Family,Worker],
          preferences: Preferences) -> dict[str, list[Restaurant]]:

    restaurants = get_all_restaurants()
    scores = []
    for restaurant in restaurants: # <1>
        if within_radius(searcher, restaurant, preferences): # <2>
            if isinstance(searcher, Worker) or restaurant.has_tables_available(): # <3>
                if isinstance(searcher, Family):
                    weighted_values = 0
                    scores.append(FamilyRestModel(weighted_values,
                                                  restaurant).score) # <4>
                if isinstance(searcher, Worker):
                    weighted_values = 5
                    scores.append(WorkerRestModel(weighted_values,
                                                  restaurant).score) # <4>

    scored_restaurants = zip(scores, restaurants)
    if isinstance(searcher, Family):
        sorted_restaurants = sorted(scored_restaurants,
                                    key=by_tier_and_score_for_family) # <5>
        grouped = (itertools.groupby(sorted_restaurants,
                                     key=by_tier_for_family)) # <6>

        return {tier: strip_scores(grouped_restaurants) 
                for tier,grouped_restaurants in grouped}

    if isinstance(searcher, Worker):
        sorted_restaurants = sorted(scored_restaurants,
                                    key=by_tier_and_score_for_worker)
        grouped = (itertools.groupby(sorted_restaurants,
                                     key=by_tier_for_worker))
        
        return {tier: strip_scores(grouped_restaurants) 
                for tier,grouped_restaurants in grouped}

    raise ValueError("Invalid Searcher")

ranked_restaurants = rank_restaurants(Family("family"), "abc")
assert ranked_restaurants == {
    "rest1": [Restaurant("rest1")],
    "rest2": [Restaurant("rest2")]
}
