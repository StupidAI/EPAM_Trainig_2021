"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    result = 0
    map_of_sums = {}
    for i in a:
        for j in b:
            if (i + j) not in map_of_sums:
                map_of_sums[i + j] = 1
            else:
                map_of_sums[i + j] = +1
    for k in c:
        for l in d:
            if -(k + l) in map_of_sums:
                result += map_of_sums[-(k + l)]
    return result
