from typing import TypeVar,List
T = TypeVar('T')
def reverse(coll: list[T]) -> list[T]:
    return coll[::-1]

assert reverse([1,2,3]) == [3,2,1]
assert reverse(['a','b','c']) ==['c','b','a'] 
