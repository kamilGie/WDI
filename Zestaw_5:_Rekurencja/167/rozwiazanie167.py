# ====================================================================================================>
# Zadanie 167
# Dane jest słowo składające się z liter alfabetu angielskiego. Słowo to tniemy na conajmniej
# dwa kawałki, tak aby każdy kawałek zawierał dokładnie jedną samogłoskę. Proszę napisać funkcję, która
# zwraca liczbę sposobów pocięcia słowa na kawałki.
# ====================================================================================================>


def Zadanie_167(slowo):
    """
    Tworzę tablicę pozycji samogłosek w napisie.
    Dla dwóch kolejnych pozycji mnożę ich odległość przez odległości następnych par.
    """
    samogloski = {"a", "e", "i", "o", "u"}
    pozycje = [i for i, char in enumerate(slowo) if char in samogloski]

    res = 1
    for i in range(1, len(pozycje)):
        res *= pozycje[i] - pozycje[i - 1]

    return res
