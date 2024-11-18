'''Easy Histogram No Dict'''

def count_string(text):
    '''count string'''
    string_list = []
    result_list = []

    for string in text:
        if not string.isdigit() and not string.isspace():
            string_list.append(string)

    string_list = list(set(string_list))
    sorted_list = sorted(sorted(string_list, reverse=True), key=str.lower)

    for string in sorted_list:
        result_list.append([string, text.count(string)])

    list_len = len(result_list)
    for i in range(list_len):
        print(f'{result_list[i][0]} = {result_list[i][1]}')

count_string(input())
