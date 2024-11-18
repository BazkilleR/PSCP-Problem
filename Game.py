'''Game'''

def find_draw(a, b):
    '''main'''
    if a%3 == b%3:
        print(a%3)
    else:
        print('Error')

find_draw(int(input()), int(input()))
