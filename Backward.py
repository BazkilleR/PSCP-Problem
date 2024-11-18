'''Backward'''

def reverse_input():
    '''dsadasda'''
    text_list = []
    while True:
        text = input()

        if text == 'NULL':
            break

        text_list.append(text)

    print(*reversed(text_list), sep='\n')

reverse_input()
