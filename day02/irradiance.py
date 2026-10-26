"""Calculate average optical irradiance at the face of a circular fiber.

This is an introductory Python assignment example. It does not model
light scattering or absorption inside brain tissue.
"""

import math

print("Optogenetic Fiber Irradiance Calculator")

# Ask the user for the light power and fiber diameter.
power_mw = float(input("Light power at fiber tip (mW): "))
diameter_um = float(input("Fiber core diameter (micrometers): "))

# The diameter must be positive, and optical power cannot be negative.
if diameter_um <= 0 or power_mw < 0:
    print("Error: diameter must be greater than 0 and power cannot be negative.")
else:
    # Convert micrometers to millimeters and calculate the circle's area.
    diameter_mm = diameter_um / 1000
    radius_mm = diameter_mm / 2
    area_mm2 = math.pi * radius_mm**2

    # Average irradiance = optical power / illuminated area.
    irradiance_mw_mm2 = power_mw / area_mm2

    print(f"Fiber area: {area_mm2:.5f} mm^2")
    print(f"Average tip irradiance: {irradiance_mw_mm2:.2f} mW/mm^2")
    print("Note: This is at the fiber tip, not at neurons in tissue.")
