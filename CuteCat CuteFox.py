"""cute cat fox"""

def extract_numeric_and_text(data):
    """Extracts numeric and text components from the input."""
    text_part = ""
    numeric_part = ""
    for char in data[1]:
        if str(char).isnumeric():
            numeric_part += char
        else:
            text_part += char
    return text_part, int(numeric_part)

def main():
    """Main function to categorize and count Cats and Foxes."""
    data_dict = {}
    cat_count = 0
    fox_count = 0
    for _ in range(int(input())):
        entry = input().replace("}", "").replace("{", "")
        key_value = entry.split(" : ")
        key = key_value[0][1:-1]
        value = key_value[1][1:-1]
        data_dict[key] = value

    if "Cat01" not in data_dict.values() and "Garfield" not in data_dict:
        key = "Garfield"
        value = "Cat01"
        data_dict[key] = value

    if "Fox01" not in data_dict.values() and "Fubuki" not in data_dict:
        key = "Fubuki"
        value = "Fox01"
        data_dict[key] = value

    for value in data_dict.values():
        if value[:3] == "Cat":
            cat_count += 1
        else:
            fox_count += 1

    sorted_data = dict(sorted(data_dict.items(), key=extract_numeric_and_text))
    print(f"Cat : {cat_count}\nFox : {fox_count}")

    for key, value in sorted_data.items():
        print(key, ":", value)

main()
