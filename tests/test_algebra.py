from algebra import check_algebra

def test_division_by_zero():
    assert "division by zero" in check_algebra("1/(x-x)")
