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