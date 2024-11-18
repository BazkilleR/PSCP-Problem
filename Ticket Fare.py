"""Ticket Fare"""

def calculate_ticket_fare(n, a, b, c, d, e, f, g):
    """find price"""
    travel_distance = abs(g - f)
    total_fare = 0

    if f < 1 or f > n or g < 1 or g > n:
        return "Error"

    # level 1
    if travel_distance <= a:
        total_fare = b

    # level 2
    elif travel_distance <= a + c:
        total_fare = b + (d * (travel_distance - a))

    # level 3
    else:
        total_fare = b + (d * c)
        total_fare += e * (travel_distance - (a + c))

    return total_fare

inputs = (int(input()) for _ in range(8))
print(calculate_ticket_fare(*inputs))
