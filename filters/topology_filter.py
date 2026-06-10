def run(expr: str):
    # analiza
    return {
        "status": "ok",
        "details": ...
    }
from sympy import sympify, singularities

def run(expr: str):
    try:
        f = sympify(expr)
        sing = list(singularities(f))
        return {
            "status": "ok",
            "singularities": [str(s) for s in sing]
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }
