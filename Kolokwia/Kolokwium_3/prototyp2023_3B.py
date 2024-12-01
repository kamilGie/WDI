# ====================================================================================================>
# Zadanie 3B, 2024-01-18
# Dana jest liczba odsyłaczowa, której elementy przechowują niepuste napisy składające się z małych
# liter alfabetu angielskiego. Proszę napisać funkcję make_order(p), która porządkuje elementy listy tak,
# aby na jej początku znalazły się napisy, w których kolejne litery są w porządku rosnącym, natomiast
# na końcu listy znalazły się napisy, w których litery są w porządku malejącym. Pomiędzy powstałymi
# grupami elementów należy wstawić elementy zawierające pusty napis. Do funkcji należy przekazać
# wskaźnik do pierwszego elementu listy, funkcja powinna zwrócić wskazanie do uporządkowanej listy.
# Na przykład lista: ala → ola → abel → ula → irys → ewa → sroka → gips
# Po uporządkowaniu może mieć postać: abel → gips → „” → irys → ala → ewa → „” → sroka → ola → ula
# Uwagi:
# • Czas na rozwiązanie zadania: 25 min.
# • Oceniane będą: czytelność (komentarze), poprawność, efektywność rozwiązań.
# Dodatkowe uwagi Garka podczas kolosa:
# • Nie można tworzyć nowych elementów poza wartownikiem (którego trzeba usunąć) i dwoma
# węzłami z pustymi stringami.
# • Można założyć, że mamy już zdefiniowane class Node.
# • Lista nie zawiera napisów składających się z jednej litery.
# ====================================================================================================>


def Zadanie_3B(): ...


if __name__ == "__main__":
    from Develop import stworz_zadanie

    Zadanie_3B()
    # stworz_zadanie([Zadanie_3B])
