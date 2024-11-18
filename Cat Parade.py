"""Cat Parade"""

def cat_parade():
    """cat parade"""
    cat_rankings = {}
    current_rank = 1

    while True:
        input_name = input()

        if input_name == "END":
            break

        if input_name == "IT'S A DOG":
            cat_rankings.popitem()
            current_rank -= 1
            continue

        cat_names = input_name.split(", ")

        for cat_name in cat_names:
            if cat_name in cat_rankings:
                cat_rankings[cat_name][1] += 1
            else:
                cat_rankings[cat_name] = [current_rank, 1]
            current_rank += 1

    for cat_name in sorted(cat_rankings.keys()):
        print(cat_name, cat_rankings[cat_name][0], cat_rankings[cat_name][1])

cat_parade()
