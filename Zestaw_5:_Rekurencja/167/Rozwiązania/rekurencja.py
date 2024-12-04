# ====================================================================================================>
# Zadanie 167
# Dane jest słowo składające się z liter alfabetu angielskiego. Słowo to tniemy na conajmniej
# dwa kawałki, tak aby każdy kawałek zawierał dokładnie jedną samogłoskę. Proszę napisać funkcję, która
# zwraca liczbę sposobów pocięcia słowa na kawałki.
# ====================================================================================================>


def iloczyn_odleglosci_pozycji(pozycje):
    if len(pozycje) < 2: return 1
    return (pozycje[1] - pozycje[0]) * iloczyn_odleglosci_pozycji(pozycje[1:])


def Zadanie_167(slowo):
    samogloski = {"a", "e", "i", "o", "u"}
    pozycje_samogłosek = [i for i, char in enumerate(slowo) if char in samogloski]
    return iloczyn_odleglosci_pozycji(pozycje_samogłosek)
