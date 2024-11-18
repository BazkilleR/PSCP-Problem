'''key'''

def format_id(id):
    '''key'''
    total = 0
    idx = 1
    last_3digit = ""

    for num in id:
        total += int(num)
        if idx >= 11:
            last_3digit += num
        idx += 1

    result = total + (int(last_3digit) * 10)

    if len(str(result)) < 4:
        result += 1000

    print(str(result)[-4:])

format_id("1234567890123")