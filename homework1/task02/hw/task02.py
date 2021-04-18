"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence


# Fibonacci generator class. Return next Fibonacci number. First and second are given as n, n_next = 0, 1
class FiboSeq:
    def __init__(self):
        self.n, self.n_next = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.n, self.n_next = self.n_next, self.n + self.n_next
        return self.n_next


# main body of program where fibonacci sequence is checking
def check_fibonacci(data: Sequence[int]) -> bool:
    data_len = len(data)
    result = False
    my_fibo = FiboSeq()
    if data_len >= 3:
        if data[0] == my_fibo.n and data[1] == my_fibo.n_next:
            for d in data[2:]:
                if d != next(my_fibo):
                    return False
                else:
                    result = True
        else:
            while data[0] > my_fibo.n_next:
                next(my_fibo)
            if data[0] == my_fibo.n_next:
                for d in data[1:]:
                    if d != next(my_fibo):
                        return False
                    else:
                        result = True
    else:
        return False
    return result
