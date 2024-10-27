#Zaimplementuj zbiór mnogościowy liczb naturalnych korzystając ze
# struktury listy odsyłaczowej.
# - czy element należy do zbioru
# - wstawienie elementu do zbioru
# - usunięcie elementu ze zbioru



class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
#end class


def print_all(p):
    while p is not None:
        print(p.val)
        p = p.next
#end def

### ELEMENTY W ZBIORZE POSORTOWANE !


# new_val - liczba
def add(p, new_val): #dodawanie rekurencyjne

    if p.next is None:
        q = Node(new_val)
        p.next = q
        return

    if p.next is not None:
        if p.next.val == new_val:
            return

        elif p.next.val > new_val:
            q = Node(new_val)
            q.next = p.next 
            p.next = q
        else:
            add(p.next, new_val)
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
    


def delete(g, val):
    if g.next is None:
        return 
    
    if g.next.val == val:
        g.next = g.next.next
    
    elif g.next.val < val:
        delete(g.next, val)
    



g = Node(0)

add(g,7)

# add(g,3)
# add(g,1)
# print_all(g.next)
 
    

    
    
    