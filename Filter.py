"""Filter"""
def main():
    """Filter"""
    input_string = input().replace("{", "").replace("}", "").replace("\"", "")
    threshold = float(input())
    entries = input_string.split(", ")
    parsed_entries = []

    for entry in entries:
        parsed_entries.append(entry.split(": "))

    parsed_entries.sort(key=lambda x: x[0][:])

    for entry in parsed_entries[:]:
        if float(entry[1]) < threshold:
            parsed_entries.remove(entry)

    if parsed_entries:
        for entry in parsed_entries:
            print(f"{entry[0]}\t{float(entry[1]):.2f}")
    else:
        print("Nope")

main()
