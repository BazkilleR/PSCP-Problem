"""HorizontalHistogram"""
def create_histogram_line(count):
    """mmfe"""
    line = ""
    for i in range(count):
        if not i % 5 and i:
            line += "|"
        line += "-"
    return line

def main():
    """HorizontalHistogram"""
    input_string = input()
    character_list = []
    unique_character_list = []
    for character in input_string:
        character_list.append([character, input_string.count(character)])
    for character in character_list:
        if character not in unique_character_list:
            unique_character_list.append(character)
    unique_character_list.sort(key=lambda x: (x[0].isupper(), x[0]))
    for character in unique_character_list:
        histogram_line = create_histogram_line(character[1])
        print(f"{character[0]} : {histogram_line}")

main()
