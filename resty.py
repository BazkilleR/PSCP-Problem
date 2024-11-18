'''Restaurant'''

def check_promotion(order, promotion, discount, pro_price):
    '''sdads'''
    result = ''
    sum_extra = order + pro_price

    if order >= promotion:
        order = order * (1 - discount / 100)

    second_price = sum_extra * (1 - discount / 100)

    if second_price < order:
        result = f'Yes {order - second_price:.3f}'
    elif second_price > order:
        result = f'No {second_price - order:.3f}'
    else:
        result = 'Yes'

    return result

a = float(input())
b = float(input())
c = float(input())
d = float(input())

print(check_promotion(a, b, c, d))
