from cmplex import C
from random import randint

# Napisać testy sprawdzające porównywanie liczb zespolonych
# w załączonym pliku

file = open("data.txt")

c_numbers = []

for line in file:
    num = line.split()
    for i in range(len(num)):
        num[i] = int(num[i])
    
    c_numbers.append(num)

file.close()

class TestInitial:
    def test_0(self):
        assert C(0, 0) == C(0, 0)
        
    def test_1(self):
        assert C(-1, -1) == C(-1, -1)

    def test_2(self):
        assert C(25000, 25000) == C(25000, 25000)

class TestUser:
    def test_0(self):
        for el in c_numbers:
            x1 = el[0]
            y1 = el[1]
            x2 = el[2]
            y2 = el[3]
            assert C(x1, y1) == C(x1, y1)
            assert C(x2, y2) == C(x2, y2)

class TestRandom:
    def test_0(self):
        x = randint(10**11, 10**12)
        y = randint(10**11, 10**12)
        assert C(x, y) == C(x, y)
    
    def test_1(self):
        x = randint(10**11, 10**12)
        y = randint(10**3, 10**4)
        assert C(x, y) == C(x, y)

    def test_2(self):
        x = randint(10**11, 10**12)
        y = randint(10**13, 10**14)
        assert C(x, y) == C(x, y)

    def test_3(self):
        x = randint(10**13, 10**14)
        y = randint(10**15, 10**16)
        assert C(x, y) == C(x, y)
