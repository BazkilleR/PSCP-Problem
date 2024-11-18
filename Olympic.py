"""Olympic"""

def main():
    """Olympic"""
    competitors = [input().split() for _ in range(int(input()))]
    num_competitors = len(competitors)

    for competitor, index in zip(competitors, range(num_competitors)):
        competitors[index].append(int(competitor[1]) + int(competitor[2]) + int(competitor[3]))

    competitors.sort(key=lambda x: (-int(x[1]), -int(x[2]), -int(x[3]), x[0][:]))

    rank = 0
    previous_entry = [[]]
    consecutive_count = 0
    is_consecutive = 0

    for competitor, prev in zip(competitors, previous_entry):
        if competitor[1:] != prev[2:]:
            rank += 1
            if is_consecutive:
                rank += consecutive_count
                consecutive_count = 0
                is_consecutive = 0
        else:
            is_consecutive = 1
            consecutive_count += 1

        previous_entry.append([rank] + competitor)

    previous_entry.pop(0)

    for entry in previous_entry:
        print(entry[0], entry[1], entry[2], entry[3], entry[4], entry[5])

main()
