a = 1
b = 2

def inc_a():
    global a
    a += 1

from typing import Callable
def do_twice(func: Callable, *args, **kwargs):
    func(*args, **kwargs)
    func(*args, **kwargs)

do_twice(inc_a)
assert a == 3

def repeat_twice(func: Callable) -> Callable:
    ''' this is a function that calls the wrapped function a specified number of times '''
    def _wrapper(*args, **kwargs):
            func(*args, **kwargs)
            func(*args, **kwargs)
    return _wrapper

@repeat_twice
def inc_b():
    global b
    b+= 1

inc_b()
assert b == 4
