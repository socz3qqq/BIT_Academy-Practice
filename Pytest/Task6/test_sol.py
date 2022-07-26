import pytest
from random import randint
from solution import prime

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n%i==0:
            return False
    
    return True

class TestInitial:
    @pytest.mark.parametrize("data, expected", [(7, True), (15, False), (19, True), (27, False)])
    def test_0(self, data, expected):
        try:
            assert prime(data) == expected
        except:
            i_f = True
            pytest.fail()

    def test_1(self):
        x = randint(10, 10**3)
        assert prime(x) == is_prime(x)

    def test_2(self):
        x = randint(10, 10**3)
        assert prime(x) == is_prime(x)

    def test_3(self):
        x = randint(10**2, 10**4)
        assert prime(x) == is_prime(x)

class TestCorner:
    @pytest.mark.parametrize("data, expected", [(2, True), (3, True), (0, False), (1, False), (-2, False)])
    def test_0(self, data, expected):
        assert prime(data) == expected

class TestRandom:
    def test_0(self):
        x = randint(10**8, 10**9)
        assert prime(x) == is_prime(x)

    def test_1(self):
        x = randint(10**9, 10**10)
        assert prime(x) == is_prime(x)

    def test_2(self):
        x = randint(10**10, 10**12)
        assert prime(x) == is_prime(x)

    def test_3(self):
        x = randint(10**10, 10**12)
        assert prime(x) == is_prime(x)

    def test_4(self):
        x = randint(10**11, 10**12)
        assert prime(x) == is_prime(x)

class TestMaxi:
    def test_0(self):
        assert prime(5448425984694149) == True

    def test_1(self):
        assert prime(4088765295373739) == True

    def test_2(self):
        assert prime(4088765295373731) == False
    
    def test_3(self):
        assert prime(2372154294303967) == True