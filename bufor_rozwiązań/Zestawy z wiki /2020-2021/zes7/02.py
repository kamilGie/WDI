# 2. Zastosowanie listy odsyłaczowej do implementacji tablicy rzadkiej. Proszę napisać trzy funkcje:
# – inicjalizującą tablicę,
# – zwracającą wartość elementu o indeksie n,
# – podstawiającą wartość value pod indeks n.

# WARTOWNIK


class Node:
    def __init__(self, val = None, i = -1):
        self.val = val
        self.next = None
        self.i = i


def init():
    a = Node()
    return a


def at(t, i):
    while t != None and t.i < i:
        t = t.next
    
    if t == None or t.i != i:
        return None
    
    return t.val


def set_val(t, i, val):
    while t.next != None and t.next.i < i:
        t = t.next
    
    if t.next != None and t.next.i == i:
        t.next.val = val
        return
    

    cell = Node(val, i)

    if t.next == None:
        t.next = cell
    else:
        cell.next = t.next
        t.next = cell            



def print_ll(ll):
    c = ll
    while c.next != None:
        print(c.next.i, end="\t")
        c = c.next
    print()

    c = ll
    while c.next != None:
        print(c.next.val, end="\t")
        c = c.next
    print()
    


l = init()

set_val(l,4,7)
set_val(l,6,1)
set_val(l,8,8)
set_val(l,234,11)
set_val(l,23,134)
set_val(l,8,4)

print_ll(l)


