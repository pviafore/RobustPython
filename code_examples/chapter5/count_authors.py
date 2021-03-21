from collections import defaultdict
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class Cookbook:
    author: str

AuthorToCountMapping = dict[str, int]
def count_authors(cookbooks: list[Cookbook]) -> AuthorToCountMapping:
    counter: dict[str, int] = defaultdict(lambda: 0)
    for book in cookbooks:
        counter[book.author] += 1
    return counter

assert {'Pat Viafore': 2, 'J Kenji Alt-Lopez': 1} == count_authors([Cookbook('Pat Viafore'), Cookbook('Pat Viafore'), Cookbook('J Kenji Alt-Lopez')])
