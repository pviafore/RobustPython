from collections import defaultdict
from dataclasses import dataclass

@dataclass
class Cookbook:
    author: str

AuthorToCountMapping = dict[str, int]
def create_author_count_mapping(cookbooks: list[Cookbook]) -> AuthorToCountMapping:
    counter: dict[str, int] = defaultdict(lambda: 0)
    for book in cookbooks:
        counter[book.author] += 1
    return counter

assert {'Pat Viafore': 2, 'J Kenji Alt-Lopez': 1} == create_author_count_mapping([Cookbook('Pat Viafore'), Cookbook('Pat Viafore'), Cookbook('J Kenji Alt-Lopez')])
