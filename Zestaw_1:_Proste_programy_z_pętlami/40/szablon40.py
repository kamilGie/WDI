# ====================================================================================================>
# Zadanie 40
# Proszę napisać funkcję, która sprawdza czy napis składający się z: liter a..z, operatorów
# dodawania i mnożenie oraz nawiasów jest poprawnym wyrażeniem arytmetycznym.
# ====================================================================================================>
# zakladam ze tylko nawiasy () innych powiedzmy ze nie bedzie
# zakladam tez ze kazda zmienna to max 1 litera


def Zadanie_40(napis) -> bool: ...


if __name__ == "__main__":
    from testy40 import odpal_testy

    Zadanie_40(str(input("Podaj napis: ")))

    # odpal_testy()
