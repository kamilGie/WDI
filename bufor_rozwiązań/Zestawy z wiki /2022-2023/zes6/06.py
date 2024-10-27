# Dana jest tablica T[N]. Proszę napisać funkcję, która znajdzie niepusty, najmniejszy (w sensie
# liczebności) podzbiór elementów tablicy, dla którego suma elementów jest równa sumie indeksów tych elementów. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić sumę elementów znalezionego podzbioru.
# Na przykład dla tablicy: [ 1,7,3,5,11,2 ] rozwiązaniem jest liczba 10.

sum_i = 0
min_quantity = float('inf')
tab = []

def zad(T):
    
    def rek(T, sum_index, sum_elements, i=0 ,pom=0):

        global sum_i
        global min_quantity
        global tab

        if sum_index == sum_elements and sum_index != 0:
            
            if pom <= min_quantity and pom != 0:
                min_quantity = pom
                sum_i = sum_elements
                tab.append(sum_elements)
            #end def

            return True
        
        if i >= len(T):
            return False 

        rek(T, sum_index + i, sum_elements + T[i], i + 1, pom + 1)
        rek(T, sum_index, sum_elements, i + 1, pom)

    #end def

    rek(T, 0, 0)
    
#end def

T = [ 1,7,3,5,11,2 ] 
zad(T)
print(tab)

