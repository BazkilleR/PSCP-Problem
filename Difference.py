'''difference'''

def find_diff(m: int, n: int):
    '''find diff'''
    a = set()
    b = set()

    for _ in range(m):
        a.add(int(input()))

    for _ in range(n):
        b.add(int(input()))

    result = set()
    for i in a:
        if i not in b:
            result.add(i)

    result = sorted(result)

    output = " ".join(map(str, result))
    print(output)

find_diff(int(input()), int(input()))
