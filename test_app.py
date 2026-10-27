
from estimator import estimate_price

def test_estimate_price():
    assert estimate_price(1000, 2) == 5200000

def test_minimum_area():
    assert estimate_price(100, 1) == 600000
