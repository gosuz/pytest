from calculator import Calculator

# Functional test
def test_calculator_functionality():
    calc = Calculator()
    total = calc.add(3,2)
    multiplication_result = calc.multiply(total, 3)

    assert multiplication_result == 15

# Unit test
def test_add():
    calc = Calculator()
    assert calc.add(1, 2) == 3
