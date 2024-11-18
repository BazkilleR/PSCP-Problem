'''Run length Encoding'''

def encode_string(s):
    '''dsadad'''
    if not s:
        return ""

    encoded = []
    count = 1
    prev_char = s[0]

    for char in s[1:]:
        if char == prev_char:
            count += 1
        else:
            encoded.append(f"{count}{prev_char}")
            prev_char = char
            count = 1

    encoded.append(f"{count}{prev_char}")
    return ''.join(encoded)

print(encode_string(input()))
