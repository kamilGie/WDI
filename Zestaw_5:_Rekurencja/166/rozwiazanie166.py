# ====================================================================================================>
# Zadanie 166
# Dwie osoby otrzymały ten sam ciąg liter. Każda osoba pocięła go na kawałki i pomieszała.
# Proszę napisać program, który otrzymując dwa zbiory kawałków odtwarza napis początkowy jeżeli odtworzenie
# to jest jednoznaczne lub stwierdza brak możliwości jednoznacznego odtworzenia napisu. Na przykład
# dla zbiorów (1) ab,cde,cfed,fab (2) abc,abc,def,fed odtworzony napis to: abcdefabcfed
# ====================================================================================================>
# return string jak sie da lub return False jak sie nie da


def buduj_prawo(T, T_nastepne, prawo, napis):
    if len(T) == 0 and prawo == "":
        return napis
    if prawo == "":
        return False

    for t in T:
        if t.startswith(prawo):
            T_copy = list(T)
            T_copy.remove(t)
            res = buduj_prawo(
                T_nastepne, T_copy, t[len(prawo) :], napis + t[len(prawo) :]
            )
            if res:
                return res

        if t in prawo:
            T_copy = list(T)  # Tworzymy kopię listy T
            T_copy.remove(t)  # Usuwamy element t z kopii
            res = buduj_prawo(
                T_copy, T_nastepne, prawo[len(t) :], napis + t[: len(prawo)]
            )
            if res:
                return res

    return False


def Zadanie_166(T1, T2):
    for t1 in T1:
        for t2 in T2:
            if t1.startswith(t2):
                T2_copy = list(T2)
                T1_copy = list(T1)
                T2_copy.remove(t2)
                T1_copy.remove(t1)
                res = buduj_prawo(T2_copy, T1_copy, t1[len(str(t2)) :], t1)
                if res:
                    return res
            if t2.startswith(t1):
                T1_copy = list(T1)
                T2_copy = list(T2)

                T1_copy.remove(t1)
                T2_copy.remove(t2)

                res = buduj_prawo(T1_copy, T2_copy, t2[len(t1) :], t2)
                if res:
                    return res

    return False


