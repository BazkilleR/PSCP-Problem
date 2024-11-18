"""WordSequence I"""

def word_sequence(text):
    """Prints incremental sequences of the input text"""
    result = ""
    for char in text:
        result += char
        print(result)

word_sequence(input())
