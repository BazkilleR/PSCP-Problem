'''Milk'''

def cal_get(a, b, c, d):
    '''calculate'''
    bought = d // a
    num = bought

    if b > 0 and c:
        while num >= b:
            num = num - b + c
            bought += c

    return bought

price = int(input())
promo_condition = int(input())
promo_get = int(input())
have_money = int(input())

print(cal_get(price, promo_condition, promo_get, have_money))
