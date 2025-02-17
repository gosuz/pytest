import pytest
from calculator_performance_testing import Calculator

@pytest.mark.parametrize("numbers", [
    (1, 1),
    (100, 100),
    (1000, 1000),
    (10**6, 10**6),
    (10**9, 10**9)
])

@pytest.mark.benchmark(group="efficient_multiply")
def test_efficient_multiply_performance(benchmark, numbers):
    calc = Calculator()
    a, b = numbers
    result = benchmark(calc.multiply, a, b)
    assert result == a * b

@pytest.mark.parametrize("numbers", [
    (1, 1),
    (100, 100),
    (1000, 1000),
    (10**6, 10**6),
    (10**9, 10**9)
])

@pytest.mark.benchmark(group="inefficient_multiply")
def test_inefficient_multiply_perfromance(benchmark, numbers):
    calc = Calculator()
    a,b = numbers
    result = benchmark(calc.inefficient_multiply, a,b)
    assert result == a * b

# def test_add():
#     calc = Calculator()
#     assert calc.add(1,2) == 3
