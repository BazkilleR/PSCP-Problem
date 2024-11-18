'''BigFrame'''

def make_frame(text1: str, text2: str, text3: str, text4: str, text5: str) -> None:
    '''crete frame'''
    text_group = [text1.strip(), text2.strip(), text3.strip(), text4.strip(), text5.strip()]
    most_string = max(len(text) for text in text_group)

    print('*' * (most_string + 4))
    for text in text_group:
        print(f'* {text:<{most_string}} *')
    print('*' * (most_string + 4))

make_frame(input(), input(), input(), input(), input())
