# ====================================================================================================>
# Zadanie A6, 17.01.2023
# Dana jest niepusta lista cykliczna, zbudowana z elementów zawierających pola val i next, której węzły
# przechowują liczby naturalne. Liczby przechowywane w liście spełniają warunek ”łączności”, tzn. dla każdego węzła ostatnia cyfra liczby jest identyczna z pierwszą cyfrą liczby z następnego węzła. Proszę napisać
# funkcję insert(p, n), która wstawia do listy wskazywanej przez wskaźnik p, liczbę n, metodą zastąpienia
# co najmniej dwóch elementów jednym zawierającym wstawioną liczbę. Po wstawieniu nowej liczby nadal
# zachowany powinien być warunek ”łączności”. Funkcja powinna zwrócić o ile skrócona została lista albo
# wartość 0 gdy elementu nie można wstawić do listy.
# Na przykład dla listy zawierającej elementy: 2023 31 17 703 37 707 72 29 902
# po wstawieniu liczby 303 lista może wyglądać następująco: 2023 303 37 707 72 29 902
# Funkcja powinna zwrócić wartość 2.
# ====================================================================================================>


def Zadanie_A6(): ...


if __name__ == "__main__":
    from Develop import stworz_zadanie

    Zadanie_A6()
    # stworz_zadanie([Zadanie_A6])
