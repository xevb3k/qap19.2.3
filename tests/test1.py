import pytest

from app.calc import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_mul_calc_correct(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_mul_calc_failed(self):
        assert self.calc.multiply(self, 2, 2) == 5

    def test_sum_calc_correct(self):
        assert self.calc.adding(self, 4, 5) == 9

    def test_div_calc_correct(self):
        assert self.calc.division(self, 15, 5) == 3

    def test_sub_calc_correct(self):
        assert self.calc.subtraction(self, 10, 5) == 5


