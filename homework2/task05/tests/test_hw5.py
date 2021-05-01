import string

import pytest

from homework2.task05.hw.hw5 import custom_range


@pytest.mark.parametrize(
    "data_to_process, result",
    [
        ((string.ascii_lowercase, "g"), (["a", "b", "c", "d", "e", "f"])),
        (
            (string.ascii_lowercase, "g", "p"),
            (["g", "h", "i", "j", "k", "l", "m", "n", "o"]),
        ),
        ((string.ascii_lowercase, "p", "g", -2), (["p", "n", "l", "j", "h"])),
    ],
)
def test_custom_range(data_to_process, result):
    assert custom_range(*data_to_process) == result
