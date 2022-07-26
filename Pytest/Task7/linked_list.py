class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

def get_middle(first):
    pass

def merge(left, right):
    first = left
    while left.next is not None:
        l_prev = left
        left = left.next
        while left.val <= right.val:
            left = left.next
        while right.val< left.val:
            right = right.next
        l_prev.next = right
        tmp_right = right.next
        l_prev.next.next = left
        right = tmp_right
    if 


    return first

def mergeSort(first):
    if first is None or first.next is None:
        return first
    
    left = get_middle(first)
    right = left.next
    left.next = None
    sorted_L = mergeSort(first)
    sorted_R = mergeSort(right)

    return merge(sorted_L, sorted_R)

    
