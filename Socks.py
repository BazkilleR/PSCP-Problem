"Socks"

def pair_sock(text):
    "pair_sock"
    char_dict = {}
    for i in text.upper():
        if i not in char_dict:
            char_dict[i] = 1
        else:
            char_dict[i] += 1

    result = ""
    count = 0
    for key in sorted(char_dict):
        pair_amount = char_dict[key] // 2
        result += ((key * 2) + " ") * pair_amount
        count += pair_amount

    if result:
        print(result)
        print(count)
    else:
        print("None")
        print(0)

pair_sock(input())
