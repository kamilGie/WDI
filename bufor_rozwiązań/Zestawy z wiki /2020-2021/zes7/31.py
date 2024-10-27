# 31. Proszę napisać funkcję, która rozdziela listę na dwie listy. Pierwsza powinna zawierać klucze
# parzyste dodatnie, drugi klucze nieparzyste ujemne, pozostałe elementy należy usunąć z pamięci. Do
# funkcji należy przekazać wskaźniki na listę z danymi oraz wskaźniki na listy wynikowe. Funkcja
# powinna zwrócić liczbę usuniętych elementów.

from helper_module import Node, print_ll, arr2list, push_front

def divide(l):
    even_positive = Node()
    odd_negative = Node()

    counter = 0

    if l.val == None:
        l = l.next

    while l != None:
        if l.val > 0 and l.val % 2 == 0:
            push_front(even_positive, l.val)
        elif l.val < 0 and l.val % 2 == 1:
            push_front(odd_negative, l.val)
        else:
            counter += 1

        l = l.next

    print_ll(even_positive)
    print_ll(odd_negative)

    return counter


a = arr2list([3,-5,-23,342,42,65,23])
print(divide(a))