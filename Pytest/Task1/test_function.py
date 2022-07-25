from function import square

def test_0():
    assert square(0) == 0
def test_1():
    assert square(1) == 1
def test_n1():
    assert square(-1) == 1
def test_100():
    assert square(100) == 10000
# Napisać cztery testy z dla funckji square dla 0, 1, -1 i 100