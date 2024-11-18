'''ValidVar'''

def verify_text():
    '''Verify variable names for validity according to Python rules.'''
    result = []

    keywords = {'if', 'else', 'elif', 'while', 'for', 'True', 'False',
                'continue', 'break', 'return', 'is', 'in', 'and', 'or',
                'from', 'as', 'pass', 'not', 'def', 'None'}

    num_cases = int(input())

    for _ in range(num_cases):
        text = input().strip()
        status = 'Valid'

        # Check if the text is a keyword
        if text in keywords:
            status = 'Invalid'

        # Check if the first character is numeric
        elif text and text[0].isdigit():
            status = 'Invalid'

        # Check if the text contains only valid characters
        elif not all(c.isalnum() or c == '_' for c in text):
            status = 'Invalid'

        result.append(status)

    for res in result:
        print(res)

verify_text()
