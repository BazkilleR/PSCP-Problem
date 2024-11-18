"""BreachTheDoor"""

def translate(text):
    """sdada"""
    word_list = text.split()
    cleaned_list = []

    for word in word_list:
        cleaned_word = ""

        for char in word:
            if char.isalpha():
                cleaned_word += char

        cleaned_list.append(cleaned_word)

    filter_list = []
    for word in cleaned_list:
        if len(word) > 6:
            filter_list.append(word)

    print(" ".join(filter_list))

translate(input())
