'''One For All'''

def one_for_all(count):
    '''united smash!!!!'''
    result = ''

    if not count:
        return ""

    for i in range(1, count + 1):
        result += input()

        if i < count and count > 1:
            if i % 2:
                result += '*' * i
            else:
                result += '-' * i

    result += f"_{count}"

    return result

print(one_for_all(int(input())))
