import jack

def test_calc_total():
    total = jack.clac_total(4,5)
    assert total == 9

def test_calc_multiply():
    result = jack.calc_multiply(10,3)
    assert result == 30
