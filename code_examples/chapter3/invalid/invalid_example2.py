from typing import List
# takes a list and adds the doubled values
# to the end
# [1,2,3] => [1,2,3,2,4,6]
def add_doubled_values(my_list: list[int]):
    my_list.update([x*2 for x in my_list])

try:
    add_doubled_values([1,2,3])
    assert False, "Should have thrown an exception"
except AttributeError:
    pass
