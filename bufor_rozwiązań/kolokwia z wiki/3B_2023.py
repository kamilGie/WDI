# OPIS METODY
# Funkcja ustala dla każdego węzła jego monotoniczność. Ustanawia
# 3 punkty kluczowe w nowej liście: strażnika i 2 miejsca puste
# (każdy rozpoczyna odpowiednio blok wyrazów rosnących, niemonotonicznych
# i malejących). Funkcja przepina węzły do wskazanych bloków zależnie od
# monotoniczności zawartych słów.


class Node:
    def __init__(self):
        self.val = None
        self.next = None


def check(s):  # 0 - rosnący, 1 - bez porządku, 2 - malejący
    l = len(s)
    if l == 1 or s[0] == s[1]:
        return 1  # edge cases: napis 1-literowy lub niemonotoniczny na początku
    lock = True if ord(s[0]) < ord(s[1]) else False
    for i in range(l - 1):
        if lock and s[i + 1] <= s[i]:
            return 1
        if not lock and s[i + 1] >= s[i]:
            return 1
    # dotarliśmy do końca bez zmiany monotoniczności
    if lock:
        return 0  # rosnący
    return 2  # malejący


def make_order(p):
    seg1 = Node()
    seg1.next = Node()
    seg2 = seg1.next
    seg2.val = ""
    seg2.next = Node()
    seg3 = seg2.next
    seg3.val = ""  # przygotowana odpowiednio lista - wskaźniki na wszystkie 3 elementy, lista w formie: seg1 -> seg2 -> seg3 -> None
    while p != None:
        variant = check(p.val)
        if (
            variant == 0
        ):  # wskazujemy węzeł początkowy bloku, do którego dopinamy węzeł wskazany przez p
            q = seg1
        elif variant == 1:
            q = seg2
        else:
            q = seg3
        tmp = q.next
        q.next = p
        p.next, p = tmp, p.next  # ta zmiana musi nastąpić równocześnie
    return seg1.next  # pomijamy 1szy pusty węzeł - naszego "wartownika"


# OBSŁUGA TESTOWANIA
def board_to_list(T):  # Przepisuje zadaną tablicę jako listę odsyłaczową
    p = Node()
    head = p
    l = len(T)
    for i in range(l):
        p.next = Node()
        p = p.next
        p.val = T[i]
    return head.next


def printlist(p):  # Wypisuje kolejne węzły listy
    while p != None:
        print(f"{p.val} -> ", end="")
        p = p.next
    return


# KONIEC OBSŁUGI TESTOWANIA

T = ["ala", "ola", "abel", "ula", "irys", "ewa", "sroka", "gips"]
p = board_to_list(T)
x = make_order(p)
printlist(x)

# Autor rozwiązania Piotr Polański
