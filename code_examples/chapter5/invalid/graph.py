from collections import defaultdict
from typing import Generic, NewType, TypeVar, Union
from typing import Dict, List

Restaurant = NewType('Restaurant', str)
Recipe = NewType('Recipe', str)


T = TypeVar("T")
W = TypeVar("W")

class Graph(Generic[T, W]):
    def __init__(self):
        
        self.edges: Edges = defaultdict(list)

    def add_relation(self, node: T, to: W):
        self.edges[node].append(to)

    def get_relations(self, node: T) -> list[W]:
        return self.edges[node]

restaurants: Graph[Restaurant, Restaurant] = Graph()

restaurants.add_relation(Recipe('Cheeseburger'), Recipe('Hamburger'))

