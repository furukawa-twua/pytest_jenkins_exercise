from exercise import CalcDistance, IsPrime

def test_CalcDistance ():
    assert CalcDistance(0, 2, 3, 6) == 5

def test_IsPrime ():
    assert IsPrime(119299)
