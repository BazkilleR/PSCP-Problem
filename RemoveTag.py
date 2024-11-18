"""RemoveTag"""

def main():
    """RemoveTag"""
    input_text = input()
    cleaned_text = ""
    inside_tag = 0

    if "<" in input_text:
        for char in input_text:
            if char == ">":
                inside_tag = 1
            if inside_tag and not char in ("<", ">"):
                cleaned_text += char
            if char == "<":
                cleaned_text += " "
                inside_tag = 0
        cleaned_text = cleaned_text.split()
    else:
        cleaned_text = input_text.split()

    print(cleaned_text)

main()
