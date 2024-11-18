'''Coffee Shop'''

def cal_best_price(a, b, c, d, e):
    '''calculate'''
    price1 = a + ((e - 1) * (a * (1 - (b/100))))

    if (a * e) >= d:
        price2 = (a * e) * (1 - (c/100))
    else:
        price2 = a * e

    if price1 < price2:
        print('1')
        print(f'{price1:.2f}')
    elif price1 > price2:
        print('2')
        print(f'{price2:.2f}')
    else:
        print('2')
        print(f'{price2:.2f}')

cal_best_price(float(input()), float(input()), float(input()), float(input()), int(input()))
