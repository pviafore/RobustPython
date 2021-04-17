from dataclasses import dataclass
from typing import List

@dataclass
class Cookbook:
    author: str

def create_author_count_mapping(cookbooks: list[Cookbook]):
    counter = {}
    for cookbook in cookbooks:
        if cookbook.author not in counter:
            counter[cookbook.author] = 0
        counter[cookbook.author] += 1
    return counter

def test_create_author_count():
    cookbooks = [Cookbook('Pat Viafore'), Cookbook('Pat Viafore'), Cookbook('J. Kenji Lopez-Alt')]
    assert create_author_count_mapping(cookbooks) == {
        'Pat Viafore': 2,
        'J. Kenji Lopez-Alt': 1
    }

test_create_author_count()
