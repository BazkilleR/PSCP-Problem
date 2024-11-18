"""MissingNumber"""

def find_miss(num):
    """find miss"""
    full_num = set(range(1, num + 1))
    input_set = set()

    while True:
        num = int(input())

        if not num:
            break

        input_set.add(num)

    missing_num = sorted(list(full_num - input_set))

    for i in missing_num:
        print(i)

find_miss(int(input()))
