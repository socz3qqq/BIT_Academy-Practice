import pytest
from function import count_chars

# Napisać testy dla funkcji count_chars za pomocą
# markera "parametrize"

@pytest.mark.parametrize("str, expected",[("abbccca", [2, 2, 3]), ("aaaaa", [5, 0, 0])])
class TestMini:
    def test_0(self, str, expected):
        assert count_chars(str) == expected

@pytest.mark.parametrize("str, expected", [("aaaaaaaaaaaaaaaaaabbbbbbbbbbcccccccccc", [18, 10, 10]),
                                            ("abababababababababcababababababababab", [18, 18, 1]),
                                            ("cbacbacbacbacbacbacbacbacbacbacbacbacbacba", [14, 14, 14])])
class TestMaxi:
    def test_0(self, str, expected):
        assert count_chars(str) == expected
    
# Funkcja count_chars zwraca trzyelementową tablicę
# która zawiera odpowiednio liczbę wystąpień znaku 'a', 'b' i 'c'