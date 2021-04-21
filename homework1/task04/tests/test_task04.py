import pytest
from task04.hw.task04 import check_sum_of_four


@pytest.mark.parametrize(
    "a, b, c, d, result",
    [
        ([1], [0], [0], [1], 0),
        ([1], [0], [0], [-1], 1),
    ],
)
def test_zero(a, b, c, d, result):
    assert check_sum_of_four(a, b, c, d) == result
