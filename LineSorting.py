"""line sorting"""

def sort_text_by_length():
    """Sorts a list of text strings by their lengths."""

    text_list = []

    for _ in range(int(input())):
        text_list.append(input())

    sorted_list = sorted(text_list, key=len)

    for text in sorted_list:
        print(text)

sort_text_by_length()
