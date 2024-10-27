from random import randint


def check(tab):
    for het1 in tab:
        for het2 in tab:
            if het1 == het2:
                continue

            if het1[0] == het2[0] or het1[1] == het2[1]:
                return False

            a = (het1[1] - het2[1]) / (het1[0] - het2[0])

            if a == 1.0 or a == -1.0:
                return False

    return True



def check2(tab):
    for y in range(len(tab)):
        for x in range(y+1, len(tab) ):
            w1, k1 = tab[y]
            w2, k2= tab[x]

            if w1 == w2 or k1 == k2:
                return False
            #end if

            quotient = (w2 - w1) / (k2 - k1)
            if quotient == -1.00 or quotient == 1.00:
                return False
            #end if

    return True



print(check([(26, 5), (2, 4)]))

print(check2([(87,1), (3, 4), (1, 6)]))