import collections
import collections.abc

def print_items(items: collections.abc.Iterable):
    for item in items:
            print(item)

print_items('abc')
print_items([1,2,3,4])
print_items({5, 3, 4})
