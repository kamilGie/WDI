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


# Proszę napisać funkcję, która sprawdza czy jedna lista zawiera się w
# drugiej. Do funkcji należy przekazać wskazania na pierwsze elementy obu
# list, funkcja powinna zwrócić wartość logiczną


def contain(p,q):

    def function(p,q):
        first_p = p
        first_q = q

        while p is not None:

            if q is None:
                return True

            if p.val == q.val:
                q = q.next 
                p = p.next
            
            else:
                p = p.next
                q = first_q
        #end while
        
        if p == None and q == None:
            return True

        return False
    #end def

    return function(p,q) or function(q,p)
#end def

T1 = [1,2,3,4,5,6,7,8,9]
T2 = [3,4,5]

# T1 = [1,2]
# T2 = [1,2]

p = create_linked_list( T1 )
q = create_linked_list( T2 )
print( contain(p,q) )