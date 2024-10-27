# Dana jest lista, który zakończona jest cyklem. Napisać funkcję, która zwraca wskaźnik do ostatniego elementu przed cyklem.
class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
#end class

def print_all(p):
    while p is not None:
        print(p.val, end = " ")
        p = p.next
#end def


def how_many_before_cycle(p):
    fast = p
    slow = p
    while 1:
        fast = fast.next.next
        slow = slow.next
        if fast == slow: break

    counter = 0
    fast = p
    while fast != slow:
        fast = fast.next
        slow = slow.next
        counter += 1 
    #end while
    return counter
#end def

def first_before_cycle(p):
    length = how_many_before_cycle(p) - 1

    if length < 0: return None

    tmp = p 
    while length > 0:
        length = length - 1
        tmp = tmp.next
    #end while
    return tmp.val

def cycle(p): # troszke uproszczona wersja
    fast = p
    slow = p
    while 1:
        fast = fast.next.next
        slow = slow.next
        if fast == slow: break

    counter = 0
    fast = p
    tail = None 
    while fast != slow:
        tail = fast
        fast = fast.next
        slow = slow.next
        counter += 1 
    #end while
    return tail.val
#end def

x = Node(1)
p = Node(2)
x.next = p
a = Node(3)
p.next = a
b = Node(4)
a.next = b
c = Node(5)
b.next = c
d = Node(6)
c.next = d
d.next = b


print( first_before_cycle(x) )
