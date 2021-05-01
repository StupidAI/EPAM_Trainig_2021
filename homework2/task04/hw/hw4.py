"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

"""
from typing import Callable


def cache(func: Callable) -> Callable:
    result_storage = {}

    def inside_func(a, b):
        if (a, b) in result_storage:
            return result_storage[(a, b)]
        result_storage[(a, b)] = func(a, b)
        return result_storage[(a, b)]

    return inside_func
