"""AndAgain"""

def find_word(text):
    """Extracts words with at least two different vowels and prints them in sorted order."""
    result = []
    vowels = set("aeiou")
    words = text.split()

    for word in words:
        clean_word = ""
        vowel_count = 0

        # Clean the word by checking if each character is alphabetic
        for char in word:
            if char.isalpha():
                clean_word += char
                if char in vowels:
                    vowel_count += 1

        # Count unique vowels in the cleaned word
        if vowel_count >= 2:
            result.append(clean_word)

    sorted_result = sorted(result)

    if sorted_result:
        for i in sorted_result:
            print(i)
    else:
        print("Nope")

find_word(input())
