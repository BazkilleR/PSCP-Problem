'''century'''

def calculate_century():
    '''calculate_century'''
    num_cases = int(input())
    centuries = []

    for _ in range(num_cases):
        input_year = input()
        year_numeric = ""
        year_era = ""
        decimal_position = 0
        year_decimal = 0

        # Separate numbers and era identifier
        for char in input_year:
            if char.isnumeric():
                year_numeric += char
            else:
                year_era += char

        # Adjust for the Buddhist Era (B.E.)
        if year_era.strip() == 'B.E.':
            year_numeric = int(year_numeric) - 543

        year_numeric = int(year_numeric) / 100

        # Locate decimal and extract the part after it
        for idx, char in enumerate(str(year_numeric)):
            if char == '.':
                year_decimal = int(str(year_numeric)[idx + 1:])
            decimal_position += 1

        # Determine century based on the decimal part
        if 0 < year_numeric * 100 <= 100:
            century = 1
        elif year_numeric * 100 > 100:
            century = int(year_numeric) if not year_decimal else int(year_numeric) + 1
        else:
            century = "ERROR"

        centuries.append(century)

    # Output the result
    for century in centuries:
        print(century)

calculate_century()
