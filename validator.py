from parser import check_syntax
from algebra import check_algebra
from logic import check_logic
from topology import check_topology
from numeric import check_numeric

def validate(equation: str):
    return {
        "syntax": check_syntax(equation),
        "algebra": check_algebra(equation),
        "logic": check_logic(equation),
        "topology": check_topology(equation),
        "numeric": check_numeric(equation)
    }
