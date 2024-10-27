class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
# end class


def put_guardian(p):
    q = Node(-float('inf'))
    q.next = p
    return q
# end def


def print_all(p):
    while p is not None:
        print(p.val, end=" ")
        p = p.next
# end def


def create_linked_list_with_given_elements(L):
    g = Node(float('inf'))
    p = g

    for elem in L:
        p.next = Node(elem)
        p = p.next

    return g.next
# end def


# 13. Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na pierwszy
# element listy o wartościach typu int, usuwającą wszystkie elementy, których
# wartość jest mniejsza od wartości bezpośrednio poprzedzających je
# elementów

# 6 -> 2 -> 1 -> 14 -> 7

def delete(p):
  if p.next is not None:
    delete(p.next)
    if p.next.val < p.val:
      p.next = p.next.next
    
# end def


# T = [15,2,14,7]
T = [5,3,4,2]
p = create_linked_list_with_given_elements( T )
print_all(p)
print()
print("----")
delete(p)
print_all(p)

