# Zad.3 Dany jest zbiór punktów płaszczyzny o współrzędnych będących liczbamicałkowitymi.7bior
# ten dany jest w postaci listy jednokierunkowej. Proszę funkcję, która rozdziela łańcuch na cztery
# łańcuchy zawierające punkty należące odpowiednio do l,ll,lll i lV ćwiartki układu współrzędnych,
# natomiast punkty leżące na osiach układu współrzędnych usuwa z pamięci. Proszę zadeklarować
# odpowiednie typy.


class Node:
    def __init__(self,x,y,next=None):
        self.x = x
        self.y = y
        self.next = next


def rozdziel(p):
    p = Node(None,None,p)
    q1 = Node(None,None)
    q2 = Node(None,None)
    q3 = Node(None,None)
    q4 = Node(None,None)
    
    while p.next is not None:
        a = None
        if p.next.x>0 and p.next.y>0:
            a = q1
        if p.next.x<0 and p.next.y>0:
            a = q2
        if p.next.x<0 and p.next.y<0:
            a = q3
        if p.next.x>0 and p.next.y<0:
            a = q4
        if a is None:
            p.next = p.next.next
        else:
            x = p.next
            p.next = p.next.next
            x.next = a.next
            a.next = x

    return q1,q2,q3,q4