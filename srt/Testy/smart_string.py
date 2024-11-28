from prime import prime


class smart_string(prime):
    def przetwarzaj_wejscie(self, wejscie):
        """
        Przetwarza wejście w formie tekstowej na strukturę danych (listę), obsługując zagnieżdżone tablice.

        Args:
            wejscie (str): Tekstowe wejście do przetworzenia, zawierające argumenty i tablice.

        Returns:
            list: Lista przetworzonych argumentów, gdzie tablice są reprezentowane jako zagnieżdżone listy.
        """
        print(wejscie)
        return [wejscie]
