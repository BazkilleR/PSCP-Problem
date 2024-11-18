def assess_fever_level(temperature)
    """Assess and print the fever level based on body temperature in Celsius."""
    if temperature >= 40:
        print("Very High Fever")
    elif temperature >= 39:
        print("High Fever")
    elif temperature >= 38:
        print("Mild Fever")
    else:
        print("No Fever")

assess_fever_level(23)