'''Pringles'''

def can_get():
    '''Helllo'''
    border = input()
    piece = input()
    border = input()
    finger_depth = int(input())

    get_piece = 0
    have_left = False
    after = ''

    for i in piece:
        if finger_depth > 0 and i == ')':
            get_piece += 1
            after += ' '
        elif finger_depth <= 0 and i == ')':
            have_left = True
            after += i
        else:
            after += i
        finger_depth -= 1

    print(get_piece)

    if have_left:
        print('There are still some left.')
    else:
        print('None.')

    print(border)
    print(after)
    print(border)

can_get()
