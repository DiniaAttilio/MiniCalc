from lexer import tokenize
from parser import parse_expression
from evaluator import evaluate

if __name__ == "__main__":
    expr = input("Inserisci espressione: ")
    tokens = tokenize(expr)
    ast = parse_expression(tokens)
    print("AST:", ast)
    print("Risultato:", evaluate(ast))
