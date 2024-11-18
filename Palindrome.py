"""Palindrome"""

def is_palindrome(text):
    """Return true if text is paindrome"""
    reverse_text = str(int(text[::-1]))
    if reverse_text == text:
        return True
    return False

def find_next_palindrome(count_next, time):
    """find next count_next palindrome"""
    colon_idex = time.find(":")
    hours = int(time[:colon_idex])
    minute = int(time[colon_idex + 1:])
    found_palindrome = 0

    while found_palindrome < count_next:
        minute += 1

        if minute == 60:
            hours += 1
            minute = 0

        if hours == 24 and minute == 00:
            hours = 0

        if is_palindrome(f"{str(hours):0>2}" + f"{str(minute):0>2}"):
            found_palindrome += 1
            print(f'{hours}:{minute:0>2}')

find_next_palindrome(int(input()), input())
