"""Easy Histogram"""

def coount_string(text):
    """Counts occurrences of non-whitespace, non-digit characters in a text string."""

    string_dict = {}

    for string in text:
        if not string.isspace() and not string.isdigit():
            string_dict[string] = string_dict.get(string, 0) + 1

    sorted_dict = dict(sorted(string_dict.items(), key=lambda x: (x[0].lower(), x[0].isupper())))

    for key, value in sorted_dict.items():
        print(f"{key} = {value}")

coount_string(input())
