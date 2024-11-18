"""PongYa"""

def pongya(num):
    """PongYa"""
    result = ""

    for i in range(1, num + 1):
        if not i % 3 or str(i)[-1] == "3":
            result = "PONG"
        else:
            result = i

    return result

print(pongya(int(input())))
