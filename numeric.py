import sympy as sp

def check_numeric(expr: str):
    try:
        x = sp.symbols('x')
        e = sp.sympify(expr)

        sol = sp.solve(e, x)
        return f"Solutions: {sol}"
    except Exception as e:
        return f"Numeric error: {e}"
