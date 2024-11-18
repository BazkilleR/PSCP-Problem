'''diamond'''

def jiaranai_pet(thickness):
    '''jiaranai diamond kub'''

    # Upper part
    for i in range(thickness // 2):
        outer_space = thickness // 2 - i
        inner_space = 2 * i - 1
        if not i:
            print(' ' * outer_space + '*')
        else:
            print(' ' * outer_space + '*' + ' ' * inner_space + '*')

    # Middle part
    print('*' * thickness)

    # Lower part
    for i in range(thickness // 2 - 1, -1, -1):
        outer_space = thickness // 2 - i
        inner_space = 2 * i - 1
        if not i:
            print(' ' * outer_space + '*')
        else:
            print(' ' * outer_space + '*' + ' ' * inner_space + '*')

jiaranai_pet(int(input()))
