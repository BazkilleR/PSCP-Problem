"""Seeker"""

def main():
    """Seeker"""
    input_string = input()
    number_list = []
    current_number = ""
    total_sum = 0

    for char in input_string:
        if char.isnumeric():
            current_number += char
        if not char.isnumeric() or char == input_string[-1]:
            if current_number:
                number_list.append(current_number)
            current_number = ""

    for number in number_list:
        total_sum += int(number)

    print(total_sum)

main()
