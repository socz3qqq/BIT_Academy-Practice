import pytest
from function import prime_greater_than, prime
from random import randint

def ftest(n):
    n+=1
    while True:
        if prime(n):
            return n
        n+=1

class TestInitial:
    @pytest.mark.parametrize("data, expected", [(5, 7), (11, 13), (12, 13), (50, 53)])
    def test_0(self, data, expected):
        assert prime_greater_than(data) == expected

class TestCorner:
    @pytest.mark.parametrize("data, expected", [(-1, 2), (2, 3), (5, 7), (0, 2), (1, 2)])
    def test_0(self, data, expected):
        assert prime_greater_than(data) == expected

class TestMini:
    data = [randint(-20, 100) for _ in range(20)]

    @pytest.mark.parametrize("n", data)
    def test(self, n):
        assert prime_greater_than(n) == ftest(n)

class TestMaxi:
    data = [randint(10**9, 10**12) for _ in range(20)]

    @pytest.mark.parametrize("n", data)
    def test(self, n):
        assert prime_greater_than(n) == ftest(n)