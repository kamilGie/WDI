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


def create_linked_list(L):
  g = Node(None)
  p = g

  for elem in L:
    p.next = Node(elem)
    p = p.next
  
  return g.next
#end def



# Lista zawiera niepowtarzające się elementy. Proszę napisać funkcję do
# której przekazujemy wskaźnik na początek oraz wartość klucza. Jeżeli
# element o takim kluczu występuje w liście należy go usunąć z listy. Jeżeli
# elementu o zadanym kluczu brak w liście należy element o takim kluczu
# wstawić do listy


def zad11(p, key):
    q = p

    def put_guardian(p):
        t = Node( None )
        t.next = p 
        return t
    #end def


    def present(p, n):
        while p is not None:
            if p.val == n:
                return True
            #end if
            p = p.next
        #end while
        return False
    #end def


    def add(p, n):
        p = q
        while p.next is not None:
            p = p.next
        k = Node(n)
        p.next = k
        
    
    def delete(g, val):
        if g.next is None:
            return 
        
        if g.next.val == val:
            g.next = g.next.next
        
        else:
            delete(g.next, val)
    #end def 


    if present(p, key):
        p = put_guardian(p)
        delete(p, key)
        return p.next
    else:
        add(p, key)
        return p
#end def


T = [1,2,3,4,5,6]
p = create_linked_list(T)
x = zad11(p,7)
print_all(x)