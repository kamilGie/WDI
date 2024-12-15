# ASRT-WDI 
## Automatyczne Szablony, Rozwiązania i Testy do WDI na AGH
### 🔧 Używanie Projektu

Każdy folder z zadaniem składa się z czterech składników:

1. **`README.md`** – zawiera treść zadania, **główne rozwiązanie** oraz, okazjonalnie, opis rozwiązania.
2. **`Rozwiązania`** – folder zawierający gotowe rozwiązania zadania.
3. **`szablon.py`** – plik zawierający szablon do wypełnienia własnym rozwiązaniem.
4. **`testy.py`** – plik z testami jednostkowymi.


### 🧪 Jak testować swoje rozwiązania?

Wypełnij plik `szablon.py` i uruchom go, odkomentowując funkcję `odpal_testy()`

https://github.com/user-attachments/assets/ad6d166e-bda7-4eca-a8cc-86d984913e0f

### 🌐 Wizualizacje Rozwiązań

Niektóre zadania zawierają wizualne wyjaśnienia algorytmów, które są hostowane w chmurze na stronie internetowej lub zrealizowane w Pygame, na przykład [Kolokwium 2022 A3](https://github.com/kamilGie/ASRT-WDI/tree/main/Kolokwia/Kolokwium_2/2022_A3), [160](https://github.com/kamilGie/ASRT-WDI/tree/main/Zestaw_5%3A_Rekurencja/160) czy [148](https://github.com/kamilGie/ASRT-WDI/tree/main/Zestaw_5%3A_Rekurencja/148) 

### 🌑 Czarny Motyw Zestawu
Każdy zestaw oraz każde zadanie zawiera plik `README` z opisem zadań. Jeśli masz ustawiony czarny motyw na GitHubie, zestaw ten będzie wyświetlany w ciemnej wersji.


### 🐛 Zgłaszanie Błędów
Błędy w rozwiązaniach, testach lub treściach zgłaszaj na <a href="https://github.com/kamilgie/ASRT-WDI/issues/new?labels=bug">****Issues****</a> lub <a href="https://gieras.pl/">****prywatnie****</a>.

### 🧱 Prototypy
Nierozwiązane zadania znajdują się w plikach `prototyp.py` i czekają na rozwiązanie. Po rozwiązaniu zadania można stworzyć pełne zadanie, automatycznie generując wszystkie pliki.


<details>
   
   <summary> Tworzenie Zadań na prototypie </summary>

1. Po rozwiązaniu zadania na `prototyp.py` można stworzyć pełne zadanie, odkomentowując funkcję `stworz_zadanie` i przekazując w tablicy funkcje, które mają być objęte testami.
2. Funkcja `stworz_zadanie` automatycznie przygotuje testy na podstawie przekazanych funkcji. Poprosi również o podanie argumentów testowych, które Twoim zdaniem mogą być interesujące lub problematyczne.
3. Następnie utworzy folder zadania zawierający pliki: `rozwiazanie.py` oraz `szablon.py` na podstawie `prototyp.py`, a także `testy.py` na podstawie wcześniej wygenerowanych testów.

https://github.com/user-attachments/assets/f3316918-a5e9-457f-8c2e-b4a5e5f0f27c



</details>


 
---

## Źródła rozwiązań 📚

Część rozwiązań została zaczerpnięta (*bezczelnie podkradziona*) z poniższych repozytoriów.  
Jestem ogromnie wdzięczny ich autorom za świetne prace, które bardzo pomogły! 

- 🌟 [WDI-2023](https://github.com/pawlowiczf/WDI-2023) - [Filip Pawłowicz](https://github.com/pawlowiczf)
- 🌟 [bit-algo-start-24-25-WDI](https://github.com/MarcinSerafin03/bit-algo-start-24-25-WDI) - [Marcin Serafin](https://github.com/MarcinSerafin03) ,[Ernest Szlamczyk](https://github.com/eszlamczyk) 
- 🌟 [WDI2020](https://github.com/Wisien999/WDI2020) - [Wisien999](https://github.com/Wisien999)  




### 🗿 Najwięksi współtwórcy:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<a href="https://github.com/kamilGie/ASRT-WDI/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=kamilGie/ASRT-WDI" alt="Najwięksi współtwórcy" />
</a>




# Szczegóły Projektu

<details>
  <summary> 🤝 Jak pomóc i zostać współtwórcą? </summary>

## 🤝 Jak pomóc i zostać współtwórcą?


- Zalecam [***utworzenie forka***](https://github.com/kamilGie/WDI/fork) oraz samodzielne stworzenie zadania i zgłaszanie swoich zmian za pomocą pull requestów.
- Można również [dodać rozwiązanie zadania](https://github.com/kamilGie/ASRT-WDI/new/main/bufor_rozwi%C4%85za%C5%84), nie wychodząc z przeglądarki, korzystając z opcji "dodaj plik" w folderze bufor rozwiązań. W wolnym czasie będę z nich tworzył zadania. Szczegóły znajdziesz w [README folderu bufor rozwiązań](/bufor_rozwiązań).


### 💡 Możliwe Ulepszenia ### 
- ✏️ Stworzenie Zadania
- 🛠️ Poprawienie treści zadania, jeśli jest niejasna lub brakuje np. znaków potęgowania.
- 🔧 Ulepszanie testow poprzez komendy lub stworzeniej własnej [Szczegóły](#komendy)
- 🧠 Tworzenie Strategi Tworzenia Zadań [Szczegóły](#strategie)
  
SRT opiera się na **rozszerzaniu funkcjonalności**. Dzięki temu możesz dodawać nowe funkcje i strategie bez modyfikacji istniejącego kodu, co ułatwia wdrożenie bez potrzeby wiedzy o całym systemie i unika konfliktów.
### 🐛 Zgłaszanie błędów

- Błędy w rozwiązaniach, testach lub treściach można zgłaszać <a href="https://github.com/kamilgie/ASRT-WDI/issues/new?labels=bug"> ****tutaj**** </a>

### 💬 Feedback

- Sam feedback na temat tego, jak się pracuje, w jakim kierunku można pójść oraz czego brakuje, również będzie mile widziany. [kontakt](http://www.gieras.pl).


</details>



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
    from testy01 import odpal_testy

    Zadanie_1(input('Podaj n: '))

    # odpal_testy()
```
### Na górze znajduje się opis zadania, funkcja do wypełnienia i przygotowany main.
Wypełniasz funkcję kodem, o który prosi opis zadania. Wyniki można zwracać lub wypisywać. Jeśli to nie będzie oczywiste, pod opisem zadania powinna być wskazówka od autora testów, jakiego sposobu zwracania wyników oczekuje. W tym przypadku widać, że boki trójkąta powinny być wypisywane kolejno, bez żadnych dodatkowych napisów.

Po tym, jak zrobisz zadanie i będziesz pewny jego poprawności, możesz odkomentować funkcję `odpal_testy()` i uruchomić program normalnie:
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
     from testy01 import odpal_testy

     odpal_testy()
```
### wynik takiego programu dalby taki wynik
<img width="1504" alt="Zrzut ekranu 2024-10-24 o 22 26 09" src="https://github.com/user-attachments/assets/666313c3-15ec-4697-955c-1e5de81e23d7">
  
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

Funkcja `stworz_zadanie` działa podobnie jak funkcja `print`. Można ją uruchomić bez dodatkowych parametrów, aby wygenerować domyślną strukturę plików: `rozwiazanie.py`, `testy.py` oraz `szablon.py`. 

### Modyfikacje 

Można modyfikować sposób, w jaki generowane są pliki, ustawiając argumenty nazw plików. Modyfikacje są podawane jako stringi, które określają  strategie, z jaką wygenerują się pliki. Dla podstawowego użycia projektu przydatne będą trzy modyfikacje:

```python
stworz_zadanie([dodaj, mnoż], testy="float")
```
- Stworzy testy, których wyniki będą zaokrąglone. Przydatne w zadaniach zwracających wartości typu `float`, gdzie wyniki mogą się różnić od ustawionego epsilonu.
  
```python
stworz_zadanie([dodaj, mnoż], testy="bez_kolejnosci")
```
- Stworzy testy, których wyniki będą w typie `set`. Przydatne w zadaniach, w których kolejność lub częstotliwość występowania wyników nie ma znaczenia.
```python
stworz_zadanie([dodaj, mnoż], testy="brak", szablon="brak")
```
- Nie stworzy pliku. Przydatne w zadaniach abstrakcyjnych, które nie są możliwe do przetestowania.

Dokładniej o modyfikacjach jest w sekcji [strategie](#Strategie)

<details>
   <summary> Domyślna konfiguracja plików </summary>

### `rozwiazanie.py` 
1. przepisuje prototyp do napotkania linijki main
```python
# ====================================================================================================>
# Zadanie 0
# Stworz 2 funkcje jedna dodaje 2 liczby druga mnoży dwie liczby
# ====================================================================================================>

def dodaj(a, b):
    return a + b

def mnoż(a, b):
    return a * b

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
1. Napisze  importy, funkcje oraz  nagłówek klasy `Testy`
2. Następnie dla każdej funkcji przekazanej do testowania:
3. Sprawdza liczbę argumentów, jaką funkcja przyjmuje.
4. Jeśli liczba argumentów nie wynosi zero, prosi użytkownika o wpisanie argumentów testowych.
5. Przetwarza input użytkownika, zmieniając go na argumenty według algorytmów.
6. Uruchamia funkcję z argumentami testowymi, monitorując jednocześnie wartości wypisywane przez `print` oraz wartości zwracane przez funkcję.
7. Jeśli funkcja nic nie zwróci, wynikiem zostanie to, co zostało przechwycone przez `print`. Jeśli funkcja zwróci inną wartość, to ona będzie wynikiem, a dane wypisane przez `print` zostaną zignorowane.
8. Z argumentów i wyniku napisze metodę testową o nazwie `test_numerTestu_funkcjaTestowalna_argument`.
```python
    def test_Nr1_dodaj_argumenty_2_2(self):
        wynik  = dodaj(2, 2)

        oczekiwany_wynik = [4]
        self.assertIn(wynik, oczekiwany_wynik)
```
9. Będzie powtarzać proces od punktów 3–8, aż do napotkania argumentu `stop` od użytkownika, który zakończy testy.

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

</details>

---

## Pisanie Testów


Po uruchomieniu funkcji `stworz_testy`, jeśli liczba argumentów przekazanych do testowania funkcji nie wynosi zero, program poprosi użytkownika o wpisanie argumentów testowych.

- Argumenty należy wpisywać, oddzielając je spacjami lub przecinkami.
  <img width="723" alt="Zrzut ekranu 2024-11-7 o 00 47 45" src="https://github.com/user-attachments/assets/ab503d2a-321c-494b-be07-0fe6a90e959c">

- Tablice wpisuje się, używając nawiasów kwadratowych, przy czym dozwolone jest zagnieżdżanie tablic dowolną ilość razy.
  <img width="724" alt="Zrzut ekranu 2024-11-7 o 00 02 27" src="https://github.com/user-attachments/assets/763ca1e4-913b-4f47-8a17-1abff1997f7e">

- Stringi należy podać w cudzysłowach, a także możliwe jest zagnieżdżanie cudzysłowów.
  <img width="724" alt="Zrzut ekranu 2024-11-7 o 00 07 02" src="https://github.com/user-attachments/assets/bb138ead-76c4-46c3-a529-2309042c9fa1">

- Jeśli argumenty wpisane będą się nie zgadzać, program poprosi o ponowne ich wprowadzenie.
  <img width="724" alt="Zrzut ekranu 2024-11-7 o 00 40 42" src="https://github.com/user-attachments/assets/61400923-4454-4aba-95c4-656b6eebc3e7">

Po stworzeniu odpowiedniej ilości testów, można zakończyć proces tworzenia testów, podając argument `stop`, co zakończy Twój wkład w tworzenie testów.

###  Finalizacja

Po stworzeniu trzech plików funkcja utworzy plik `prototypBackup.py`, aby bezpiecznie móc usunąć prototyp. Plik `prototypBackup.py` jest ignorowany przez `.gitignore`, więc nie będzie dodawany do głównego repozytorium. Został stworzony, aby w przypadku błędnego stworzenia zadania z różnych powodów móc utworzyć zadanie na nowo. Funkcja `stworz_zadanie` dba o to, by nie usunąć pliku `prototypBackup`, dzięki czemu można tworzyć zadania do momentu zadowolenia z efektu końcowego.

Na tym kończy się funkcja `stworz_zadanie`. Jeśli jednak komuś nie podoba się sposób w jaki pliki `rozwiazanie.py`, `szablon.py`, `testy.py` są tworzone, chciałby dodać jakąś funkcjonalność lub inaczej tworzyć testy zawsze może stworzyć własną Strategię!

---
</details>

<details>
  <summary>🧠 Strategie</summary>

## Strategie
Strategie definiują sposób, w jaki będziemy tworzyć nasze pliki w projekcie. Aktualna lista strategii znajduje się w folderach o odpowiednich nazwach: [srt/Szablon](srt/Szablon), [srt/Rozwiazania](srt/Rozwiazania), [srt/Testy](srt/Testy). Każda z nich jest klasą z krótkim komentarzem opisującym jej przeznaczenie i jest dostępna do użycia przez każdego twórcę zadania. 

Taki układ projektu pozwala na prosty rozwój i umożliwia rozwijanie go przez każdego, bez potrzeby znajomości całego systemu. Każdy może napisać własną klasę domyślną, która będzie następnie testowana w użyciu. Po tym, jak stanie się powszechniejsza, szybsza lub lepsza, zostanie ustawiona jako domyślna. Można również dodać klasę dodatkową, która obsługuje testy dla określonej puli zadań, dla których domyślne tworzenie zadania nie jest wystarczające.


### Podstawy Pisania Strategii

Stworzymy kilka przykładowych klas strategii:

- **`Data`** – Jest to strategia szablonu, która działa jak domyślna, z tą różnicą, że na górze pliku zostanie dodana data rozwiązania.
  
W folderze [srt/Szablon](srt/Szablon), tworzymy nowy plik z klasa o takiej samej nazwie. Klasa dziedziczy po jednej z klas w jej folderze albo po klasie bazowej. Klasa [srt/Bazowa.py](srt/Bazowa.py) jest abstrakcyjną klasą, z której będą pochodzić wszystkie klasy pochodne.

Klasa bazowa ma abstrakcyjną metodę `__str__`, w której musimy zwrócić wynik w postaci stringa, który później znajdzie się w pliku szablonu. Dla naszego pomysłu ta klasa będzie wyglądać tak:

```python
# srt/Szablon/data.py

#  Dziedzicze po klasie z pliku szablonów do której metody __str__  mógłbym coś dodać
from domyslne_s import domyslne_s 
from datetime import date

class data(domyslne_s):
""" na górze pliku zostanie dodana data rozwiązania. """
    def __str__(self):
        res = str(date.today().day)
        res += "\n"
        res += super().__str__()
        return res
```
Tak stworzoną klasę możemy już używać w funkcji `stworz_zadanie`, podając argument `szablon="data"`.

---

- **`meritum`** strategia rozwiazania  która koncentruje się wyłącznie na samym rozwiązaniu, pomijając opis zadania oraz sekcję `main`

 Aby dostosować sposób generowania pliku, można skorzystać z atrybutów klasy bazowej, które są dostępne w klasach pochodnych:

- **`linie_prototypu`** – lista stringów reprezentujących linie prototypu.
- **`nr_zadania`** – numer zadania, które rozwiązujemy.
- **`funkcje`** – funkcje przekazane do testów szablonu oraz inne pomocnicze funkcje.
- **`sciezka`** – ścieżka folderu, w którym znajduje się tworzone zadanie.
- **`nazwa_pliku`** – domyślna nazwa pliku, która pochodzi od nazwy folderu zawierającego klasę. Na przykład, w folderze *Rozwiazanie*, klasy dziedziczące mają atrybut ustawiony na "rozwiazanie{`nr_zadania`}.py".

Te atrybuty mogą być wykorzystywane w klasach pochodnych od klasy bazowej, a poniżej przedstawiamy przykład użycia jednego z nich.

```python
# srt/Rozwiazanie/meritum.py

from bazowa import bazowa
import inspect

class meritum(bazowa):
    """rozwiazania  która koncentruje się wyłącznie na samym rozwiązaniu, pomijając opis zadania oraz sekcję `main`"""

    def __str__(self):
        res = ""
        for funkcja in self.funkcje:
            res += inspect.getsource(funkcja)
        return res
```

Tak stworzoną klasę możemy już używać w funkcji `stworz_zadanie`, podając argument `rozwiazanie="meritum"`.

---

- **`float`**  strategia testów, która będzie zaokrąglać wyniki.

Strategie testów będą najtrudniejszych do napisania. Najczęściej będą nadpisywały metody już istniejących strategii i modyfikować sposób sprawdzania wyników testów.

Aby skutecznie zaimplementować taką strategię, będziemy musieli nadpisać dwie specjalnie wyodrębnione metody klasy `prime`:

```python
from prime import prime

DOKLADNOSCI = int(input("podaj dokładność, z jaką testy mogą zaokrąglać: "))


class float(prime):
    """testy beda zaaokroglac oczekiwany wynik"""

    def metoda_zwracajaca_testow_bez_kolejnosci(
        self, NazwaTestu, numerTestu, zmienne, wynikWywolania, zmienne_nazwa
    ):
        return f"""    def test_Nr{numerTestu:02}_{NazwaTestu}_argumenty_{'_'.join(zmienne_nazwa)}(self):
            wynik  = {NazwaTestu}({', '.join(map(str, zmienne))})

            self.assertAlmostEqual(wynik, { wynikWywolania }, places={DOKLADNOSCI})\n"""

    def metoda_nasluchujaca_testow_bez_kolejnosci(
        self, NazwaTestu, numerTestu, zmienne, wynikWywolania, zmienne_nazwa
    ):
        return f"""    def test_Nr{numerTestu:02}_{NazwaTestu}_argumenty_{'_'.join(zmienne_nazwa)}(self):
            f = io.StringIO()
            with redirect_stdout(f):
                {NazwaTestu}({', '.join(map(str, zmienne))})
            wynik = f.getvalue().strip()

            self.assertAlmostEqual(wynik, { wynikWywolania }, places={DOKLADNOSCI})\n"""
```
Klasa `prime` ma wiele metod specjalnie wyodrębnionych do nadpisywania.

---

> Strategie nie mogą od siebie zależeć i muszą być niezależne. Można je odpalić w dowolnej konfiguracji.


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
  - `zmien_testy`
    ```python
    # tworzy na nowo zadanie na bazie szablonu jako prototyp
    komenda("zmien_testy", [funkcje], testy="domyslna", rozwiazanie="domyslna", szablon="domyslna")
     ```

  
  - `dodaj_testy`, `dt` - w budowie
    ```python
    # dodaje  dodatkowe testy 
    komenda("dodaj_testy", funkcja, ilosci_dodatkowych_testow)
     ```
     
  - `dodaj_wariancje`, `dw` - w budowie
    ```python
    # Do istniejacych juz wynikow testow funkcji dodaje kolejne mozliwe warienty na podstawie funkcji przeslanej
    komenda("dodaj_wariancje", funkcja)
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
