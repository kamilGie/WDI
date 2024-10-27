class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
#end class

# Proszę napisać funkcję, która otrzymując jako parametr wskazujący na
# początek listy dwukierunkowej, usuwa z niej wszystkie elementy, w których
# wartość klucza w zapisie binarnym ma nieparzystą ilość jedynek.

def how_many_ones(n):
    cnt = 0
    while n > 0:
        cnt += n % 2 
        n = n // 2
    #end while
    return cnt % 2 == 1 
#end def


def print_all(p):
    while p is not None:
        print(p.val, end = " ")
        p = p.next
#end def


def dec_to_bin(n):
    dig = 0
    number = 0

    while n > 0:
        number += ( n % 2 ) * ( 10 ** dig)
        dig += 1
    #end while
    return number
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
    k = Node( None )
    k.next = p
    return k 
#end def



# -----------

def odd_ones(n):
    counter = 0
    while n > 0:
        counter += n % 2 
        n = n // 2 
    #end while
    return counter % 2 == 1 
#end def 

def remove(p):

    if p is None: return None
    p = Node(None,p) # wartownik
    first = p
   

    while p.next is not None:
        if odd_ones( p.next.val ):
            p.next = p.next.next 
        else:
            p = p.next
    #end while
    return first.next
#end def 

T = [1,2,3,4,5,6,1]

p = create_linked_list(T)
p = remove(p)
print_all(p)

# ma usunac 1,2,4,7
# ma zostac 3,5,6
