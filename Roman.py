"""Roman"""
def roman(numeral):
    """ROMAN"""
    value = 0
    if numeral == "N":
        value += 90
    elif numeral == "L":
        value += 50
    elif numeral == "F":
        value += 40
    elif numeral == "X":
        value += 10
    elif numeral == "n":
        value += 9
    elif numeral == "V":
        value += 5
    elif numeral == "f":
        value += 4
    elif numeral == "I":
        value += 1
    return value

def main():
    """Roman"""
    roman_string = input().replace("IV", "f").replace("IX", "n").replace("XL", "F")
    roman_string = roman_string.replace("XC", "N").replace("CD", "R").replace("CM", "G")
    total_value = 0

    for char in roman_string:
        if char == "M":
            total_value += 1000
        elif char == "G":
            total_value += 900
        elif char == "D":
            total_value += 500
        elif char == "R":
            total_value += 400
        elif char == "C":
            total_value += 100
        else:
            total_value += roman(char)

    print(total_value)

main()
