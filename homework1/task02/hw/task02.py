"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence


# main body of program where fibonacci sequence is checking
def check_fibonacci(data: Sequence[int]) -> bool:
    n, n_next = 0, 1
    result = False
    if len(data) < 3:
        return False
    if data[0] != n and data[1] != n_next:
        while data[0] > n:
            n, n_next = n_next, n + n_next
    for d in data:
        if d != n:
            return False
        else:
            result = True
        n, n_next = n_next, n + n_next
    return result
