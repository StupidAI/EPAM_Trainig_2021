import pytest
from task02.hw.hw2 import major_and_minor_elem


@pytest.mark.parametrize(
    "data_to_process, result",
    [([3, 2, 3], (3, 2)), ([2, 2, 1, 1, 1, 2, 2], (2, 1))],
)
def test_major_and_minor_elem_example(data_to_process, result):
    assert major_and_minor_elem(data_to_process) == result
