# 26. Proszę napisać funkcję, która sprawdza czy jedna lista zawiera się w drugiej. Do funkcji należy
# przekazać wskazania na pierwsze elementy obu list, funkcja powinna zwrócić wartość logiczną. 


from helper_module import print_ll, Node, arr2list


def is_sublist(glist, sublist):
    gstart = glist
    substart = sublist

    while glist != None:
        if sublist == None:
            return True

        if glist.val != sublist.val:
            gstart = gstart.next
            glist = gstart
            sublist = substart
        else:
            glist = glist.next
            sublist = sublist.next
        
    
    if glist == None and sublist == None:
        return True

    return False
        


def chect_if_one_list_is_in_another(start1, start2):
    if start1.val == None:
        start1 = start1.next
    if start2.val == None:
        start2 = start2.next

    l1 = start1
    l2 = start2


    return is_sublist(l1, l2) or is_sublist(l2, l1)



a = arr2list([1,3,4,6,7,8])
b = arr2list([6,7,8])
print(chect_if_one_list_is_in_another(a, b))