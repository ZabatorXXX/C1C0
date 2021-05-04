from Calculator import Calc


class TestCalc:

    def test_addition(self):
        assert 6 == Calc.addition(6, 0)
        assert 16 == Calc.addition(6, 10)
        assert 9 == Calc.addition(3, 6)

    def test_subtract(self):
        assert 69 == Calc.subtract(100, 31)
        assert 1 == Calc.subtract(100, 99)
        assert 21 == Calc.subtract(40, 19)

    def test_multiply(self):
        assert 31 == Calc.multiply(31, 1)
        assert 27 == Calc.multiply(9, 3)
        assert 73 == Calc.multiply(6, 9)

    def test_divide(self):
        assert 1 == Calc.divide(69, 69)
        assert 10 == Calc.divide(690, 69)
        assert 99 == Calc.divide(99, 1)
