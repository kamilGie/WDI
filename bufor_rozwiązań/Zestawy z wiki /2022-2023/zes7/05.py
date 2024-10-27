# 5. Proszę napisać funkcję, która rozdziela elementy listy odsyłaczowej do
# 10 list, według ostatniej cyfry pola val. W drugim kroku powstałe listy
# należy połączyć w jedną listę odsyłaczową, która jest posortowana
# niemalejąco według ostatniej cyfry pola val.

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
#end class


def print_ll(ll: Node):
    while ll is not None:
        print(ll.val, end=' ')
        ll = ll.next
    #end while
#end def


def split(ll: Node):
    curr = ll.next if ll.val is None else ll

    part = [ Node(None) for _ in range(10) ]
    lasts = [ n for n in part ] 

    while curr is not None:

        nex = curr.next
        i = curr.val % 10

        # lasts[i].next = curr 
        # lasts[i].next.next = None
        #  curr.next = None 

        lasts[i].next = curr
        lasts[i] = lasts[i].next
        lasts[i].next = None # curr.next = None 

        curr = nex
    #end while
    for l in part:
        print_ll(l)
        print()
#end def

def join(p): # troszke do poprawy 
    lists = [ None for _ in range(0,10) ]
    firsts = [ None for _ in range(0,10) ]
    first = p

    while p is not None:
        k = p
        p = p.next
        if lists[k.val % 10] == None:
            firsts[k.val % 10] = k  
            lists[k.val % 10] = k 
        else:
            lists[k.val % 10].next = k
            lists[k.val % 10] = k  
        
    #end while

    result = None 
    for i in range(9,-1,-1):
        if firsts[i] is not None:
            lists[i].next = result 
            result = firsts[i]
    return result 

#end def

a = Node(3)
b = Node(14)
c = Node(4)
a.next = b
b.next = c
