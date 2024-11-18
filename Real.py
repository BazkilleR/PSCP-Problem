"""real"""

def decode_segment(binary_input):
    """Converts a 7-segment binary input to its corresponding digit, and checks for decimal point"""
    segment_to_digit = {
        "1111110": "0",
        "0110000": "1",
        "1101101": "2",
        "1111001": "3",
        "0110011": "4",
        "1011011": "5",
        "1011111": "6",
        "1110000": "7",
        "1111111": "8",
        "1111011": "9"
    }

    # Extract the first 7 bits and look up the corresponding digit
    digit = segment_to_digit.get(binary_input[:7], None)
    if digit is None:
        return None, True  # Invalid digit, trigger error

    # Check if the last bit (8th bit) is for a decimal point
    if binary_input[7] == "1":
        digit += "."

    return digit, False


def main():
    """Main function to read 3 segments and output the corresponding float or error."""
    result = ""
    error = False

    for _ in range(3):
        binary_input = ""
        for _ in range(8):
            user_input = input()
            if user_input != "off":
                binary_input += "1"
            else:
                binary_input += "0"

        decoded_digit, error = decode_segment(binary_input)
        if error:
            print("Error")
            return

        result += decoded_digit

    if result.count(".") > 1:
        print("Error")
    else:
        print(f"{float(result):.2f}")

main()
