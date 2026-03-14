def tokenize(expression):
    tokens = []
    current_number = ""
    for char in expression:
        if char.isdigit():
            current_number += char
        else:
            if current_number != "":
                tokens.append(current_number)
                current_number = ""
            if char in "+-*/()":
                tokens.append(char)
    if current_number != "":
        tokens.append(current_number)
    return tokens
