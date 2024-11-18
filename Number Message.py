'''Number Message'''

def format_text(text):
    '''format text'''
    text1 = text.replace('12', 'R')
    text1 = text1.replace('13', 'B')
    text1 = text1.replace('1', 'I')
    text1 = text1.replace('3', 'E')
    text1 = text1.replace('4', 'A')
    text1 = text1.replace('5', 'S')
    text1 = text1.replace('0', 'O')

    new_text = ''
    for i in text1:
        if i.isalpha() or i.isspace():
            new_text += i

    return new_text.upper()

print(format_text(input()))
