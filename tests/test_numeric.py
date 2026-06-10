from numeric import check_numeric

def test_quadratic():
    result = check_numeric("x^2 - 4")
    assert "Solutions" in result
