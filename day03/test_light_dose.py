import math

import pytest

from light_dose import calculate_light_dose


def test_calculates_irradiance_and_dose():
    irradiance, dose = calculate_light_dose(1, 200, 2)

    assert math.isclose(irradiance, 1 / (math.pi * 0.1**2))
    assert math.isclose(dose, irradiance * 2)


def test_zero_power_gives_zero_irradiance_and_dose():
    assert calculate_light_dose(0, 200, 5) == (0, 0)


@pytest.mark.parametrize(
    ("power_mw", "diameter_um", "duration_s"),
    [
        (-1, 200, 1),
        (1, 0, 1),
        (1, -200, 1),
        (1, 200, -1),
    ],
)
def test_rejects_invalid_measurements(power_mw, diameter_um, duration_s):
    with pytest.raises(ValueError):
        calculate_light_dose(power_mw, diameter_um, duration_s)
