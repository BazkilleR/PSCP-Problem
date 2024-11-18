'''Run Length Decoding'''

def decoding(text):
    '''decoding'''
    full_text = ""
    count_char = ""

    for char in text:
        if char.isdigit():
            count_char += char
        elif char.isalpha():
            full_text += char * int(count_char)
            count_char = ""

    return full_text

print(decoding(input()))
