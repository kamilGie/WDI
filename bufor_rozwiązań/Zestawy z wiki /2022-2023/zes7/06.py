# Proszę napisać funkcję wstawiającą na koniec listy nowy element. Do
# funkcji należy przekazać wskazanie na pierwszy element listy oraz wstawianą
# wartość


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


def put_guardian(p):
    q = Node(None)
    q.next = p 
    return q 
#end def


def insert_at_end(p, number): # dodawanie na koniec rekurencyjnie  (WAZNE!! z wykorzystaniem guardiana)
    
    if p.next is None:
        k = Node(number)
        p.next = k
        return 
    
    else:
        return insert_at_end(p.next, number)
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



# Dlaczego wywolanie funkcji tak po prostu zmienia nam w globalnym programie?

#rekurencyjnie:
# p = None
# p = put_guardian(p)
# insert_at_end(p, 7)
# print_all(p.next)

#  iteracyjnie: # bez guardiana
# p = None
# p = insert_at_end_it(p,5)
# print_all(p)
