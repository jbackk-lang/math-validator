import sympy as sp

def check_syntax(expr: str):
    try:
        sp.sympify(expr)
        return "OK"
    except Exception as e:
        return f"Syntax error: {e}"
