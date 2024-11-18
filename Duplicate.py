'''Duplicate I'''

def find_dup(n, m):
    '''find dup'''
    g1 = set(input() for _ in range(n))
    g2 = set(input() for _ in range(m))

    dup_id = sorted((g1 & g2), reverse=True)

    if not dup_id:
        print("Nope")
    else:
        for i in dup_id:
            print(i)

find_dup(int(input()), int(input()))
