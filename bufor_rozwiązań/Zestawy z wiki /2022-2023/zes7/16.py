# Proszę napisać funkcję, która otrzymując jako parametr wskazujący na
# początek listy jednokierunkowej, przenosi na początek listy te z nich,
# które mają parzystą ilość piątek w zapisie ósemkowym


class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next 
#end class



def wypisz(p):
    while p is not None:
        print(p.val, end = " ")
        p = p.next 
    #end while
#end def



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



def number_of_fives_even( n ):
    cnt = 0

    while n > 0:
        if n % 8 == 5: cnt += 1
        n = n // 8 
    #end while
    
    return cnt % 2 == 0
#end def




def move(p):
    g = Node(None, p) # guardian
    # p = g nie dawaj 
    while p.next is not None:
        
        if number_of_fives_even( p.next.val ):

            q = p.next # wskazanie na element, ktory wycinamy
            p.next = p.next.next 

            q.next = g.next # wstawianie na poczatek
            g.next = q # - || -

        else:
            p = p.next

    #end while
    return g.next
#end def


p = Node(2)
add(p, 3)
add(p, 5)
add(p, 7)
add(p, 11)

wypisz(p)
p = move(p)
print()
wypisz(p)






