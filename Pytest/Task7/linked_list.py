class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

def printList(first):
    while first is not None:
        print(first.val, end=" ")
        first = first.next

def get_middle(first):
    if first is None:
        return first
    middle = first
    last = first
    while last.next is not None and last.next.next is not None:
        middle = middle.next
        last = last.next.next

    return middle

def merge(left, right):
    if left.val > right.val:
        left, right = right, left
    merged = left
    left = left.next
    el = merged


    while left is not None and right is not None:
        if left.val <= right.val:
            el.next = left
            el = el.next
            left = left.next
            el.next = None
        else:
            el.next = right
            el = el.next
            right = right.next
            el.next = None

    if left is None:
        el.next = right
    else:
        el.next = left

    return merged

def mergeSort(first):
    if first is None or first.next is None:
        return first
    
    left = get_middle(first)
    right = left.next
    left.next = None
    sorted_L = mergeSort(first)
    sorted_R = mergeSort(right)

    return merge(sorted_L, sorted_R)



