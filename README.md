
# SRT-WDI 
## Szablony Startowe, Rozwiązania i Automatycznie Generujące się Testy do WDI na AGH
### 🔧 Używanie Projektu

Każdy folder z zadaniem składa się z trzech kluczowych plików:

1. `rozwiazanie.py` – plik z gotowym rozwiązaniem zadania.
2. `szablon.py` – plik zawierający szablon do wypełnienia własnym rozwiązaniem.
3. `testy.py` – plik zawierający testy jednostkowe, które sprawdzają poprawność funkcji napisanych w pliku `szablon.py`.

### 🧪 Jak testować swoje rozwiązania?

1. Otwórz plik `szablon.py` w folderze zadania i wypełnij rozwiazaniem zadania.
2. Odkomentuj funkcję `odpal_testy()`.
3. Uruchom plik `szablon.py`, a funkcja `odpal_testy()` przeprowadzi testy jednostkowe na Twoim kodzie i wyświetli wyniki.

### 🧱 Prototypy
Jeśli zadanie nie zostało jeszcze rozwiązane przez nikogo wcześniej, jest nazwane `prototyp.py`.
1. Po rozwiązaniu zadania na `prototyp.py` można stworzyć pełne zadanie, odkomentowując funkcję `stworz_zadanie` i przekazując w tablicy funkcje, które mają być objęte testami.
2. Funkcja `stworz_zadanie` automatycznie przygotuje testy na podstawie przekazanych funkcji. Poprosi również o podanie argumentów testowych, które Twoim zdaniem mogą być interesujące lub problematyczne.
3. Następnie utworzy folder zadania zawierający pliki: `rozwiazanie.py` oraz `szablon.py` na podstawie `prototyp.py`, a także `testy.py` na podstawie wcześniej wygenerowanych testów.

   

 [Szczegóły dotyczące używania projektu, prototypów i działania tutaj](#szczegóły-projektu)
 
---
### 🗿 Najwięksi współtwórcy:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<a href="https://github.com/kamilGie/WDI/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=kamilGie/WDI" alt="Najwięksi współtwórcy" />
</a>


## 🤝 Jak pomóc i zostać współtwórcą?

- Zalecam [***utworzenie forka***](https://github.com/kamilGie/WDI/fork) oraz samodzielne stworzenie zadania i zgłaszanie swoich zmian za pomocą pull requestów.
- Można również [dodać rozwiązanie zadania](https://github.com/kamilGie/WDI/new/solutions/bufor_rozwiązań), nie wychodząc z przeglądarki, korzystając z opcji "dodaj plik" w folderze bufor rozwiązań. W wolnym czasie będę z nich tworzył zadania. Szczegóły znajdziesz w [README folderu bufor rozwiązań](/bufor_rozwiązań).


### 💡 Możliwe Ulepszenia ### 
- ✏️ Stworzenie Zadania
- 🛠️ Poprawienie treści zadania, jeśli jest niejasna lub brakuje np. znaków potęgowania.
- 🔧 Ulepszanie testow poprzez komendy lub stworzeniej własnej [Szczegóły](#komendy)
- 🧠 Tworzenie Strategi Tworzenia Zadań [Szczegóły](#strategie)
  
SRT opiera się na **rozszerzaniu funkcjonalności**. Dzięki temu możesz dodawać nowe funkcje i strategie bez modyfikacji istniejącego kodu, co ułatwia wdrożenie bez potrzeby wiedzy o całym systemie i unika konfliktów.
### 🐛 Zgłaszanie błędów

- Błędy w rozwiązaniach, testach lub treściach można zgłaszać <a href="https://github.com/kamilgie/wdi/issues/new?labels=bug"> ****tutaj**** </a>

### 💬 Feedback

- Sam feedback na temat tego, jak się pracuje, w jakim kierunku można pójść oraz czego brakuje, również będzie mile widziany. [kontakt](http://www.gieras.pl).

---


# Szczegóły Projektu

<details>
  <summary> 🧪 Testowanie Zadania </summary>

## Testowanie Zadania
Przykładowy `szablon.py` wygląda tak: 
```python
# ====================================================================================================>
# Zadanie 1
# Proszę napisać program poszukujący trójkątów Pitagorejskich w których długość przekątnej
# jest mniejsza od liczby N wprowadzonej z klawiatury.
# ====================================================================================================>
# print(a,b,c)

def Zadanie_1(n): ...


if __name__ == "__main__":
    from testy01 import Testy01

    Zadanie_1(input('Podaj n: '))

    # Testy01.Uruchom()
```
### Na górze znajduje się opis zadania, funkcja do wypełnienia i przygotowany main.
Wypełniasz funkcję kodem, o który prosi opis zadania. Wyniki można zwracać lub wypisywać, choć zazwyczaj wypisujesz wynik za pomocą `print()`. Jeśli to nie będzie oczywiste, pod opisem zadania powinna być wskazówka od autora testów, jakiego sposobu zwracania wyników oczekuje. W tym przypadku widać, że boki trójkąta powinny być wypisywane kolejno, bez żadnych dodatkowych napisów.

Po tym, jak zrobisz zadanie i będziesz pewny jego poprawności, możesz odkomentować funkcję `Testy01.Uruchom()` i uruchomić program normalnie:
```python
# ====================================================================================================>
# Zadanie 1
# Proszę napisać program poszukujący trójkątów Pitagorejskich w których długość przekątnej
# jest mniejsza od liczby N wprowadzonej z klawiatury.
# ====================================================================================================>
# print(a,b,c)

def Zadanie_1(n):
    for a in range(1, n):
        for b in range(a, n):
            c = (a * a + b * b) ** 0.5
            if c.is_integer() and c <= n:
                print(a, b, c)

if __name__ == "__main__":
    from testy01 import Testy01

    Testy01.Uruchom()
```
### wynik takiego programu dalby taki wynik
<img width="1504" alt="Zrzut ekranu 2024-10-24 o 22 26 09" src="https://github.com/user-attachments/assets/666313c3-15ec-4697-955c-1e5de81e23d7">

### `test_Nr5_Zadanie_1_argumenty_20` oznacza:
- **5**. test
- Testuje funkcję **Zadanie_1**, czyli funkcję, która jest sprawdzana (to rozróżnienie jest przydatne w przyszłych zadaniach, gdzie testowanych będzie więcej funkcji).
- Test został uruchomiony z argumentem **20** (czyli Zadanie_1(20)).
  
Wynik testu wskazuje na błąd: widzimy komunikat `AssertionError: '3 4 5' not found in [''].` Oznacza to, że test oczekiwał pustego stringa `''`, a otrzymał `'3 4 5'`, co sugeruje, że wynik dla c = 5 został niepotrzebnie wypisany.

Po chwili namysłu i ponownym przeczytaniu treści zadania, można zauważyć, że warunek mówi o długości przekątnej mniejszej, niż liczba **N**. Kod należy poprawić i ponownie uruchomić testy z nową nadzieją.

### Czasami można spotkać się z takim przypadkiem:
 <img width="1165" alt="Zrzut ekranu 2024-10-24 o 22 57 49" src="https://github.com/user-attachments/assets/4fe66d52-766c-417a-87ab-738a38271137">
Widzimy, że mimo poprawnego wyniku mamy błędny test, ponieważ wypisujemy wynik w innym typie lub kolejności. W takim przypadku możemy:

- Cieszyć się poprawnym rozwiązaniem i pójść dalej.
- Zmienić typ lub format wyjścia na taki, jaki jest oczekiwany w teście.
- Zainteresować się pomocą w rozwijaniu projektu i za pomocą komendy dodać swoją funkcję wraz z jej rozwiązaniem do listy poprawnych odpowiedzi, aby inni użytkownicy mieli dobre testy dla takich samych wyników jak twój.

Więcej o tym, jak działa cały projekt w 


  
---
</details>

<details>
  <summary> ✏️  Tworzenie Zadania z prototypu  </summary>

## Tworzenie Zadania
### `stworz_zadanie()` 
Każdy prototyp zawiera funkcję `stworz_zadanie`, importowaną z pliku `Develop`. Funkcja `stworz_zadanie` przesyła funkcje, które chcemy by obejmowały testy oraz wchodziły w skład szablonu do wypelnienia. Wiec przykładowo wypełniony `prototyp` powinnien wygladać tak:
```python
# ====================================================================================================>
# Zadanie 0
# Stworz 2 funkcje jedna dodaje 2 liczby druga mnoży 2 liczby
# ====================================================================================================>

def dodaj(a, b):
    return a + b

def mnoż(a, b):
    return a * b

if __name__ == "__main__":
    from Develop import stworz_zadanie

    # stworz_zadanie([dodaj, mnoż])
```
Na tak wypełnionym prototypie możemy odkomentować `stworz_zadanie` i rozpocząć proces tworzenia.

<details>
    <summary> Dzialanie Developa </summary>
   
Plik `Develop` zbiera informacje o pliku, który importuje tę funkcję. Następnie zbiera następujące dane:
- `funkcje`, które chcemy testowac,
- `nr_zadania`, które rozwiązaliśmy bierze to z nazwy prototypu,
- `sciezke` do folderu w ktorym jest prototyp, aby `stworz_zadanie` mogło w tym samym stworzyć folder zadania,
- `strategie` rodzaj w jaki chcemy by testy zostaly napisane domyslnie jest to strategia bazowa. [Wiecej o strategi](#Strategie)

Nastepnie Develop do tego dodaje nową scieżkę importu, która znajduje się w [srt](srt) i tam wcześniej przygotowane zmienne przesyła na dalszy proces.
</details>


Funkcja `stworz_zadanie` znajduje się w katalogu [srt](srt) w pliku o nazwie `StworzZadanie`. Stamtąd funkcja utworzy folder zadania oraz trzy pliki: `rozwiazanie.py`, `szablon.py`, `testy.py`. To, jak pliki te są generowane, zależy od przekazanej `strategii`, jednak domyślnie stosowana jest strategia `bazowa`, która...

### `rozwiazanie.py` 
1. przepisuje prototyp usuwając tylko linijki, które mają w sobie `stworz_zadanie`
```python
# ====================================================================================================>
# Zadanie 0
# Stworz 2 funkcje jedna dodaje 2 liczby druga mnoży dwie liczby
# ====================================================================================================>

def dodaj(a, b):
    return a + b

def mnoż(a, b):
    return a * b

if __name__ == "__main__":

```
### `szablon.py` 
1. Przepisuje pierwsze linie, które są komentarzami, aby zostawić opis zadania wraz z ewentualnymi komentarzami twórcy zadania.
2. Następnie usuwa wszystkie linijki poza linijką zaczynającą się od `def FunkcjaKtoraTestujemy(`. Tę linijkę pozostawia i dopisuje trzy kropki, aby użytkownik wiedział, że te funkcje są do napisania.
3. Usuwa wszystkie linie do momentu napotkania bloku `if __name__ == "__main__":`.
4. Zapisuje import funkcji `odpal_testy`.
5. Zapisuje uruchomienie funkcji, które testujemy, wraz z dynamicznym wprowadzeniem nazw ich argumentów.
6. Zakomentowana metoda `odpal_testy()`, która będzie uruchamiać testy.

```python
# ====================================================================================================>
# Zadanie 0
# Stworz 2 funkcje jedna dodaje 2 liczby druga mnoży dwie liczby
# ====================================================================================================>

def dodaj(a, b): ...

def mnoż(a, b): ...

if __name__ == "__main__":
    from testy01 import odpal_testy

    dodaj(input('Podaj a: '), input('Podaj b: '))
    mnoż(input('Podaj a: '), input('Podaj b: '))

    # odpal_testy()
```

### `testy.py` 
1. Napisze potrzebne importy
2. Napisze funkcję `odpal_testy`, która będzie odpalać testy
3. Napisze funkcję `komenda` do odpalania komend [Wiecej o komendach](#Komendy)
4. Napisze nagłówek (deklaracje) klasy `Testy`.
5. Następnie dla każdej funkcji przekazanej do testowania:
6. Sprawdza liczbę argumentów, jaką funkcja przyjmuje.
7. Generuje `(10 * liczba argumentów + 1)` testów.
8. Jeśli liczba argumentów nie wynosi zero, prosi użytkownika o wpisanie argumentów testowych.
9. Jeśli argumenty wpisane przez użytkownika nie będą się zgadzały typem z argumentami funkcji, poprosi o ponowne wpisanie.
   <img width="930" alt="Zrzut ekranu 2024-10-25 o 15 05 53" src="https://github.com/user-attachments/assets/9d641167-62e8-4a80-b77e-80aed160cbe1">
10. Uruchamia funkcję z argumentami testowymi, monitorując jednocześnie wartości wypisywane przez `print` oraz wartości zwracane przez funkcję.
11. Jeśli funkcja nic nie zwróci, wynikiem zostanie to, co zostało przechwycone przez `print`. Jeśli funkcja zwróci inną wartość, to ona będzie wynikiem, a dane wypisane przez `print` zostaną zignorowane.
12. Z argumentów i wyniku napisze metodę testową o nazwie `test_numerTestu_funkcjaTestowalna_argument`.
```python
    def test_Nr1_dodaj_argumenty_2_2(self):
        wynik  = dodaj(2, 2)

        oczekiwany_wynik = [4]
        self.assertIn(wynik, oczekiwany_wynik)
```
10. Po napisaniu `liczba funkcji*( 10*liczba argumentow +1 )` metod testowych zakonczy klase Testy

<details>
   <summary>Pelny kod testy przykladu </summary>
   
```python 
import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon01 import dodaj, mnoż


def odpal_testy():
    suite = unittest.TestLoader().loadTestsFromTestCase(testy)
    unittest.TextTestRunner(verbosity=2).run(suite)


def komenda(k: str, *args, **kwargs):
    """
    Wykonuje zadaną komendę z przekazanymi argumentami.
    Dodanie własnej komendy ogranicza sie do dodania pliku z funkcja o tej samej nazwie
    w folderze glównym projektu src/Komendy
    Wiecej informacji o dodaniu wlasnej komendy jak i lista komend w ReadMe projektu

    Args:
        k (str): Komenda do wykonania.
        *args: Dodatkowe argumenty do komendy.
        **kwargs: Dodatkowe argumenty kluczowe do komendy.
    """
    sciezka_pliku_wykonalnego = os.path.abspath(sys.argv[0])
    srt_dir = os.path.join(
        os.path.dirname(sciezka_pliku_wykonalnego), "../../srt"
    )
    sys.path.append(srt_dir)
    nr_zadania = os.path.dirname(sciezka_pliku_wykonalnego)
    return importlib.import_module("WykonajKomende").wykonaj_komende(
        k, sciezka_pliku_wykonalnego, nr_zadania, *args, **kwargs
    )


class testy(unittest.TestCase):

    def test_Nr1_dodaj_argumenty_2_2(self):
        wynik  = dodaj(2, 2)

        oczekiwany_wynik = [4]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr2_dodaj_argumenty_14_123(self):
        wynik  = dodaj(14, 123)

        oczekiwany_wynik = [137]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr3_dodaj_argumenty_123_123(self):
        wynik  = dodaj(123, 123)

        oczekiwany_wynik = [246]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr4_dodaj_argumenty_123_1123(self):
        wynik  = dodaj(123, 1123)

        oczekiwany_wynik = [1246]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr5_dodaj_argumenty_12_3123(self):
        wynik  = dodaj(12, 3123)

        oczekiwany_wynik = [3135]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr6_dodaj_argumenty_12_3123(self):
        wynik  = dodaj(12, 3123)

        oczekiwany_wynik = [3135]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr7_dodaj_argumenty_-213_12312(self):
        wynik  = dodaj(-213, 12312)

        oczekiwany_wynik = [12099]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr8_dodaj_argumenty_2_2(self):
        wynik  = dodaj(2, 2)

        oczekiwany_wynik = [4]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr9_dodaj_argumenty_2_4(self):
        wynik  = dodaj(2, 4)

        oczekiwany_wynik = [6]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr10_dodaj_argumenty_2_-1(self):
        wynik  = dodaj(2, -1)

        oczekiwany_wynik = [1]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr11_dodaj_argumenty_2913_123(self):
        wynik  = dodaj(2913, 123)

        oczekiwany_wynik = [3036]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr12_dodaj_argumenty_324_56234(self):
        wynik  = dodaj(324, 56234)

        oczekiwany_wynik = [56558]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr13_dodaj_argumenty_21_35(self):
        wynik  = dodaj(21, 35)

        oczekiwany_wynik = [56]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr14_dodaj_argumenty_12_4(self):
        wynik  = dodaj(12, 4)

        oczekiwany_wynik = [16]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr15_dodaj_argumenty_0_0(self):
        wynik  = dodaj(0, 0)

        oczekiwany_wynik = [0]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr16_dodaj_argumenty_-1_-1(self):
        wynik  = dodaj(-1, -1)

        oczekiwany_wynik = [-2]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr17_dodaj_argumenty_1_1(self):
        wynik  = dodaj(1, 1)

        oczekiwany_wynik = [2]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr18_dodaj_argumenty_12_23(self):
        wynik  = dodaj(12, 23)

        oczekiwany_wynik = [35]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr19_dodaj_argumenty_2_1(self):
        wynik  = dodaj(2, 1)

        oczekiwany_wynik = [3]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr20_dodaj_argumenty_2_5(self):
        wynik  = dodaj(2, 5)

        oczekiwany_wynik = [7]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr21_dodaj_argumenty_21_1(self):
        wynik  = dodaj(21, 1)

        oczekiwany_wynik = [22]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr1_mnoż_argumenty_213_4512(self):
        wynik  = mnoż(213, 4512)

        oczekiwany_wynik = [961056]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr2_mnoż_argumenty_-4_12(self):
        wynik  = mnoż(-4, 12)

        oczekiwany_wynik = [-48]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr3_mnoż_argumenty_-3_-2(self):
        wynik  = mnoż(-3, -2)

        oczekiwany_wynik = [6]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr4_mnoż_argumenty_0_0(self):
        wynik  = mnoż(0, 0)

        oczekiwany_wynik = [0]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr5_mnoż_argumenty_-231_-2312(self):
        wynik  = mnoż(-231, -2312)

        oczekiwany_wynik = [534072]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr6_mnoż_argumenty_23_1(self):
        wynik  = mnoż(23, 1)

        oczekiwany_wynik = [23]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr7_mnoż_argumenty_231_213(self):
        wynik  = mnoż(231, 213)

        oczekiwany_wynik = [49203]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr8_mnoż_argumenty_21_-123(self):
        wynik  = mnoż(21, -123)

        oczekiwany_wynik = [-2583]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr9_mnoż_argumenty_52_1(self):
        wynik  = mnoż(52, 1)

        oczekiwany_wynik = [52]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr10_mnoż_argumenty_3213_-3212(self):
        wynik  = mnoż(3213, -3212)

        oczekiwany_wynik = [-10320156]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr11_mnoż_argumenty_-1_12(self):
        wynik  = mnoż(-1, 12)

        oczekiwany_wynik = [-12]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr12_mnoż_argumenty_3_212(self):
        wynik  = mnoż(3, 212)

        oczekiwany_wynik = [636]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr13_mnoż_argumenty_213_123(self):
        wynik  = mnoż(213, 123)

        oczekiwany_wynik = [26199]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr14_mnoż_argumenty_123_213(self):
        wynik  = mnoż(123, 213)

        oczekiwany_wynik = [26199]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr15_mnoż_argumenty_54_6435(self):
        wynik  = mnoż(54, 6435)

        oczekiwany_wynik = [347490]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr16_mnoż_argumenty_435_43(self):
        wynik  = mnoż(435, 43)

        oczekiwany_wynik = [18705]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr17_mnoż_argumenty_34_5345(self):
        wynik  = mnoż(34, 5345)

        oczekiwany_wynik = [181730]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr18_mnoż_argumenty_34_53(self):
        wynik  = mnoż(34, 53)

        oczekiwany_wynik = [1802]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr19_mnoż_argumenty_3_45(self):
        wynik  = mnoż(3, 45)

        oczekiwany_wynik = [135]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr20_mnoż_argumenty_3_3(self):
        wynik  = mnoż(3, 3)

        oczekiwany_wynik = [9]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr21_mnoż_argumenty_345_34(self):
        wynik  = mnoż(345, 34)

        oczekiwany_wynik = [11730]
        self.assertIn(wynik, oczekiwany_wynik)


```

</details>

Po stworzeniu trzech plików funkcja utworzy plik `prototypBackup.py`, aby bezpiecznie móc usunąć prototyp. Plik prototypBackup.py jest ignorowany przez .gitignore, więc nie będzie dodawany do głównego repozytorium. Został stworzony, aby w przypadku błędnego stworzenia zadania z różnych powodów móc utworzyć zadanie na nowo. Funkcja `stworz_zadanie` dba o to, by nie usunąć pliku `prototypBackup`, dzięki czemu można tworzyć zadania do momentu zadowolenia z efektu końcowego.

Na tym kończy się funkcja `stworz_rozwiazanie`. Jeśli jednak komuś nie podoba się sposób w jaki pliki `rozwiazanie.py`, `szablon.py`, `testy.py` są tworzone, chciałby dodać jakąś funkcjonalność lub inaczej tworzyć testy zawsze może stworzyć własną Strategię!

---
</details>

<details>
  <summary>🧠 Strategie</summary>

## Strategie
Strategie definiują sposób, w jaki będziemy tworzyć nasze zadania w projekcie. Umożliwiają ulepszanie plików z rozwiązaniami, szablonami i testami, poprzez nową logikę ich tworzenia. Aby użyc danej strategi, wystarczy do `stworz_zadanie` w prototypie dodać argument `strategia=` i nazwę strategi. Aktualną listę strategi znajdziesz w pliku [srt/Strategie](srt/Strategie). Każda z nich będzie funkcją, która definiuje jej nazwę i krótki komentarz na czym polega. 




### Podstawy Pisania Strategi
Dla przykladu zrobimy strategie w której 
- **`szablon`**  jest takie samo jak domyślnie, ale z datą rozwiazania na górze
- **`rozwiazania.py`**  nie zawiera opisu zadania, ani sekcji `main`, skupiamy całe meritum rozwiązania 
- **`testy.py`**  jest bazowe

  
Zaczniemy od szablonu w folderze [srt/Szablon](srt/Szablon), gdzie tworzymy nowy plik. W pliku klasa dziedziczy po jednej z klas w jej folderze albo po klasie bazowej. Klasa [srt/Bazowa.py](srt/Bazowa.py) jest abstrakcyjną klasą, z której będą pochodzić wszystkie klasy pochodne.

Klasa bazowa ma abstrakcyjną metodę `__str__`, w której musimy zwrócić wynik w postaci stringa, który później znajdzie się w pliku szablonu. Dla naszego pomysłu ta klasa będzie wyglądać tak:

```python
# srt/StrategieSzablonow/data_rozwiazania.py

#  Dziedzicze po klasie z pliku szablonów do której metody __str__  mógłbym coś dodać
from input_main import input_main 
from datetime import date

class Data(input_main): 
    def __str__(self):
        res = str(date.today().day)
        res += "\n"
        res += super().generuj()
        return res
```
LSP może zgłaszać, że jest to błędny import. Jednak przez to, że używam `sys.path`, a nie pakietów, program dopiero po uruchomieniu i stworzeniu folderu `__pycache__` poprawi import.

Dalej zajmiemy się `rozwiazanie.py`, gdzie dodam możliwe do użycia atrybuty klasy bazowej:

- **`linie_prototypu`** – linie w liście stringów, które reprezentują linie prototypu.
- **`nr_zadania`** – numer zadania, które zrealizowaliśmy.
- **`funkcje`** – funkcje, które zostały przekazane do testów szablonu i inne.
- **`sciezka`** – ścieżka folderu z zadaniem, które jest tworzone.
- **`nazwa_pliku`** – nazwa pliku ktorego wygeneruje domyslnie pochodzi od nazwy folderu, w którym znajduje się klasa. Na przykład, w folderze *Rozwiazanie*, klasy dziedziczące mają ten atrybut ustawiony na "rozwiazanie{`nr_zadania`}.py".

Wszystkich tych atrybutów można używać w klasach pochodnych od klasy bazowej, jednego z nich użyjemy co będzie widoczne w naszym przykładzie.

```python
# srt/StrategieRoziwazania/meritum.py

from bazowa import bazowa
import inspect

class Meritum(bazowa):
    def __str__(self):
        res = ""
        for funkcja in self.funkcje:
            res += inspect.getsource(funkcja)
        return res
```

Następnie z dwoma nowymi metodami mogę dodać swoją strategię w pliku [srt/Strategie.py](srt/Strategie.py). W pliku `Strategie.py` dodaję funkcję o nazwie, jaką chcę, aby miała moja strategia, a następnie w tej funkcji zwracam trzy klasy nazw metod, jakie chcę, by strategia użyła w kolejności: Szablony, Rozwiązania i Testy.
Jako, że nie zroblismy nowej klasy testów użyjemy strategii `testy_domyslne`, która zwraca nam na bieżąco aktualizowaną najlepszą strategię testów.

``` python
# rozwiazanie z sama funkcja a szablon z dniem
def testowa():
    from Szablony.data_rozwiazania import Data
    from Rozwiazanie.meritum import meritum

    return Data, meritum, testy_domyslne()

```

### Liczba plików tworzonych na podstawie strategii zależy od liczby zwracanych klas.

Jeśli użyjemy strategii zwracającej jedną klasę, zostanie stworzony jeden plik. Na przykład, `testy_domyslne()` to sama w sobie strategia, której możemy użyć do stworzenia zadania z samymi testami, bez rozwiązania i szablonu. Możemy także opracować strategię zwracającą 10 klas, co w efekcie utworzy 10 plików zadania.

Przykładowo, jeśli chcemy dodać plik zawierający wyjaśnienie autora zadania lub inne elementy, które nie są obecnie przewidziane, można to zrobić na dwa sposoby:
1. **Ustawienie nazwy pliku wewnątrz klasy** – przez przypisanie np. `self.res = "wyjasnienie"` (metoda mniej zalecana).
2. **Stworzenie dodatkowego folderu z odpowiednią nazwą** – wystarczy dodać folder o nazwie, którą chcemy nadać plikowi, oraz utworzyć w nim klasę dziedziczącą z klasy bazowej, która będzie zawierać odpowiednie treści. I powoli rozwijac kolejne typy plikow.

Z nowym plikiem możemy stworzyć strategię zwracającą 4 klasy metod, co spowoduje utworzenie 4 plików.

> **Należy pamiętać**, że strategie nie mogą być od siebie zależne; każda powinna być tworzona samodzielnie i działać logicznie niezależnie od innych.


  
Po zapisaniu można teraz uruchomić funkcję `stworz_zadanie` z argumentem strategii `testowa`, co pozwoli na stworzenie zadania na podstawie naszych klas. Przykładowe wywołanie funkcji wygląda następująco:
```python
stworz_zadanie([Zadanie_1], strategia="testowa")
```

Ograniczeniem strategii jest to, że nie przyjmuje argumentów innych niż `input` i jest to ustalenie stałe. Jednak, jeśli chcemy utworzyć zadanie, dodając pewne zmienne, możemy skorzystać z **komend**

</details>

<details>
  <summary> 💻 Komendy</summary>

## Komendy

<details>
   <summary> Działanie </summary>
   
W folderze [srt/Komendy](srt/Komendy) znajdują się pliki Python z komendami. Każdy plik zawiera **funkcje** o takiej samej nazwie, które wykonują odpowiednią komendę.

 przykładowa komenda wyglada tak. 
 ```python
# srt/Komendy/hello_name.py
def hello_name(imie):
    print("hello", imie)
```

Takiej komendy możemy użyć w `szablon.py`, importując z `testy` funkcję `komenda` i przekazując w pierwszym argumencie nazwę komendy, a następnie kolejne argumenty.
```python
# ====================================================================================================>
# Zadanie 1
# Wypisac swoje imie
# ====================================================================================================>

def Zadanie_1(): ...

if __name__ == "__main__":
    from testy01 import odpal_testy, komenda

    komenda("hello_name", "kamil")

    # Zadanie_1()
    # odpal_testy()
```
- w pliku `prototyp.py` importujemy z `Develop` funkcje komenda

Wynik odpalenia takiego programu będzie: `hello kamil`

Taka funkcjonalność pozwala w prosty sposób rozszerzać projekt o nowe komendy, umożliwiając ulepszanie testów, na przykład poprzez dodawanie dodatkowych testów lub wariacji poprawnego wyniku, a także wprowadzanie własnych preferencji, takich jak dodatkowe zachowanie po przejsciu testów na szablonie.

</details>

<details  >
  <summary><strong> SPIS KOMEND </strong> </summary>

### Legenda 
- `nazwaKomendy`, `mozliiwy do uzycia skrot`
- w budowie oznacza, że nie chce mi sie jej robić
- lokalna oznacza, że jej działanie nie moze wyjść poza lokalne repozytorium. By uniknąć przypadkow, że ktos nie spodziwal ze mu poleci [najlepsza  domyslna piosenka zwycieska](https://www.youtube.com/watch?v=CpeJiGDVMGo) po napisaniu szablonu
- Zapis `link_do_muzyki="https://www.youtube.com/watch?v=CpeJiGDVMGo` oznacza ze zmienna `link_do_muzyki` jest opcjonalna i domyslnie uzyjemy `https://www.youtube.com/watch?v=CpeJiGDVMGo`



### Spis 
  
  - `dodaj_testy`, `dt` - w budowie
    ```python
    # dodaje  dodatkowe testy 
    komenda("dodaj_testy", funkcja, ilosci_dodatkowych_testow)
     ```
     
  - `dodaj_wariancje`, `dw` - w budowie
    ```python
    # Do istniejacych juz wynikow testow funkcji dodaje kolejne mozliwe warienty na podstawie funkcji przeslanej
    komenda("dodaj_testy", funkcja)
     ```
  - `zwycieska_muzyka`,`zm` - w budowie, lokalna
    ```python
    # Do testow danego zadania dodaje muzyka po zaliczeniu testow w szablonie
    # imo must have 
    komenda("zwycieska_muzyka", link_do_muzyki="https://www.youtube.com/watch?v=CpeJiGDVMGo" )
     ```
 - `funkcja_input`,`fi` - w budowie
    ```python
    # szybkie testowanie funkcji na parametrach
    # dopoki nie przerwiesz bedziesz wpisywac input a komenda uzyje jej na funkcji i wypisze output
    komenda("szybka_funkcja", funkcja )
     ```
    
  - `StworzStruktureWDI`
    ```python
    # Nie bedzie wiecej uzywana i nawet nie da sie jej odpalic z poziomu plikow zadań - Takie zabezpieczenie
    # Ale dodaje jako taka ciekawostka oraz na przyszlosci do tworzenia struktur innych zadan
    komenda("StworzStruktureWDI")
     ```

</details>

<details  >
  <summary> Ogólne </summary>
   
### Argumenty
Funkcja `komenda` przyjmuje `"nazwaKomendy"`, `*args` oraz `**kwargs`, co pozwala na przesyłanie dowolnych argumentów zarówno w postaci argumentów pozycyjnych, jak i nazwanych. Aby ułatwić korzystanie, dodatkowo są dodawane dwa argumenty, jeśli komenda ich wymaga. Nie ma obowiązku ich podawania podczas wywołania komendy, są to: 
  - `nr_zadania`
  - `sciezka`
Więc komenda:
 ```python
# srt/Komendy/hello_zadanie.py
def hello_zadanie(nr_zadania, sciezka):# trzeba pamietac by nazwac te argumenty dokladnie tak 
    print("hello", nr_zadania, "from ", sciezka)
```
Może być wywołana w następujący sposób:
 ```python
# prototyp01.py
komenda("hello_zadanie")
```
Wynik takiej komendy to:

`hello 01 from  /Users/user/Desktop/projekty/WDI-RST/Zestaw_1:_Proste_programy_z_pętlami/prototyp01.py`



### skroty 

   Jesli komenda jest czesto używana może miec swój skrót w pliku `_skroty.py`, który tylko importuje komendę i ją odpala.
  ```python
  def hz(nr_zadania, sciezka):
    from hello_zadanie import hello_zadanie

    hello_zadanie(nr_zadania, sciezka)
   ```

### Zasady komend

- Każda ma mieć swój plik i ograniczać sie tylko do niego nawet jakby plik miałby mieć 20 linijek lub 100000 linijek.
- Każda komenda musi być w pełni niezależna i działać poprawnie samodzielnie, ale może wywoływać inne komendy w ramach swoich działań [zgodnie z wzorcem łańcucha zobowiązań]( https://refactoring.guru/pl/design-patterns/chain-of-responsibility)

</details>
</details>

---

## 🤓 Kilka slów od Autora
Projekt wydaje się być znacznie ambitniejszy, niż sugeruje problem, jakim jest WDI, oraz forma, w jakiej jest realizowany — czyli pisanie na kartce a program nie ma dzialac ma byc ladny. Powstał jednak z myślą o tym, że raczej nikt nie wykona wszystkich 200 zadań. By uniknac repozytoriów po 40 zadan i wspólnie stworzyć jakies większe.
Na początku nie sądziłem, że projekt rozwinie się do takiego stopnia. Uważam, że stał się bardziej systemem rozwiązań, szablonów i testów RST (stad nazwa), które planuje wykorzystać w innych zbiorach zadań lub przedmiotach. Tworzenie go dało mi fajny projekt w cv, fun i wiele doswiadczenia wiec nie istotne co sie dalej z nim stanie i tak bede z niego bardzo zadowolony. I tak wgl, projekt SRT nie tylko dlatego ze to skrot 
ale tez czytajac to  mozna poczuc podobienstwo do slowa asSeRT xddd co za legenda dajcie gwiazdke chce tego achigmenta za gwiazdki  plz ⭐⭐⭐



  
   
