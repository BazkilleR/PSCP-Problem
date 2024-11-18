"""Counting Stars"""

def count_star(stars_group: str) -> None:
    """count all three star type"""
    constellation = 0
    comet = 0
    shooting_star = 0

    idx = 0
    while idx < len(stars_group) - 1:
        pair_stars = stars_group[idx] + stars_group[idx + 1]

        if pair_stars in ('~*', '*~'):
            comet += 1
            idx += 1
        elif pair_stars == "*/":
            shooting_star += 1
            idx += 1
        elif pair_stars == "**":
            constellation += 1
            idx += 1
        idx += 1

    if not constellation and not comet and not shooting_star:
        print("Tonight is a quiet night.")
        return

    print(f"constellation: {constellation}")
    print(f"comet: {comet}")
    print(f"shooting star: {shooting_star}")
    return

count_star(input())
