# Day 03 — Optogenetics Light Dose Calculator

## What it does

`light_dose.py` calculates average irradiance at the face of a circular fiber
and the total light dose for each experiment listed in `experiments.csv`. It
prints a table of results in **mW/mm²** and **mJ/mm²**.

The fiber area is calculated as π × (diameter / 2)² after converting the
diameter from micrometers to millimeters. Irradiance is optical power divided
by fiber area; light dose is irradiance multiplied by stimulation duration.
Because 1 mW × 1 second equals 1 mJ, dose is reported in mJ/mm².

These are average values at the fiber face. They do not model light scattering
or absorption in tissue or account for a nonuniform beam.

## How to run

From the repository root, run:

```bash
python day03/light_dose.py
```

On Windows, if `python` is not on your PATH, use the Python launcher:

```powershell
py -3 day03/light_dose.py
```

The script loads the CSV file next to itself. To run the tests, install pytest
if needed, then run:

```bash
python -m pytest day03/test_light_dose.py
```

On Windows, the corresponding command is:

```powershell
py -3 -m pytest day03/test_light_dose.py
```

## Prompts

In my repo, create a folder called day03 with:
1. light_dose.py: a function that takes optical power (mW), fiber core diameter (µm), and stimulation duration (s), and returns irradiance (mW/mm²) and light dose (mJ/mm²). The script should read experiments from a CSV file, run the function on each row, and print a results table.
2. experiments.csv: 8 realistic example optogenetics experiments with columns name, power_mW, diameter_um, duration_s.
3. test_light_dose.py: a few pytest tests for the function.
4. README.md: explain what the program does, how to run it, and include this exact prompt under a "Prompts" heading.
