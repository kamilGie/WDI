# 3. Dane są trzy listy jednokierunkowe uporządkowane rosnąco bez powtarzających się
# liczb. Proszę napisać funkcję która usunie w każdej liście elementy powtarzające się
# w trzech listach. Funkcja ma zwrócić liczbę usuniętych elementów.


def zadanie_kolos(p1,p2,p3):
    cnt = 0
    p1 = Node(None,p1)
    p2 = Node(None,p2)
    p3 = Node(None,p3)
    s1 = p1 
    s2 = p2 
    s3 = p3
    while p1.next is not None and p2.next is not None and p3.next is not None:
        if p1.next.value == p2.next.value == p3.next.value:
            p1.next = p1.next.next
            p2.next=p2.next.next
            p3.next=p3.next.next
            cnt+=1
        else:
            if p1.next.value <p2.next.value and p1.next.value< p3.next.value:
                p1 = p1.next
            if p2.next.value <p3.next.value and p2.next.value< p1.next.value:
                p2 = p2.next
            if p3.next.value <p1.next.value and p3.next.value< p2.next.value:
                p3 = p3.next
    return cnt