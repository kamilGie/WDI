# 4. Proszę napisać funkcję, która dla podanej listy odsyłaczowej odwraca
# kolejność jej elementów.

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

# Działanie odwracanie
# 1. Jeśli nasza lista składa się tylko z jednego elementu to ją zwróc
# 2. W.p.p odwróć listę zaczynającą się w następnym elemencie
# 3. Na koniec odwróconej listy z kolejnego elementu doczep element aktualny

def reverse(p):
    if p.next is None:
        return p
    
    else:
        prev = reverse( p.next )
        q = prev
        
        while q.next != None:
            q = q.next
        #end while

        q.next = p
        p.next = None 
        return prev 

#end def

a = Node(2, None)
b = Node(1,a)
c = Node(3,b)
d = Node(7,c)

print_all(d)
x = reverse(d)
print('---')
print_all(x)