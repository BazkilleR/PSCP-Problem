"""Password"""
import math
import string

def meter(e):
    """meter"""
    # Password strength based on entropy
    if e <= 27:
        return e, "Very Weak"
    if e <= 35:
        return e, "Weak"
    if e <= 59:
        return e, "Reasonable"
    if e <= 127:
        return e, "Strong"
    return e, "Very Strong"

def how_strong(password):
    """Improved password strength checker."""
    l = len(password)

    # Character pools
    lower = string.ascii_lowercase  # 26
    upper = string.ascii_uppercase  # 26
    digits = string.digits  # 10
    special = string.punctuation  # 32

    # Track usage of different character types
    has_lower = has_upper = has_digit = has_special = False

    # Check for character types in the password
    for char in password:
        if char in lower:
            has_lower = True
        elif char in upper:
            has_upper = True
        elif char in digits:
            has_digit = True
        elif char in special:
            has_special = True

    # Calculate the size of the character pool
    r = 0
    if has_lower:
        r += len(lower)
    if has_upper:
        r += len(upper)
    if has_digit:
        r += len(digits)
    if has_special:
        r += len(special)

    # Entropy calculation
    e = math.floor(math.log2(r**l))

    entropy, feedback = meter(e)
    print(entropy)
    print(feedback)

how_strong(input())
