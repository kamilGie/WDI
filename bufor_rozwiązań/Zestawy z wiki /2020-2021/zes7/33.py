# 33. Napis s1 poprzedza napis s2 jeżeli ostatnia litera s1 jest „mniejsza” od pierwszej litery s2. Według
# tej zasady rozmieszczono napisy w liście cyklicznej, na przykład:
# ┌─bartek──leszek──marek──ola──zosia─┐
# └───────────────────────────────┘
# Proszę napisać stosowne definicje typów oraz funkcję wstawiającą do listy napis z zachowaniem
# zasady poprzedzania. Do funkcji należy przekazać wskaźnik do listy oraz wstawiany napis, funkcja
# powinna zwrócić wartość logiczną wskazującą, czy udało się wstawić napis do listy. Po wstawieniu
# elementu wskaźnik do listy powinien wskazywać na nowo wstawiony element


from helper_module import Node, print_ll, arr2list

def insert(cycle, val):
    if cycle.val == None:
        cycle = cycle.next

    first = cycle

    while True:
        c = cycle
        while c.next != cycle:
            if ord(val[-1]) > ord(c.next.val[0]) or ord(c.val[-1]) > ord(val[0]):
                break
            c = c.next
        else:
            q = Node(val)
            q.next = cycle.next
            cycle.next = q
            return True



        cycle = cycle.next

        if cycle == first:
            return False
    


a = arr2list(["bartek", "leszek", "marek", "zosia"])
print_ll(a)
a.next.next.next.next.next = a.next
print(insert(a, "ola"))
# print(insert(a))
print_ll(a)