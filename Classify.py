"""Classify"""

def main():
    """Classify"""
    result = []
    unique_codes = []
    all_codes = []
    processed_codes = []
    counts = []

    while True:
        code = input()
        if code == "END":
            break
        all_codes.append(code[:4])

    all_codes.sort()

    for code in all_codes:
        if code not in processed_codes:
            counts.append(all_codes.count(code))
            unique_codes.append(code)
        processed_codes.append(code)

    current_prefix = unique_codes[0][:2]
    flag = 0
    index = 0

    for code in unique_codes:
        if code[:2] == current_prefix and not flag:
            flag = 1
            result.append(code[:2] + " " + str(int(code[2:])) + " " + str(counts[index]))
        elif code[:2] == current_prefix:
            result.append("--" + " " + str(int(code[2:])) + " " + str(counts[index]))
        else:
            current_prefix = code[:2]
            result.append(code[:2] + " " + str(int(code[2:])) + " " + str(counts[index]))
        index += 1

    for entry in result:
        print(entry)

main()
