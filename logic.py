import sympy as sp

def check_logic(expr: str):
    try:
        e = sp.sympify(expr)
        if e == True:
            return "Tautology"
        if e == False:
            return "Contradiction"
        return "OK"
    except Exception as e:
        return f"Logic error: {e}"
