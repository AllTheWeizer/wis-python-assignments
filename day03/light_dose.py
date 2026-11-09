"""Calculate fiber-tip irradiance and light dose for optogenetics experiments."""

import csv
import math
from pathlib import Path


def calculate_light_dose(
    power_mw: float, diameter_um: float, duration_s: float
) -> tuple[float, float]:
    """Return average irradiance (mW/mm²) and light dose (mJ/mm²)."""
    if power_mw < 0:
        raise ValueError("Optical power cannot be negative.")
    if diameter_um <= 0:
        raise ValueError("Fiber core diameter must be greater than zero.")
    if duration_s < 0:
        raise ValueError("Stimulation duration cannot be negative.")

    radius_mm = diameter_um / 2000
    area_mm2 = math.pi * radius_mm**2
    irradiance_mw_mm2 = power_mw / area_mm2
    light_dose_mj_mm2 = irradiance_mw_mm2 * duration_s
    return irradiance_mw_mm2, light_dose_mj_mm2


def main() -> None:
    """Read the example experiments and print their irradiance and dose."""
    csv_path = Path(__file__).with_name("experiments.csv")
    with csv_path.open(newline="", encoding="utf-8") as experiments_file:
        experiments = csv.DictReader(experiments_file)
        print(
            f"{'Experiment':<32} {'Irradiance (mW/mm²)':>21} "
            f"{'Dose (mJ/mm²)':>17}"
        )
        print("-" * 73)
        for experiment in experiments:
            irradiance, dose = calculate_light_dose(
                float(experiment["power_mW"]),
                float(experiment["diameter_um"]),
                float(experiment["duration_s"]),
            )
            print(f"{experiment['name']:<32} {irradiance:>21.2f} {dose:>17.2f}")


if __name__ == "__main__":
    main()
