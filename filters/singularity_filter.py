from functools import lru_cache
from sympy import symbols, limit, S, singularities

x = symbols("x")

@lru_cache(maxsize=256)
def singularity_filter(expr):
    s = singularities(expr, x)

    if not s:
        return {"status": "clean"}

    results = []
    for point in s:
        left = limit(expr, x, point, "-")
        right = limit(expr, x, point, "+")

        if left != right:
            results.append(point)

    if results:
        return {"status": "twist_detected", "points": results}

    return {"status": "hidden_singularity", "point": list(s)[0]}
