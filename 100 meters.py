"""100 meters"""

def who_win():
    """find 3 fastest"""
    best_time = float('inf')
    second_best_time = float('inf')
    third_best_time = float('inf')

    gold = 0
    silver = 0
    bronze = 0

    for runner in range(1, 9):
        time = float(input())

        if time < best_time:
            # Shift current best to second best and third best
            third_best_time = second_best_time
            bronze = silver

            second_best_time = best_time
            silver = gold

            best_time = time
            gold = runner

        elif time < second_best_time:
            # Shift current second best to third best
            third_best_time = second_best_time
            bronze = silver

            second_best_time = time
            silver = runner

        elif time < third_best_time:
            third_best_time = time
            bronze = runner

    print(gold, silver, bronze)

who_win()
