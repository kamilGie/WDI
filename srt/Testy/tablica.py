from prime import prime

from typing import Callable, Tuple, Any


class tablica(prime):
    """dla funkcji modyfikujących tablicę in-place"""

    def wynik_wykonania_funkcji( self, funkcja: Callable, parametry: str) -> Tuple[Any, bool]:
        tablica = eval(parametry)
        funkcja(tablica)
        return tablica, False

    def metoda_zwracajaca_testow(self, NazwaTestu, numerTestu, zmienne, wynikWywolania):
        return f"""    def test_Nr{numerTestu:02}_{NazwaTestu}(self):
            tablica = {zmienne}
            {NazwaTestu}(tablica)
            self.assertEqual(tablica, { wynikWywolania })\n"""
