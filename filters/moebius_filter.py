def run(expr: str):
    # analiza
    return {
        "status": "ok",
        "details": ...
    }
def run(expr: str):
    # filtr Möbiusa: wykrywa odwrócenia, pętle, transformacje
    score = 0
    if "/" in expr:
        score += 1
    if "**-1" in expr:
        score += 1
    if "(" in expr and ")" in expr:
        score += 1

    return {
        "status": "ok",
        "moebius_density": score
    }
