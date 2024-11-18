'''MissingNumber No Set'''

def find_miss(num):
    """find missing number"""
    input_list = []
    missing_numbers = []

    while True:
        num_input = int(input())

        if not num_input:
            break

        input_list.append(num_input)

    for i in range(1, num + 1):
        if i not in input_list:
            missing_numbers.append(i)

    missing_numbers.sort()
    for i in missing_numbers:
        print(i)

find_miss(int(input()))
