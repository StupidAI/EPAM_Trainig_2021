import os

import pytest
from task03.hw.task03 import find_maximum_and_minimum

os.chdir(r"./homework1/task03/tests")


@pytest.mark.parametrize(
    "data, result",
    [
        ("task03_dataset1.txt", (1, 5)),
        ("task03_dataset2.txt", (0, 0)),
    ],
)
def test_positive_for_sorted_dataset(data, result):
    assert find_maximum_and_minimum(data) == result
