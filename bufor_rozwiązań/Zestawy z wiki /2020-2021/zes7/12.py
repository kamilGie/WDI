# 12. Zbiór mnogościowy zawierający napisy jest reprezentowany w postaci jednokierunkowej listy.
# Napisy w łańcuchu są uporządkowane leksykograficznie. Proszę napisać stosowne definicje typów
# oraz funkcję dodającą napis do zbioru. Do funkcji należy przekazać wskaźnik do listy oraz wstawiany
# napis, funkcja powinna zwrócić wartość logiczną wskazującą, czy w wyniku operacji moc zbioru
# uległa zmianie.

# WARTOWNIK (chyba)


from helper_module import print_ll, arr2list, Node

def diff(str1, str2):
    for i in range(min(len(str1), len(str2))):
        if str1[i] != str2[i]:
            return i
    
    if len(str1) == len(str2):
        return -1
    
    return min(len(str1), len(str2))

def insert(l, string):
    best = -1
    while l.next != None:
        r = diff(string, l.next.val)
        if r == -1:
            # print(1)
            return
        
        if r == len(l.next.val):
            l = l.next
            continue

        if r == len(string) or ord(string[r]) < ord(l.next.val[r]):
            # print(2)
            new = Node(string)
            new.next = l.next
            l.next = new
            return
        

        l = l.next
    
    if l.val == string:
        return
    
    l.next = Node(string)




a = arr2list(["aaba","bbbb","bbcccc","cccc"])

insert(a, "bbbbaaaa")
print_ll(a)

insert(a, "bbbbaaaa")
print_ll(a)

insert(a, "ccc")
print_ll(a)

insert(a, "dccccccc")
print_ll(a)

insert(a, "ac")
print_ll(a)

insert(a, "a")
print_ll(a)