class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
#end class


def put_guardian(p):
    q = p
    
    while p.next is not None:
        p = p.next

    a = Node(None)
    p.next = a 

    return q 
    
#end def


def print_all(p):
    while p.next is not None:
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


# Proszę napisać funkcję, która pozostawia w liście wyłącznie elementy
# unikalne. Do funkcji należy przekazać wskazanie na pierwszy element listy

# algo 
def uniq_ubik(p):
    first = p
    
    while p.next is not None:
        pointer = p.next
        tail = p
        
        while pointer is not None:
            
            if pointer.val == p.val:
                tail.next = pointer.next # przepiecie 
                pointer = pointer.next
                
            else:
                pointer = pointer.next
                tail = tail.next
        #end while

        p = p.next
    #end while
    return first 
#end def

T = [1,2,1,3,4,8,8,9,4,4,3,3,3,3,3,3,3,3,3,11,14,11,33,33,32,1,1,1,1,1,1,1,1,1,1,1,1,33,45,311,3251,13,13,13,13,13,13,2137,2137]
p = create_linked_list(T)
p = put_guardian(p)
p = uniq_ubik(p)
print_all(p)
