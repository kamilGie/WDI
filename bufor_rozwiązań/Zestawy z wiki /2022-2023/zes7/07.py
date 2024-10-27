# Proszę napisać funkcję usuwającą ostatni element listy. Do funkcji
# należy przekazać wskazanie na pierwszy element listy.


class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
#end class


def create_linked_list_with_given_elements(L):
  g = Node(None)
  p = g

  for elem in L:
    p.next = Node(elem)
    p = p.next
  
  return g.next
#end def


def put_guardian(p):
    q = Node(None)
    q.next = p 
    return q 
#end def


def insert_at_end_it(p, number): # dodawanie na koniec iteracyjnie # bez guardiana 
    q = p 

    if p is None:
        k = Node(number)
        return k
    
    else:
        while p.next is not None:
            p = p.next
        #end while

        k = Node(number)
        p.next = k 
        return q
#end def


def print_all(p):
    while p is not None:
        print(p.val)
        p = p.next
#end def


def delete_at_end(p):

    if p is None:
        return None

    p = put_guardian(p)
    first = p

    while p.next.next is not None:
        p = p.next 
    #end while

    p.next = None
    return first.next
#end def


p = create_linked_list_with_given_elements( [1,2] )
p = delete_at_end(p)
print_all(p)