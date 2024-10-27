class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
#end class


def put_guardian(p):
    q = Node(None)
    q.next = p 
    return q 
#end def


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



# 14. Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na pierwszy
# element listy o wartościach typu int, usuwającą wszystkie elementy, których
# wartość dzieli bez reszty wartość bezpośrednio następujących po nich
# elementów. 


def remove(p):

    if p == None or p.next is None:
        return p
    
    x, y = p.val, p.next.val

    if y % x == 0:
        return remove(p.next) # nie chcemy zachowywac tego elementu wiec zwracamy remove(p.next)
    #end if
    
    p.next = remove(p.next)
    return p

#end def


p = create_linked_list([6,2,2,4])
print_all(p)
print()
p = remove(p)
print_all(p)




