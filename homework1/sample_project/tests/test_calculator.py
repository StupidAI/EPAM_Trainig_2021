import pytest
from sample_project.calculator.calc import check_power_of_2


@pytest.mark.parametrize(
    "data, result", [(65536, True), (12, False), (0, False), (-8, False)]
)
def test_calc(data, result):
    assert check_power_of_2(data) == result
