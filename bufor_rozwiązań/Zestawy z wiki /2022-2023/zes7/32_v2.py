class Node:
    def __init_(self, pot,wsp,next = None):
        self.pot = pot
        self.wsp = wsp
        self.next = next
    #end def
#end class


# Listy wyjsciowe sie zmieniaja 
def subtract_polynomials(a,b):

    if b is None:
        return a 
    if a is None:
        b.wsp *= -1
        b.next = subtract_polynomials(a,b.next)
        return b
    if a.pot == b.pot:
        a.wsp -= b.wsp
        a.next = subtract_polynomials(a.next,b.next)
        return a
    else:
        if a.pot < b.pot:
            a.next = subtract_polynomials(a.next,b)
            return a
        
        else:
            b.wsp *= -1 
            b.next = subtract_polynomials(a,b.next)
            
    
