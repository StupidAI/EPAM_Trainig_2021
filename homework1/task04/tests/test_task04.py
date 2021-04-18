from task04.hw.task04 import check_sum_of_four


def test_zero():
    """
    Testing function with zero result:
    a = [1]
    b = [0]
    c = [0]
    d = [1]
    """
    a = [1]
    b = [0]
    c = [0]
    d = [1]
    result = check_sum_of_four(a, b, c, d)

    assert result == 0


def test_one():
    """
    Testing function on simple dataset:
    a = [1]
    b = [0]
    c = [0]
    d = [-1]
    """
    a = [1]
    b = [0]
    c = [0]
    d = [-1]
    result = check_sum_of_four(a, b, c, d)

    assert result == 1
