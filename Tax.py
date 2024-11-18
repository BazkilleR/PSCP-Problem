"""Tax"""

def tax_cal(year, cc):
    """aaa"""
    total = 0
    discount = 0

    if cc <= 600:
        total += cc * 0.5
    elif cc <= 1800:
        total += 300 + ((cc - 600) * 1.5)
    else:
        total += 2100 + ((cc - 1800) * 4)

    if year == 6:
        discount = 0.1
    elif year == 7:
        discount = 0.2
    elif year == 8:
        discount = 0.3
    elif year == 9:
        discount = 0.4
    elif year >= 10:
        discount = 0.5

    result = total - (total * discount)
    print(f"{result:.2f}")

tax_cal(int(input()), int(input()))
