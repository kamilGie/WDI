# Dana jest niepusta lista reprezentująca liczbę naturalną. Kolejne
# elementy listy przechowują kolejne cyfry. Proszę napisać funkcję
# zwiększającą taką liczbę o 1



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


def create_link_list(T):
    p = Node( None )
    q = p

    for element in T:
        k = Node(element)
        p.next = k
        p = p.next 
    #end for
    return q.next
#end def

def put_guardian(p):
    k = Node(0)
    k.next = p
    return k

# global p
# def increase_number(p, beginn = p, end = None):
#     if p.next 
#     if p.next is not None:
#         increase_number(p.next, beginn, p)
    
#     if end != 
#     if p.val == 9:
#         p.val = 0
        

    
    
    
# Dana jest niepusta lista reprezentująca liczbę naturalną. Kolejne
# elementy listy przechowują kolejne cyfry. Proszę napisać funkcję
# zwiększającą taką liczbę o 1


def zad9(p):

    flag = False
    p = put_guardian(p)
    q = p
    
    def increase(p):
        nonlocal flag 

        if p.next is not None:
            increase(p.next)

        if p.val == 9 and flag is not True :
            p.val = 0

        elif p.val < 9 and flag is not True :
            p.val += 1 
            flag = True 
     

    #end def
    increase(p.next)

    if flag == False:
        q.val += 1 
        return q
    return q.next
    
#end def




T = [1,2,3,9]
p = create_link_list(T)

print_all(p)
print()

p = zad9(p)
print_all(p)

