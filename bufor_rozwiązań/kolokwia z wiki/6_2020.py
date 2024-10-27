"""
Dana jest definicja klasy, której obiekty stanowią elementy listy odsyłaczowej:
  class Node
    def init(self,val):
      self.val = val
      self.next = None

Zbiór mnogościowy liczb naturalnych reprezentowany jest przez listę o
uporządkowanych rosnąco elementach. Proszę napisać funkcję iloczyn(z1,z2,z3),
która przekształca 3 listy (zbiory) z1,z2,z3 w jedną listę (zbiór) zawierającą
elementy będące częścią wspólna zbiorów z1,z2,z3. Funkcja powinna zwrócić
wskazanie do listy wynikowej.

Komentarz: Zadanie jest tak proste, że nie wymaga przykładu ani danych testowych.
[komentarz też był częścią zadania. xD]
"""

# Bartłomiej Wiśniewski
# Szukam elementu występującego w zbiorze pierwszym i drugim, a następnie sprawdzam czy istnieje taki w zbiorze trzecim.
# Jeżeli tak to należy on do iloczynu mnogościowego tych trzech zbiorów

# Zakładam, że wejściowe listy nie mają strażnika na początku.
# Zakładam, że mogę zmieniać wejściowe listy. Jeżeli nie mogę to w liniach 32-36 należy skopiować wartość zamiast "przepinać" element listy.


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def iloczyn(l1, l2, l3):

    ans = Node(None)
    ans_c = ans

    while l1 != None and l2 != None:
        if l1.val > l2.val:
            l2 = l2.next
        elif l1.val < l2.val:
            l1 = l1.next
        else:
            while l3 != None and l3.val < l1.val:
                l3 = l3.next

            if l3 != None and l3.val == l1.val:
                # Tutaj zakładam, że mogę zmieniać wejściowe listy. Jeżeli nie mogę to należy skopiować wartość zamiast "przepinać" element listy.
                ans_c.next = l3
                ans_c = ans_c.next
                q = l3.next
                ans_c.next = None
                l3 = q

            l1 = l1.next
            l2 = l2.next
    return ans.next
