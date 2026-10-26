# Day 02 — Optogenetic Fiber Irradiance Calculator

## Purpose

This Python program calculates the **average optical irradiance at the tip of a circular optical fiber**. It is a simple example of a scientific calculation used in neuroscience and optogenetics.

The program asks the user to enter:

- Light power at the fiber tip, in **milliwatts (mW)**
- Fiber core diameter, in **micrometers (µm)**

It then prints the fiber's cross-sectional area and the average irradiance in **mW/mm²**.

## Calculation

The fiber is treated as a circle:

- Diameter in mm = diameter in µm / 1000
- Radius in mm = diameter in mm / 2
- Area in mm² = π × radius²
- Average irradiance in mW/mm² = power in mW / area in mm²

The script uses Python's built-in `math.pi` constant.

## How to run

1. Install Python 3 if necessary.
2. Open a terminal in the folder containing `irradiance.py`.
3. Run:

   ```bash
   python irradiance.py
   ```

   On some systems, use `python3 irradiance.py` instead.
4. Enter the requested values.

## Example

For **1 mW** delivered through a **200 µm** fiber:

```text
Optogenetic Fiber Irradiance Calculator
Light power at fiber tip (mW): 1
Fiber core diameter (micrometers): 200
Fiber area: 0.03142 mm^2
Average tip irradiance: 31.83 mW/mm^2
Note: This is at the fiber tip, not at neurons in tissue.
```

## Input checks and limitations

- The fiber diameter must be greater than zero.
- The optical power cannot be negative. Zero power gives zero irradiance.
- Inputs must be numbers; entering text instead of a number causes a Python error in this beginner version.
- The result assumes power is uniformly distributed across the fiber core. Real beams may have nonuniform intensity profiles.
- **This is the average irradiance at the fiber face.** It does not calculate the irradiance inside brain tissue, where absorption, scattering, fiber numerical aperture, and distance affect light delivery.

## AI assistance disclosure

OpenAI ChatGPT was used to help prepare the Python example and this README. The requests included **“provide .py file”** and **“+readme”**, following a discussion about using an optogenetic irradiance calculator for the course's second assignment. The code and explanation should be reviewed, run, and understood before submission.
