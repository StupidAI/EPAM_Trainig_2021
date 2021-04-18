import os

from task03.hw.task03 import find_maximum_and_minimum

os.chdir(r"./homework1/task03/tests")


def test_positive_for_sorted_dataset():
    """Testing function on sample example"""
    result = find_maximum_and_minimum("task03_dataset1.txt")
    assert result == (1, 5)


def test_positive_for_zero_dataset():
    """Testing function on dataset with zero values"""
    result = find_maximum_and_minimum("task03_dataset2.txt")
    assert result == (0, 0)
