from hw.task02 import check_fibonacci


def test_positive_from_zero_seq():
    """Testing that sequence is Fibonacci: from 0, 1, 1 value"""
    data_to_process = [
        0,
        1,
        1,
        2,
        3,
        5,
        8,
        13,
        21,
        34,
        55,
        89,
        144,
        233,
        377,
        610,
        987,
        1597,
        2584,
        4181,
        6765,
    ]
    assert check_fibonacci(data_to_process)


def test_positive_from_random_seq():
    """Testing that sequence is Fibonacci: from random value"""
    data_to_process = [89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
    assert check_fibonacci(data_to_process)


def test_negative_from_random_seq():
    """Testing that sequence is not Fibonacci: from random non Fibonacci value"""
    data_to_process = [4, 6, 10, 16]
    # data_to_process = [4181, 6765]
    # data_to_process = [6765]
    assert not check_fibonacci(data_to_process)


def test_negative_from_seq_of_two():
    """Testing that sequence is incorrect: len less than 3"""
    data_to_process = [4181, 6765]
    # data_to_process = [6765]
    assert not check_fibonacci(data_to_process)


def test_negative_from_seq_of_one():
    """Testing that sequence is incorrect: len less than 3"""
    data_to_process = [6765]
    assert not check_fibonacci(data_to_process)
