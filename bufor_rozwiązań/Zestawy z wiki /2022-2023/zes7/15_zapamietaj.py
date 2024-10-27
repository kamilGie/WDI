class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
#end class


def put_guardian(p):
    
    q = Node(0)
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


# Proszę napisać funkcję, która otrzymując jako parametr wskazujący na
# początek listy jednokierunkowej, usuwa z niej wszystkie elementy, w których
# wartość klucza w zapisie trójkowym ma większą ilość jedynek niż dwójek

# Z dodaniem wartownika na poczatku i koncu

def counting(n):
    jedynki = 0
    dwojki = 0

    while n > 0:
        if n % 3 == 1: jedynki += 1
        elif n % 3 == 2: dwojki += 1 
        n = n // 3 
    #end while
    return jedynki > dwojki
#end def 



def removing(p): # to jest wlasnie algo 
    p = put_guardian(p)
    q = p
    while p.next is not None:

        if counting( p.next.val ):
            p.next = p.next.next
             
        else:
            p = p.next 
    #end while
    return q 

    
#end def

T = [31,3,25,6,39,38,13,6,913,130,481]
p = create_linked_list_with_given_elements(T)
print_all(p)
print()
p = removing(p)
print_all(p.next)



