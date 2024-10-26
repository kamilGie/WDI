import os
import sys

srt_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Testy")
sys.path.append(srt_dir)
srt_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Rozwiazania")
sys.path.append(srt_dir)
srt_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Szablony")
sys.path.append(srt_dir)


BAZOWA = "bazowa"


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
    from Testy.Prime import Prime
    from Szablony.input_main import input_main
    from Rozwiazanie.importless import importless

    return input_main, Prime, importless


# sama funkcja w rozwiązaniu
def meritum():
    return "input_main", "meritum", BAZOWA


def bazowa():
    return BAZOWA, BAZOWA, BAZOWA
