'''Meteorite'''

def count_fire(weight, small, safe):
    '''count fire'''
    weight_now = weight
    amount_fire = 0

    count = 0
    while weight_now >= safe:
        weight_now /= small
        amount_fire += small**count
        count += 1
        # print('weight now :', weight_now)
        # print('amount fire :', amount_fire)
        # print('------')
    print(amount_fire)

count_fire(float(input()), int(input()), float(input()))