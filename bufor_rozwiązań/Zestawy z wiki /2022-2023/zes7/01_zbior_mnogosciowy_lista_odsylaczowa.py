# Zaimplementuj zbiór mnogościowy liczb naturalnych korzystając ze
# struktury listy odsyłaczowej.
# - czy element należy do zbioru
# - wstawienie elementu do zbioru
# - usunięcie elementu ze zbioru

# Bedziemy tworzyc uporzadkowana liste ( strukture odsylaczowa )

class Node:
    def __init__(self):
        self.val = None
        self.next = None 
    #end def

#end Class ---------


def wypisz(zb):
    while zb != None:
        print(zb.val, end=" ")
        zb = zb.next
    #end while
    print()

#end def ----------




def member(el, zb): # czy element nalezy do zbioru, przekazujemy do funkcji element (type: int) i wskaźnik do struktury zbioru, wskaźnik na zbiór to wskaźnik na pierwszy element
    r = zb

    while r != None:
        if r.val == el:
            return True 

        r = r.next
    #end while

    return False
#end def ----------



def insert(el,zb):

    q = zb
    r = None # ogon
    while q != None and q.val < el:
        r = q
        q = q.next
    #end while
    # wykryjmy, który warunek nie został spełniony, przez który pętla się zakończyła

    # 1: jesli jakis element jest juz w łańcuchu to nic nie musimy robic, panowie, wychodzimy 
    if q != None and q.val == el:
        return zb

    # W kolejnych przypadkach musimy tworzyc nowy element 

    #wstawianie na początek, zbiór był pusty
    p = Node()
    p. val = el
    

    # 3: Jeśli wstawiam na poczatek łańcucha to r jest None, petla sie nie ruszyla, ale elementow moze byc wiecej, nie musialbyć pusty
    if r == None:
        p.next = zb
        return p # Zwracamy p, bo zawsze zwracamy wskazanie do naszego łańcucha, czyli do pierwszego elementu

    # Wstawianie w środku (r wskazuje element za ktorym wstawiamy, q element przed ktorym wstawiamy )
    # Wstawianie na końcu nie różni się niczym ( r wskazuje element za jakim wstawiamy, wskazuje na ostatni, a q to None)

    else:
        r.next = p
        p.next = q
        return zb

    

# Pusty zbiór to zmienna z wartością None




# Usuwanie elementu ze zbioru polega na:
# - jeśli elementu nie ma to wychodzimy 
# - jeśli jest to robimy przepięcie, z wyjątkiem 1 elementu, tam trzeba inaczej, nie wystarczy zrobic obejscia tylko nalezy zmodyfikowac 1 wskaźnik 

def remove(el,zb):

    q = zb
    r = None # ogon
    while q != None and q.val < el:
        r = q
        q = q.next
    #end while
    

    if q == None: return zb

    # if q != None and q.val != el:
    #     return zb

    if r == None:
        zb = zb.next
        return zb 
    
    else:
        r.next = q.next

#end def





x = None 
x = insert(2,x)
x = insert(3,x)
x = insert(5,x)
x = insert(7,x)

remove(2,x)

wypisz(x)
        
    
        





    
