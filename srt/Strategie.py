BAZOWA = "bazowa"

# kontrowersyjny plik mozna by bylo strategie zimportowac poprostu skoro zawsze jest w tym samym miejscu
# a nie jakies dodatkowe importwy stringi na stringach i wgl, zgadzam sie ale nie mam czasu tego poprawiac


def domyslna():
    """
    Strategia domyslna strategii.

    Zwraca domyslna wartości dla strategii szablonów,rozwiązań i testów.
    Jesli kiedys jakas strategia bedzie powszechniej uzywana i lepsza wtedy
    strategia domyslna zmieni swoje strategie zwracane

    Returns:
        tuple: Krotka z trzema wartościami domyślnymi:
            - strategia szablonów (str): S
            - strategia rozwiązań (str): R
            - strategia testów (str): T
    """
    return "input_main", "importless", BAZOWA


# sama funkcja w rozwiązaniu
def meritum():
    return "input_main", "meritum", BAZOWA


def bazowa():
    return BAZOWA, BAZOWA, BAZOWA
