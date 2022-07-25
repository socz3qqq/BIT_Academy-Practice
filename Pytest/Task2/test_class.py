from function import is_prime
from random import randint

def check_is_prime(n):
    if n < 2:
        return False
    if n == 0 or n == 3:
        return True
    if n%2 == 0 or n%3 == 0:
        return False
    i = 6
    g = int((n**(0.5)))
    while i<=g:
        if n%(i-1) == 0:
            return False
        if i+1<=g:
            if n%(i+1) == 0:
                return False
        i+=6
    return True


class TestMini:
    # Napisać testy sprawdzające funkcję is_prime dla liczb
    # z przedziału <-1, 6>
    def test_n1(self): #n - negative
        assert is_prime(-1) is True # błąd w  is_prime
    def test_0(self):
        assert is_prime(0) is False
    def test_1(self):
        assert is_prime(1) is False
    def test_2(self):
        assert is_prime(2) is True
    def test_3(self):
        assert is_prime(3) is True
    def test_4(self):
        assert is_prime(4) is False
    def test_5(self):
        assert is_prime(5) is True
    def test_6(self):
        assert is_prime(6) is False

class TestMid:
    # Napisać 5 testów sprawdzających funkcję is_prime dla losowych
    # liczb z przedziału <10 ** 4, 10 ** 5>
    def test_1(self):
        n = randint(10**4, 10**5)
        assert is_prime(n) == check_is_prime(n)

    def test_2(self):
        n = randint(10**4, 10**5)
        assert is_prime(n) == check_is_prime(n)

    def test_3(self):
        n = randint(10**4, 10**5)
        assert is_prime(n) == check_is_prime(n)

    def test_4(self):
        n = randint(10**4, 10**5)
        assert is_prime(n) == check_is_prime(n)

    def test_5(self):
        n = randint(10**4, 10**5)
        assert is_prime(81368) == check_is_prime(81368)

class TestMaxi:
    def test_1(self):
        n = randint(10**12, 10**13)
        assert is_prime(n) == check_is_prime(n)
    def test_2(self):
        n = randint(10**12, 10**13)
        assert is_prime(n) == check_is_prime(n)
    def test_3(self):
        n = randint(10**12, 10**13)
        assert is_prime(n) == check_is_prime(n)
    def test_4(self):
        n = randint(10**12, 10**13)
        assert is_prime(n) == check_is_prime(n)
    def test_5(self):
        n = randint(10**12, 10**13)
        assert is_prime(n) == check_is_prime(n)
    # Napisać 5 testów sprawdzających funkcję is_prime dla losowych
    # z przedziału <10 ** 12, 10 ** 13>, a następnie
    # naprawić funkcję is_prime aby testy wykonywały się szybciej
    # niż dla aktualnej funkcji
