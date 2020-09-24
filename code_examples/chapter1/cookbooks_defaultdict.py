from collections import defaultdict
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class Cookbook:
    author: str

def create_author_count(cookbooks: List[Cookbook]):
    counter: Dict[str, int] = defaultdict(lambda: 0) 
    for cookbook in cookbooks:
        counter[cookbook.author] += 1
    return counter

def test_create_author_count():
    cookbooks = [Cookbook('Pat Viafore'), Cookbook('Pat Viafore'), Cookbook('J. Kenji Lopez-Alt')]
    assert create_author_count(cookbooks) == {
        'Pat Viafore': 2,
        'J. Kenji Lopez-Alt': 1
    }

test_create_author_count()
