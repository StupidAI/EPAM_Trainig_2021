"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
import sys
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    if len(nums) < k:
        raise Exception('Input "k" is longer than given "nums" lenght')
    max = -sys.maxsize - 1
    steps = len(nums) - k + 1
    for i in range(steps):
        sliced_num = nums[i : i + k]
        cur_sum = sum(sliced_num)
        if max < cur_sum:
            max = cur_sum
    return max
