'''post office'''

def cal_envelop(amount: int) -> int:
    '''calculate price for envelopes'''
    total = 13 * amount

    for _ in range(amount):
        weight = float(input())

        if weight <= 10:
            total += 16
        elif weight <= 20:
            total += 18
        elif weight <= 100:
            total += 23
        elif weight <= 250:
            total += 28
        elif weight <= 500:
            total += 33
        elif weight <= 1000:
            total += 48
        elif weight <= 2000:
            total += 68

    return total

def cal_package(amount: int) -> int:
    '''calculate price for packages'''
    total = 15 * amount

    for _ in range(amount):
        weight = float(input())

        if weight <= 500:
            total += 45
        elif weight <= 1000:
            total += 55
        elif weight <= 2000:
            total += 70

    return total

def main():
    '''main function'''
    a = int(input())
    b = int(input())

    envelop = cal_envelop(a)
    package = cal_package(b)
    total = envelop + package
    print(total)

main()
