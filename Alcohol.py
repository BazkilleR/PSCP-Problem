"""Alcohol"""

def can_drive():
    """can drive?"""
    gender = input() # Male or Female
    weight = float(input())
    driver_license = input() # Yes or No
    drink_volume = float(input())
    alcohol_percent = float(input())
    num_drinks = int(input())
    rest_hours = int(input())

    if driver_license == "No":
        return "Not Safe"

    water_constant = 0.68 if gender == "Male" else 0.55

    total_alcohol_grams = ((alcohol_percent * drink_volume) / 100) * num_drinks
    bac = (total_alcohol_grams) / (weight * water_constant * 10)

    bac_after_rest = bac - (0.015 * rest_hours)
    bac_after_rest = max(0, bac_after_rest)

    if bac_after_rest > 0.05:
        return "Not Safe"
    return "Safe"

print(can_drive())
