"""LetterFrequency"""

def find_most_letter(text):
    """sadas"""
    letters_dict = {}
    for char in text:
        if char.isalpha():  # Include this to focus only on letters
            if char not in letters_dict:
                letters_dict[char] = 1
            else:
                letters_dict[char] += 1

    # Use max with key parameter correctly to find the letter with the highest count
    most_frequent_letter = max(letters_dict, key=letters_dict.get)
    print(most_frequent_letter)

find_most_letter(input())
