"""Heads and Legs"""

def aaaaa(amount, leg_count):
    """aaaa"""
    rabbit = 0
    eagle = 0

    if leg_count % 2 or (leg_count // 4) > amount:
        return "Impossible"
    
    eagle, leg_left = divmod(leg_count, 4)
    rabbit = leg_left // 2
    return f"{rabbit} {eagle}"

print(aaaaa(int(input()), int(input())))
