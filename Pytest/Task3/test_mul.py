from cmplex import C
from random import randint

# Napisać testy sprawdzające mnożenie liczb zespolonych
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
        assert C(0, 0) * C(1, 1) == C(0, 0)
        
    def test_1(self):
        assert C(0, 1) * C(-1, -1) == C(1, -1)

    def test_2(self):
        assert C(2, 8) * C(1, -3) == C(26, 2)

class TestUser:
    def test_0(self):
        for el in c_numbers:
            x = C(el[0], el[1])
            y = C(el[2], el[3])
            x_res = x.x*y.x - x.y*y.y
            y_res = x.x*y.y + x.y*y.x
            assert x * y == C(x_res, y_res)

class TestRandom:
    def test_0(self):
        x = C(randint(10**11, 10**12), randint(10**11, 10**12))
        y = C(randint(10**11, 10**12), randint(10**11, 10**12))
        x_res = x.x*y.x - x.y*y.y
        y_res = x.x*y.y + x.y*y.x
        assert x * y == C(x_res, y_res)
    def test_1(self):
        x = C(randint(10**11, 10**12), randint(-10**12, 10**11))
        y = C(randint(-10**12, -10**11), randint(-10**12, -10**11))
        x_res = x.x*y.x - x.y*y.y
        y_res = x.x*y.y + x.y*y.x
        assert x * y == C(x_res, y_res)
    def test_2(self):
        x = C(randint(10**12, 10**13), randint(10**12, 10**13))
        y = C(randint(10**12, 10**13), randint(10**12, 10**13))
        x_res = x.x*y.x - x.y*y.y
        y_res = x.x*y.y + x.y*y.x
        assert x * y == C(x_res, y_res)
    def test_3(self):
        x = C(randint(10**13, 10**14), randint(10**13, 10**14))
        y = C(randint(10**13, 10**14), randint(10**13, 10**14))
        x_res = x.x*y.x - x.y*y.y
        y_res = x.x*y.y + x.y*y.x
        assert x * y == C(x_res, y_res)
