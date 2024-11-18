"""Stair"""
def main():
    """Stair"""
    y = int(input())
    n = int(input())
    xList = []
    num = 0
    c = 0
    i1 = -1
    for _ in range(n):
        x = int(input())
        xList.append(x)
    for i in xList:
        num += i
        i1 += 1
        if i > y:
            c = "NO"
            break
        if num == y:
            c += 1
            num = 0
        elif num < y and i1 == n - 1:
            c += 1
            num = 0
        elif num > y:
            c += 1
            num = i
            if num < y and i1 == n - 1:
                c += 1
    print(c)

main()
