# 28. Dwie listy zawierają niepowtarzające się (w obrębie listy) liczby naturalne. W pierwszej liście
# liczby są posortowane rosnąco, a w drugiej nie. Proszę napisać funkcję usuwającą z obu list liczby
# występujące w obu listach. Do funkcji należy przekazać wskazania na obie listy, funkcja powinna
# zwrócić łączną liczbę usuniętych elementów.

# WARTOWNIK


from helper_module import Node, arr2list, print_ll


def remove_if_in_ordered_list(ordered, val):
    while ordered.next != None and ordered.next.val < val:
        ordered = ordered.next

    if ordered.next == None:
        return False

    if ordered.next.val == val:
        ordered.next = ordered.next.next
        return True


def remove_duplicates(ordered, not_ordered):
    start_ordered = ordered
    start_not_ordered = not_ordered

    counter = 0

    while not_ordered.next != None:
        if remove_if_in_ordered_list(start_ordered, not_ordered.next.val):
            not_ordered.next = not_ordered.next.next
            counter += 1
        
        else:
            not_ordered = not_ordered.next
        

    
    return counter*2
    

a = arr2list([1,2,3,4,5,6,7,8,9,14,423])
b = arr2list([1,4,23,53,234,423])
print(remove_duplicates(a, b))
print_ll(a)
print_ll(b)