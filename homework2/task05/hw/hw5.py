"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""

import string
from typing import Any, Iterable, List


def custom_range(inp: Iterable, *args: Any) -> List[Any]:
    result = []
    if not args:
        return [i for i in inp]
    if len(args) == 1:
        for item in inp:
            if item != args[0]:
                result += item
            else:
                return result
    if len(args) == 2:
        first_inp = True
        for item in inp:
            if first_inp:
                if item == args[0]:
                    first_inp = False
                else:
                    continue
            if item != args[1]:
                result += item
            else:
                return result
    if (
        len(args) == 3
    ):  # плохая реализация на мой взгляд - потому что создается еще один одъект в пямяти
        inp = list(inp)
        start = inp.index(args[0])
        end = inp.index(args[1])
        result = inp[start : end : args[2]]
        return result


print(custom_range(string.ascii_lowercase, "g", "p"))
