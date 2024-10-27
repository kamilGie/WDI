#  Dane są dwie niepuste listy, z których każda zawiera niepowtarzające
# się elementy. Elementy w pierwszej liście są uporządkowane rosnąco, w
# drugiej elementy występują w przypadkowej kolejności. Proszę napisać
# funkcję, która z dwóch takich list stworzy jedną, w której uporządkowane
# elementy będą stanowić sumę mnogościową elementów z list wejściowych.
# Do funkcji należy przekazać wskazania na obie listy, funkcja powinna
# zwrócić wskazanie na listę wynikową

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



def create_linked_list_with_given_elements(L):
  g = Node(None)
  p = g

  for elem in L:
    p.next = Node(elem)
    p = p.next
  
  return g.next



def add(p, z): #dodawanie rekurencyjne Nod'ow 

    if p.next is None:
        p.next = z
        z.next = None
        return 

    if p.next is not None:
        if p.next.val == z.val:
            return

        elif p.next.val > z.val:
            z.next = p.next
            p.next = z
            
        else:
            add(p.next, z)
    #end if 
#end def


#sprawdzamy czy wartosc 'val' znajduje sie w liscie
def is_present(g, val):

    if g.next is None:
        return False
    
    if g.next.val == val:
        return True
    elif g.next.val > val:
        return False
    else:
        return is_present(g.next, val)


def merge(p, q): # p - wskazanie 1 lista, q - wskazanie 2 lista

    k = Node(None) # guardian

    while q is not None:
        if is_present(p, q.val):
            tmp = q
            q = q.next
            add(k, tmp)
        else:
            q = q.next
    #end while
    return k.next 

#end def

p = create_linked_list_with_given_elements( [1,4,9,25,49,81] )
q = create_linked_list_with_given_elements( [4,81,23,3,76,100] )
x = merge(p, q) 
print_all(x)
        
        

    



