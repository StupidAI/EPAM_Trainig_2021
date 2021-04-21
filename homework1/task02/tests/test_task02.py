import pytest
from task02.hw.task02 import check_fibonacci


@pytest.mark.parametrize(
    "data_to_process, result",
    [
        ([0, 1, 1, 2, 3, 5, 8], True),
        ([89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765], True),
        ([4, 6, 10, 16], False),
        ([4181, 6765], False),
    ],
)
def test_fonacci_sequense(data_to_process, result):
    assert check_fibonacci(data_to_process) == result
