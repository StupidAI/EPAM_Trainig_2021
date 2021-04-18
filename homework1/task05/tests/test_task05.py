import pytest

from task05.hw.task05 import find_maximal_subarray_sum


def test_for_sample_dataset():
    """
    Testing function on sample example
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    result == 16
    """
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    result = find_maximal_subarray_sum(nums, k)
    assert result == 16


def test_for_input_error():
    """
    Testing function with wrong input
    nums = [1, 3]
    k = 3
    result -> Exception: 'Input "k" is longer than given "nums" lenght'
    """
    with pytest.raises(Exception) as excinfo:
        nums = [1, 3]
        k = 3
        result = find_maximal_subarray_sum(nums, k)
    assert 'Input "k" is longer than given "nums" lenght' in str(excinfo.value)
