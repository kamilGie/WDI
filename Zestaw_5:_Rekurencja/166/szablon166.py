# ====================================================================================================>
# Zadanie 166
# Dwie osoby otrzymały ten sam ciąg liter. Każda osoba pocięła go na kawałki i pomieszała.
# Proszę napisać program, który otrzymując dwa zbiory kawałków odtwarza napis początkowy jeżeli odtworzenie
# to jest jednoznaczne lub stwierdza brak możliwości jednoznacznego odtworzenia napisu. Na przykład
# dla zbiorów (1) ab,cde,cfed,fab (2) abc,abc,def,fed odtworzony napis to: abcdefabcfed
# ====================================================================================================>
# return string jak sie da lub return False jak sie nie da


def buduj_prawo(T, T_nastepne, prawo, napis):

    if prawo == "":
        return napis if len(T) == 0 else False

    for i, t in enumerate(T):

        if t.startswith(prawo):
            nowa_lista = T[:i] + T[i + 1 :]
            nowe_prawo = t[len(prawo) :]
            res = buduj_prawo(T_nastepne, nowa_lista, nowe_prawo, napis + nowe_prawo)
            if res:
                return res

        elif t in prawo:
            nowa_lista = T[:i] + T[i + 1 :]
            nowe_prawo = prawo[len(t) :]
            res = buduj_prawo(nowa_lista, T_nastepne, nowe_prawo, napis)
            if res:
                return res

    return False


def Zadanie_166(T1, T2):
    for i, t1 in enumerate(T1):
        for j, t2 in enumerate(T2):
            if t1.startswith(t2) or t2.startswith(t1):
                nowa_T1 = T1[:i] + T1[i + 1 :]  # Kopia listy T1 bez elementu `t1`
                nowa_T2 = T2[:j] + T2[j + 1 :]  # Kopia listy T2 bez elementu `t2`

                if t1.startswith(t2):
                    res = buduj_prawo(nowa_T2, nowa_T1, t1[len(str(t2)) :], t1)
                else:
                    res = buduj_prawo(nowa_T1, nowa_T2, t2[len(t1) :], t2)

                if res:
                    return res

    return False


if __name__ == "__main__":
    from testy166 import odpal_testy

    # Zadanie_166(int(input('Podaj T1: ')), int(input('Podaj T2: ')))

    odpal_testy()
