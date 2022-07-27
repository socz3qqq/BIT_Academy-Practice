import pytest
from random import randint
from linked_list import Node, mergeSort

def create_ll(list_elements):
    if len(list_elements) == 0:
        return None
    first = Node(list_elements[0])
    el = first
    for i in range(1, len(list_elements)):
        el.next = Node(list_elements[i])
        el = el.next
    return first
        
def ll_to_list(first):
    data = []
    while first is not None:
        data.append(first.val)
        first = first.next

    return data

class TestInitial:
    def test_0(self):
        data = [3, 2, 6]
        assert ll_to_list(mergeSort(create_ll(data))) == sorted(data)
    def test_1(self):
        data = [1,0]
        assert ll_to_list(mergeSort(create_ll(data))) == sorted(data)
    def test_2(self):
        data = [6, 5, 3, 9, 5, 4]
        assert ll_to_list(mergeSort(create_ll(data))) == sorted(data)
    def test_3(self):
        data = [3, -6, 0, 9, -15, 13, 19, -4]
        assert ll_to_list(mergeSort(create_ll(data))) == sorted(data)

        

class TestCorner:
    def test_0(self):
        data = []
        assert ll_to_list(mergeSort(create_ll(data))) == sorted(data)
    def test_1(self):
        data = [1]
        assert ll_to_list(mergeSort(create_ll(data))) == sorted(data)
    def test_2(self):
        data = [1, 2, 3, 4, 5, 6]
        assert ll_to_list(mergeSort(create_ll(data))) == sorted(data)
    def test_3(self):
        data = [-3, -2, 1, 2, 3, 4, 5, 6]
        assert ll_to_list(mergeSort(create_ll(data))) == sorted(data)
    def test_0(self):
        data = [6, 5, 4, 3, 2, 1]
        assert ll_to_list(mergeSort(create_ll(data))) == sorted(data)

class TestMini:
    def test_0(self):
        data = [randint(0, 100) for _ in range(20)]
        assert ll_to_list(mergeSort(create_ll(data))) == sorted(data)
    def test_1(self):
        data = [randint(0, 100) for _ in range(100)]
        assert ll_to_list(mergeSort(create_ll(data))) == sorted(data)
    def test_2(self):
        data = [randint(-100, 100) for _ in range(100)]
        assert ll_to_list(mergeSort(create_ll(data))) == sorted(data)
    def test_3(self):
        data = [randint(-10**4, 10**4) for _ in range(200)]
        assert ll_to_list(mergeSort(create_ll(data))) == sorted(data)

class TestMaxi:
    def test_0(self):
        data = [randint(-10**10, 10**10) for _ in range(50)]
        assert ll_to_list(mergeSort(create_ll(data))) == sorted(data)
    def test_1(self):
        data = [randint(0, 100) for _ in range(10**4)]
        assert ll_to_list(mergeSort(create_ll(data))) == sorted(data)
    def test_2(self):
        data = [randint(-100, 100) for _ in range(10**5)]
        assert ll_to_list(mergeSort(create_ll(data))) == sorted(data)
    def test_3(self):
        data = [randint(-10**4, 10**4) for _ in range(10**6)]
        assert ll_to_list(mergeSort(create_ll(data))) == sorted(data)