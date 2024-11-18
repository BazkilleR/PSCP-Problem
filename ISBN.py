"""ISBN"""

def cal(text):
    """Check if the given ISBN-10 number is valid."""
    # Remove hyphens and create a list of characters
    num_list = [char for char in text if char != "-"]

    result = 0
    i = 10

    # Calculate the weighted sum for the first 9 digits
    for num in num_list[:-1]:
        result += i * int(num)
        i -= 1

    # Special case for the last character
    last_digit = 10 if num_list[-1] == "X" else int(num_list[-1])

    # Calculate the checksum
    result = (result * -1) % 11

    # Validate the checksum
    if result == last_digit:
        print("Yes")
    else:
        print("No", "X" if result == 10 else result)

cal(input())
