"PH"

def find_ph(num):
    """find ph"""
    if num < 0 or num > 14:
        print("error")
    elif num == 7:
        print("neutral")
    elif num < 7:
        print("acidic")
    else:
        print("akaline")

find_ph(float(input()))
