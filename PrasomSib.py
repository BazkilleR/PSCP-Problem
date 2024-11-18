"""PrasomSib"""

def prasomsib(text):
    """dasda"""
    # num_list = []
    result = 0

    for focus in range(len(text[1:])):
        sequence = text[focus]
        for num in text[focus+1:]:
            sequence += num
            sum_num = sum(list(map(int, (list(sequence)))))

            if sum_num == 10:
                result += 1
                break
            if sum_num > 10:
                break

    # print(num_list)
    return result

print(prasomsib(input()))
