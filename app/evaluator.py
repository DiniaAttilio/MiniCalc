from models import NumberNode, BinOpNode

def evaluate(node):
    if isinstance(node, NumberNode):
        return node.value
    elif isinstance(node, BinOpNode):
        left_val = evaluate(node.left)
        right_val = evaluate(node.right)
        if node.operator == '+':
            return left_val + right_val
        elif node.operator == '-':
            return left_val - right_val
        elif node.operator == '*':
            return left_val * right_val
        elif node.operator == '/':
            return left_val / right_val
