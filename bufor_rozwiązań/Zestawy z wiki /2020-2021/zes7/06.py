# 6. Proszę napisać funkcję wstawiającą na koniec/początek listy nowy element. Do
# funkcji należy przekazać wskazanie na pierwszy element listy oraz wstawianą
# wartość.


class Node:
    def __init__(self, value = None):
        self.val = value
        self.next = None

def push_front(first, val):
    q = Node(val)
    q.next = first
    return q


def push_back(first, val):
    if first is None:
        return Node(val)

    p = first
    while p.next is not None:
        p = p.next
    
    p.next = Node(val)
    return first


