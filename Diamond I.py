"""Diamond I"""

def mining(m, n):
    """diamond I"""
    ore = []
    most_earn = []

    for _ in range(m):
        ore.append([int(x) for x in input().split()])

    for i in range(n):
        earn = 0

        for j in range(m):
            earn += ore[j][i]

        most_earn.append(earn)

    return max(most_earn)

print(mining(int(input()), int(input())))
