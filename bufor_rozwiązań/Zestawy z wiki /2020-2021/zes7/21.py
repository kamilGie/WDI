# 21. Kolejne elementy listy o zwiększającej się wartości pola val nazywamy podlistą rosnącą. Proszę
# napisać funkcję, która usuwa z listy wejściowej najdłuższą podlistę rosnącą. Warunkiem usunięcia jest
# istnienie w liście dokładnie jednej najdłuższej podlisty rosnącej.


from helper_module import print_ll, Node, arr2list


def remove_the_lobgest_increasing_sublist(l):
    start = l
    l = l.next

    best = 0
    best_i = 0
    counter_best = 0

    start_i = 1
    leng = 1

    c = l
    i = 1
    while c.next != None:
        if c.next.val <= c.val:
            # print("end of increasing", i, leng)
            if best == leng:
                counter_best += 1
                
            if best < leng:
                best = leng
                best_i = start_i
                counter_best = 1
                # print("new best", start_i, leng)
        
            leng = 0
            start_i = i+1

        c = c.next
        i += 1
        leng += 1
    

    if best == leng:
        counter_best += 1
    if best < leng:
        best = leng
        best_i = start_i
        counter_best = 1

    # print()
    # print("no", counter_best, "best_start", best_i, "best_leng", best)
    # print()
    
    # do nothing if there are more than one the longest increasing sublist
    if counter_best > 1:
        return start
    
    
    # Find element one before starting index
    i = 1
    l = start
    while i < best_i:
        i += 1
        l = l.next
    
    # Find element one after ending index
    c = l.next
    while i < best_i+best:
        i += 1
        c = c.next
    
    # create shortcut from starting index to ending index
    l.next = c


    return start




a = arr2list([321,123,1,2,3,4,5,34,23,4,6,-1])
print_ll(a)
remove_the_lobgest_increasing_sublist(a)
print_ll(a)

print()
print()
print()

a = arr2list([321,1,2,3,4,5,34,23,4,6,-1])
print_ll(a)
remove_the_lobgest_increasing_sublist(a)
print_ll(a)

print()
print()
print()

a = arr2list([1,2,3,4,5,34,23,4,6,-1])
print_ll(a)
remove_the_lobgest_increasing_sublist(a)
print_ll(a)

print()
print()
print()

a = arr2list([1,34,23,4,6,9])
print_ll(a)
remove_the_lobgest_increasing_sublist(a)
print_ll(a)

