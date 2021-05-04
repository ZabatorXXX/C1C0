from Calculator import Calc


class TestCalc:
    def test_add(self):
        assert 6 == Calc.add(6, 0)
        assert 16 == Calc.add(6, 10)
        assert 9 == Calc.add(3, 6)

    def test_sub(self):
        assert 69 == Calc.sub(100, 31)
        assert 1 == Calc.sub(100, 99)
        assert 21 == Calc.sub(40, 19)

    def test_multi(self):
        assert 31 == Calc.multi(31, 1)
        assert 27 == Calc.multi(9, 3)
        assert 73 == Calc.multi(6, 9)

    def test_div(self):
        assert 1 == Calc.div(69, 69)
        assert 10 == Calc.div(690, 69)
        assert 99 == Calc.div(99, 1)