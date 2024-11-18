'''Tuple's Sad life'''

def use_tuple(text, focus):
    '''Tuple's Sad life'''
    num_tuple = tuple(text.split())
    idx = num_tuple.index(focus)
    count = num_tuple.count(focus)

    for _ in range(count):
        for _ in range(count):
            print(idx, end=' ')
        print()

use_tuple(input(), input())
