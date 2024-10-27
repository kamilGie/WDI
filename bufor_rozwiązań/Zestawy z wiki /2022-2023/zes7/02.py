# Zastosowanie listy odsyłaczowej do implementacji
# tablicy rzadkiej. Proszę napisać trzy funkcje:
# – inicjalizującą tablicę,
# – zwracającą wartość elementu o indeksie n,
# – podstawiającą wartość value pod indeks n.

# Tablica rzadka to tablica, ktora nie w kazdym indeksie ma wartosc ( tam gdzie nie ma jest None)

class Node:
    def __init__(self, idx: int, val, next = None):
        self.idx = idx
        self.val = val
        self.next = next
    #end def
    

def atIdx(ll: Node, idx: int): # ll - link list
    curr = ll.next if ll.val is None else ll
    
    while curr is not None:
        if curr.idx == idx:
            return curr.val
        #end if
        curr = curr.next 
    #end while
#end def


a = Node(0,23)
b = Node(39,42)
c = Node(55,23)

a.next = b
b.next = c 

print( '0: ', atIdx(a,23) )
print( '23: ', atIdx(a,23) )
print( '39: ', atIdx(a,39) )
print( '55: ', atIdx(a,55) )
