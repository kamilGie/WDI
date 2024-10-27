# 8. Dana jest niepusta lista, proszę napisać funkcję usuwającą co drugi
# element listy. Do funkcji należy przekazać wskazanie na pierwszy element
# listy. 
# WERSJA Z WARTOWNIKIEM

class Node:
    def __init__(self, value = None):
        self.val = value
        self.next = None



def push_front(first, val):
    q = Node(val)
    q.next = first.next
    first.next = q
    return first


def remove(p):
    curr = p

    while curr.next is not None:
        # if curr.next.next is None:
        #     return

        tmp = curr.next.next
        del curr.next
        curr.next = tmp

        if curr.next is not None:
            curr = curr.next



from helper_module import print_ll

first = Node()

push_front(first, 6)
push_front(first, 234)
push_front(first, 9)
push_front(first, 84)
push_front(first, 33)
# push_front(first, 353)

print_ll(first)
print()


remove(first)

print_ll(first)
