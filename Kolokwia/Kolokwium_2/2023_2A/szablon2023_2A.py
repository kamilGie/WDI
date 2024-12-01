# ====================================================================================================>
# Zadanie 2A, 2024-01-04
# Ogród składa sie z 𝑁2
# jednakowych kwadratowych działek. Posiada on dwa wejścia, jedno w lewym
# górnym rogu od strony północnej, drugie w prawym dolnym rogu od strony południowej. Dokładnie
# na środkach niektórych działek ustawiono obustronne lustra pod katem 45° albo 135° tak, że patrzący
# przez wejście północne widzi osobę stojącą przy wejściu południowym.
# (tu jest zdjecie znajdjace sie w folderze)
# Do ogrodu przyszedł zły człowiek i przekręcił dwa lustra, każde o 90°. Proszę napisać funkcję
# napraw(ogrod) poprawiającą położenie luster, tak aby przywrócić widoczność pomiędzy oboma
# wejściami. Ogród jest reprezentowany jako dwuwymiarowa tablica wypełniona spacjami. Lustra
# feprezentowane sa odpowiednio jako znaki: / i \\ .
# ====================================================================================================>


def Zadanie_2A(ogrod): ...


if __name__ == "__main__":
    from testy2023_2A import odpal_testy

    ogrod = [
        ["/", "\\", ""],
        ["", "/", "\\"],
        ["", "", ""],
    ]

    Zadanie_2A(ogrod) # return -> [ ["\\", "\\", ""], ["", "\\", "\\"], ["", "", ""] ],


    # odpal_testy()
