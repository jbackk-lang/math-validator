from validator import validate

def test_basic_equation():
    result = validate("x + 1")
    assert result["syntax"] == "OK"
