"""safe"""

def main():
    """Safe"""
    first_input = input()
    second_input = input()
    first_positions = [ord(char) - ord("A") + 1 for char in first_input]
    second_positions = [ord(char) - ord("A") + 1 for char in second_input]
    total_distance = 0

    for pos1, pos2 in zip(first_positions, second_positions):
        distance = abs(pos1 - pos2)
        if distance > 13:
            adjusted_distance = min(pos1, pos2) + 26
            distance = abs(adjusted_distance - max(pos1, pos2))
        total_distance += distance

    print(total_distance)

main()
