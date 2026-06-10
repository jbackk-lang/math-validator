import sympy as sp

def check_algebra(expr: str):
    try:
        e = sp.sympify(expr)
        if e.has(sp.zoo):
            return "Error: division by zero"
        return "OK"
    except Exception as e:
        return f"Algebra error: {e}"
