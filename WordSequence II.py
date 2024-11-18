"""WordSequence II"""

def main():
    """WordSequence II"""
    first_input = input()
    second_input = input()
    length = 0
    len_first, len_second = len(first_input), len(second_input)

    for _ in range(max(len_first, len_second)):
        print(second_input[:length] + first_input[length:])
        length += 1

    print(second_input)

main()
