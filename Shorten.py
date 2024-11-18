'''shorten'''

def shorten_sequence():
    """Shortens a sequence of consecutive numbers."""
    current_num = int(input())
    result = str(current_num)
    first_in_sequence = current_num
    prev_num = current_num
    output_string = result

    while current_num != -1:
        current_num = int(input())

        if abs(prev_num - current_num) > 1:
            if current_num == -1:
                next_number = ""
            else:
                next_number = ", " + str(current_num)

            if prev_num == first_in_sequence:
                range_indicator = ""
            else:
                range_indicator = "-" + str(prev_num)

            output_string += range_indicator + next_number
            first_in_sequence = current_num

        prev_num = current_num

    print(output_string if output_string != "-1" else "")

shorten_sequence()
