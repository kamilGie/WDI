s = 0


# def sum_of_il(divisors: list, i: int, il: int):
#     global s
#     if i == len(divisors):
#         s += il
#         return
#     #end if
#     sum_of_il( divisors, i + 1, il)
#     sum_of_il( divisors, i + 1, il * divisors[i] )



def div(n):
    i = 2
    divs = []
    while n > 1:
        if n % i == 0:
            divs += [i]
            while n % i == 0:
                n = n // i
            #end while
        i += 1
        #end if
    #end while
    return divs



def zadanie(n):
    suma = 0

    def sum_of_il(divisors: list, i: int, il: int):
        nonlocal suma
        if i == len(divisors):
            suma += il
            return
        # end if
        sum_of_il(divisors, i + 1, il)
        sum_of_il(divisors, i + 1, il * divisors[i])
    #end def 2

    sum_of_il(div(n), 0, 1)

    return suma




n = 60
print( zadanie( n ) )

