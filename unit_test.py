from calculator import Calculator

# Function we want to test
def add(a,b):
    return a + b + 1

# Unit test
def test_add_unit_test():
    assert add(1,2) == 3

def test_calculator_functionality():
    calc = Calculator()
    total = calc.add(2,3)
    result = calc.multiply(total, 3)
    assert result == 15
