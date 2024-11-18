'''Coke'''

def best_buy(price, promotion, new_price, want):
    '''find best buy'''
    get = 0
    paid = 0

    while get < want:
        if promotion and get and not get % promotion:
            paid += new_price
        else:
            paid += price
        get += 1

    return paid

print(best_buy(int(input()), int(input()), int(input()), int(input())))
