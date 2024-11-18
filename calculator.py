'''Calculator'''

def count_touch(most_num):
    '''count tocuch'''
    if most_num == 1:
        count = 1
        return count

    count = 0
    for num in range(1, most_num + 1):
        count += len(str(num)) + 1
    return count

print(count_touch(int(input())))
