"""
Unit test for the calculator library
"""
import calculator


class TestCalculator:
    def test_addition(self):
        assert 3 == calculator.add(1, 2)

    def test_addition2(self):
        assert 7 == calculator.add(4, 3)

    def test_substraction(self):
        assert 2 == calculator.subtract(4, 2)

    def test_multiplication(self):
        assert 100 == calculator.multiply(10, 10)

    def test_divition(self):
        assert 2 == calculator.divide(10, 5)
