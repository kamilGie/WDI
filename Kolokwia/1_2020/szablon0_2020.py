# Napis nazywamy wielokrotnym, jeżeli powstał przez n-krotne (n > 1) powtórzenie
# innego napisu o długości co najmniej 1.  Przykłady napisów wielokrotnych:
# ABCABCABC, AAAA, ABAABA.  Dana jest tablica T[N] zawierająca napisy.  Proszę
# napisać funkcję multi(T), która zwraca długość najdłuższego napisu wielokrotnego
# występującego w tablicy T lub wartość 0, jeżeli takiego napisu nie ma w tablicy.


def multi(T): ...


if __name__ == "__main__":
    from testy0_2020 import odpal_testy

    multi(int(input("Podaj T: ")))

    # odpal_testy()
