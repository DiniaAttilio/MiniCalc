from models import NumberNode, BinOpNode

def parse_expression(tokens, min_precedence=0):
    token = tokens.pop(0)
    if token.isdigit():
        current_node = NumberNode(token)
    elif token == "(":
        current_node = parse_expression(tokens)
        tokens.pop(0)  # rimuove ")"

    precedenza = {'+': 1, '-': 1, '*': 2, '/': 2}

    while tokens:
        op = tokens[0]
        if op not in precedenza:
            break
        precedenza_op = precedenza[op]
        if precedenza_op < min_precedence:
            break

        tokens.pop(0)  # consuma l'operatore

        next_token = tokens.pop(0)
        if next_token.isdigit():
            right_node = NumberNode(next_token)
        elif next_token == "(":
            right_node = parse_expression(tokens)
            tokens.pop(0)  # rimuove ")"

        while tokens and tokens[0] in precedenza and precedenza[tokens[0]] > precedenza_op:
            right_node = parse_expression(tokens, min_precedence=precedenza[tokens[0]])

        current_node = BinOpNode(left=current_node, operator=op, right=right_node)

    return current_node
