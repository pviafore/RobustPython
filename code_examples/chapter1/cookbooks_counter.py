from collections import Counter
from dataclasses import dataclass
from typing import List

@dataclass
class Cookbook:
    author: str

def create_author_count_mapping(cookbooks: list[Cookbook]):
    return Counter(book.author for book in cookbooks)

def test_create_author_count():
    cookbooks = [Cookbook('Pat Viafore'), Cookbook('Pat Viafore'), Cookbook('J. Kenji Lopez-Alt')]
    assert create_author_count_mapping(cookbooks) == {
        'Pat Viafore': 2,
        'J. Kenji Lopez-Alt': 1
    }

test_create_author_count()
