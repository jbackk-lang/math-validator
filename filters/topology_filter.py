from sympy import sympify, singularities
import re

def run(expr: str):
    result = {
        "status": "ok",
        "Λ_structure": None,
        "τ_transforms": None,
        "ρ_defects": None,
        "singularities": [],
        "notes": []
    }

    # 1. Λ — analiza struktury (czy równanie ma cykle, pętle, sprzężenia)
    cycles = expr.count("(") + expr.count(")")
    fractions = expr.count("/")
    powers = len(re.findall(r"\*\*", expr))

    result["Λ_structure"] = {
        "cycles": cycles,
        "fractions": fractions,
        "powers": powers
    }

    # 2. τ — transformacje (odwrócenia, skręty, zmiany orientacji)
    tau_score = 0
    if "/" in expr:
        tau_score += 1
    if "**-1" in expr:
        tau_score += 1
    if "sqrt" in expr:
        tau_score += 1
    if "^" in expr:
        tau_score += 1

    result["τ_transforms"] = tau_score

    # 3. ρ — defekty topologiczne (punkty osobliwe)
    try:
        f = sympify(expr)
        sing = list(singularities(f))
        result["singularities"] = [str(s) for s in sing]
        result["ρ_defects"] = len(sing)
    except Exception as e:
        result["status"] = "error"
        result["notes"].append(str(e))

    return result
