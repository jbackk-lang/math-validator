from parser import check_syntax
from algebra import check_algebra
from logic import check_logic
from topology import check_topology
from numeric import check_numeric

import importlib
import pkgutil
import filters

def load_filters():
    loaded = {}
    for _, module_name, _ in pkgutil.iter_modules(filters.__path__):
        module = importlib.import_module(f"filters.{module_name}")
        if hasattr(module, "run"):
            loaded[module_name] = module.run
    return loaded

FILTERS = load_filters()

def validate(equation: str):
    results = {}
    for name, func in FILTERS.items():
        results[name] = func(equation)
    return results

def validate(equation: str):
    return {
        "syntax": check_syntax(equation),
        "algebra": check_algebra(equation),
        "logic": check_logic(equation),
        "topology": check_topology(equation),
        "numeric": check_numeric(equation)
    }
