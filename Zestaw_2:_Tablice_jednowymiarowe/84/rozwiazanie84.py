# ====================================================================================================>
# Zadanie 84
# Napis nazywamy wielokrotnym, jeżeli powstał przez n-krotne (n>1) powtórzenie innego
# napisu o długości conajmniej 1. Przykłady napisów wielokrotnych: ABCABCABC, AAAA, ABAABA.
# Dana jest tablica T[N] zawierająca napisy. Proszę napisać funkcję multi(T), która zwraca długość najdłuższego
# napisu wielokrotnego występującego w tablicy T lub wartość 0, jeżeli takiego napisu nie ma w tablicy.
# ====================================================================================================>


def multi(T):
    """
    Dla kazdego napisu iterujemy od połowy długości napisu w dół.
    W każdej iteracji tworzę podnapis od 0 do bieżącej pozycji iteracji,
    sprawdzam, czy powtarzając podnapis , otrzymam oryginalny napis.
    """
    res = 0
    for napis in T:
        n = len(napis)
        for i in range(n // 2, 0, -1):
            if n % i == 0 and napis[:i] * (n // i) == napis:
                res = max(res, i)
                break
    return res
