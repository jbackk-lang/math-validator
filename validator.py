from core import parse
from filters.singularity_filter import singularity_filter
from filters.topology_filter import topology_filter

def validate(expr_str):
    parsed = parse(expr_str)
    s = singularity_filter(parsed.expr)
    t = topology_filter(parsed, s)
    return t
