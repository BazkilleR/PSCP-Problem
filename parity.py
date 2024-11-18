'''Parity'''

def amout_one(byte):
    '''asd'''
    len_one = 0
    for bit in byte:
        if bit == '1':
            len_one += 1
    return len_one

def parity(byte, select):
    '''parity'''
    result = ''
    len_one = amout_one(byte)
    if select == 'Even':
        if len_one % 2:
            result = byte + '1'
        else:
            result = byte + '0'
    elif select == 'Odd':
        if len_one % 2:
            result = byte + '0'
        else:
            result = byte + '1'

    return result

print(parity(input(), input()))
