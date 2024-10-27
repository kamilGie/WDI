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


def create_linked_list_with_given_elements(L):
  g = Node(None)
  p = g

  for elem in L:
    p.next = Node(elem)
    p = p.next
  
  return g.next
#end def


# Dana jest lista, który zakończona jest cyklem. Napisać funkcję, która zwraca liczbę elementów w cyklu

def cycle(p):

    if p is None:
        return False

    counter = 0 
    fast = p
    slow = p
    
    while 1:

        fast = fast.next.next
        slow = slow.next

        if fast == slow: break

    #end while

    fast = fast.next.next
    slow = slow.next
    counter += 1 

    while fast != slow:
        counter += 1
        fast = fast.next.next
        slow = slow.next 
    #end while

    return counter 
#end def

def cycle2(p): #mozna troche poprawic i bedzie bardzo dobre rozwiazanie 
    slow_pointer = p
    fast_pointer = p 
    
    if fast_pointer.next is not None and fast_pointer.next.next is not None:
        fast_pointer = fast_pointer.next.next
        slow_pointer = slow_pointer.next

    while fast_pointer.next is not None and fast_pointer.next.next is not None:
        if fast_pointer == slow_pointer:
            cnt = 1
            slow_pointer = slow_pointer.next
            while slow_pointer is not fast_pointer:
                slow_pointer = slow_pointer.next
                cnt += 1
            #end while
            return cnt

        #end if
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next
    #end while
    return False
#end def


a = Node(1) 
b = Node(4)
a.next = b
c = Node(5)
b.next = c
d = Node(7)
c.next = d
e = Node(11)
d.next = e
f = Node(13)
e.next = f
f.next = c




print( cycle(a) ) 

