'''Kaprekar'''

def jud_num(num, reverse=False):
    '''jud lek kub isus'''
    num_list = list(map(int, list(str(num))))
    n = len(num_list)

    for i in range(n):
        for j in range(i+1, n):
            if not reverse:
                if num_list[i] < num_list[j]:
                    num_list[i], num_list[j] = num_list[j], num_list[i]
            else:
                if num_list[i] > num_list[j]:
                    num_list[i], num_list[j] = num_list[j], num_list[i]

    result = "".join(map(str, num_list))
    return int(result)

def cal_til_dead(num):
    '''calculate'''
    count = 0
    while num != 6174:
        most_num = jud_num(num)
        miin_num = jud_num(num, reverse=True)
        num = most_num - miin_num
 
        if num < 1000:
            num *= 10

        count += 1

    return count

print(cal_til_dead(input()))
