import pytest
from task03.hw.hw3 import combinations


@pytest.mark.parametrize(
    "data_to_process, result",
    [
        (([1, 2], [3, 4]), ([[1, 3], [1, 4], [2, 3], [2, 4]])),
        (([1], [1]), ([[1, 1]])),
    ],
)
def test_major_and_minor_elem_example(data_to_process, result):
    assert combinations(*data_to_process) == result
