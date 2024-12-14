<picture>
  <source srcset="../../srt/zbior_zadan/148.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_148.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_148.png" alt="zadanie 148">
</picture>

```python

def hetmany():
    def rek(K, i):
        # Jeśli osiągnięto ósmy wiersz, znaleziono poprawne rozwiązanie
        if i == 8:
            return 1
        wynik = 0
        # Próbujemy ustawić hetmana w każdej kolumnie bieżącego wiersza
        for x in range(8):
            # Sprawdzamy, czy pozycja jest bezpieczna
            bezpieczna_pozycja = True
            for j in range(i):
                # Sprawdź, czy hetman w kolumnie `x` nie jest w tej samej kolumnie lub na tej samej przekątnej
                if K[j] == x or abs(K[j] - x) == i - j:
                    bezpieczna_pozycja = False
                    break

            if bezpieczna_pozycja:
                K[i] = x  # Ustawiamy hetmana
                wynik += rek(K, i + 1)  # Rekurencja na kolejny wiersz
        return wynik

    return rek([0] * 8, 0)  # Tablica K przechowuje kolumny, w których są hetmany
```
# Opis Rozwiązania 

Szukamy ustawienia 8 hetmanów tak, aby żaden z nich nie atakował innego, wykorzystując rekurencję, i zwracamy liczbę takich ustawień.

<div align="center">
  <video src="https://github.com/user-attachments/assets/52ea29fa-d361-4962-b845-6e73047e5803" width="400" />
</div>



Program wizu w `Rozwiązania`
