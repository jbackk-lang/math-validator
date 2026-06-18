from sympy import sympify

class ParsedExpr:
    def __init__(self, expr):
        self.expr = expr
        self.is_zoo = expr.is_infinite
        self.is_const = expr.is_constant()
        self.has_division = any(node.is_Rational or node.is_Pow for node in expr.atoms())
        self.fractions = [n for n in expr.atoms() if n.is_Rational]
        self.powers = [p for p in expr.atoms() if p.is_Pow]
        self.cycles = len(self.fractions) + len(self.powers)

def parse(expr_str):
    expr = sympify(expr_str)
    return ParsedExpr(expr)
