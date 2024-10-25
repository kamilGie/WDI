
# Szablony Startowe, Rozwiązania i Automatycznie Generujące się Testy do WDI na AGH
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
Jeśli zadanie nie zostało jeszcze rozwiązane przez nikogo wcześniej, jest uznawane za prototyp.
1. Po rozwiązaniu zadania na `prototyp.py` można stworzyć pełne zadanie, odkomentowując funkcję `stworz_zadanie` i przekazując w tablicy funkcje, które mają być objęte testami.
2. Funkcja `stworz_zadanie` automatycznie przygotuje testy na podstawie przekazanych funkcji. Poprosi również o podanie argumentów testowych, które Twoim zdaniem mogą być interesujące lub problematyczne.
3. Następnie utworzy folder zadania zawierający pliki: `rozwiazanie.py` oraz `szablon.py` na podstawie `prototyp.py`, a także `testy.py` na podstawie wcześniej wygenerowanych testów

   

 [Szczegóły dotyczące używania projektu, prototypów i działania tutaj](#Szczegóły)
 
---
### 🗿 Najwięksi współtwórcy:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<a href="https://github.com/kamilGie/WDI/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=kamilGie/WDI" alt="Najwięksi współtwórcy" />
</a>

## 🤝 Jak pomóc i zostac współtwórcą?

- Zalecam [***Utwórzyć fork***](https://github.com/kamilGie/WDI/fork) i zgłaszanie swoich zmian za pomocą pull requestów. Dzięki temu staniesz się widocznym współtwórcą projektu. 
- Można też wysłać mi kody bezpośrednio [kontakt tutaj](http://www.gieras.pl).

### 💡 Możliwe poprawki ### 
- ✏️ Stworzenie Zadania [Szczegóły](#Szczegóły-Projektu)
- 🛠️ Poprawienie treści zadania, jeśli jest niejasna lub brakuje np. znaków potęgowania.
- 🔧 Ulepszanie testow poprzez komendy [Szczegóły](#komendy)
- 💻 Stworzenie wlasnej komendy [Szczegóły](#komendy)
- 🧠 Tworzenie/Ulepszanie Strategi Tworzenia Zadań [Szczegóły](#Strategie)

### 🐛 Zgłaszanie błędów

- Błędy w rozwiązaniach, testach lub treściach  mozna zgłaszać <a href="https://github.com/kamilgie/wdi/issues/new?labels=bug"> ****tutaj**** </a>

### 💬 Feedback

- Sam feedback na temat tego, jak się pracuje, w jakim kierunku można pójść oraz czego brakuje, również będzie mile widziany. [kontakt](http://www.gieras.pl).

---


# Szczegóły Projektu

<details>
  <summary> 🧪 Testowanie Zadania </summary>

## Testowanie Zadania
Przykladowy `szablon.py` wyglada tak 
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

Po chwili namysłu i ponownym przeczytaniu treści zadania, można zauważyć, że warunek mówi o długości przekątnej mniejszej niż liczba **N**. Kod należy poprawić i ponownie uruchomić testy z nowa nadzieją

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
W kazdym prototypie mamy funkcje `stworz_zadanie` importowana z  pliku `Develop`. Plik `Develop` zbiera informacje o pliku która ja importuje a funkcja `stworz_zadanie` wysyla
- `funkcje` ktore chcemy testowac
- `nr_zadania` ktore rozwiązaliśmy (bierze to z nazwy prototypu)
- `sciezke` do folderu w ktorym jest prototyp
- `strategie` rodzaj w jaki chcemy by testy zostaly napisane domyslnie jest to strategia bazowa. [Wiecej o strategi](#Strategie)

te zmienn odbiera inna  funkcjia `stowrz_zadanie` ktora znajduje sie w katalogu skrypty w  katalogu glownym projektu  w pliku o nazwie `StworzZadanie`.
Z tamtad funkcja z  `sciezca` ktora przeslalismy stworzy folder  zadania oraz 3 pliki . `rozwiazanie.py`, `szablon.py`, `testy.py`. to jak stworzy jest zaleznie od `strategi` jaka przeslalismy ale domyslnie przesylamy strategie `bazowa` ktora 
### `rozwiazanie.py` 
1. przepisuje prototyp usuwajac tylko linijki ktore maja w sobie `stworz_zadanie`
### `szablon.py` 
1. przepisuje pierwsze linie póki sa komatarzami by zostawic opis zadania. wraz z mozliwymi kometarzami tworcy zadania (np jak zwracac by testy przeszly)
2. Nastepnie usuwa wszystkie linijki po za linijkami zaczynajacymi sie od `def FunkcjaKtoraTestujemy(` ta linijke zostawia i dopsiuje trzy kropki by uzytkownik wiedzial ze te funkcje sa do napisania.
3. Usuwa tak do napotkania maina ktorego zapisuje 
4. importuje klase testy
5. zapisuje odpalenia funkcje  ktore testujemy wraz z inputem nazw ich arguemntow.
6. zakomentowana metode  `Uruchom()` ktora bedzie uruchamiac testy
```python
# ====================================================================================================>
# Zadanie 21
# zrob szablon
# ====================================================================================================>
# tutaj moge dodac swoje kometarze
# wynik zwroc w print(a,b,c)

def Zadanie_21(n, b):
    # implementacja funkcji

if __name__ == "__main__":
    from testy21 import Testy21
    Zadanie_21(input("Podaj n: "), input("Podaj b: "))

    # Testy21.Uruchom()
```

### `testy.py` 
1. Napisze potrzebne importy oraz stworzy gore (deklaracje) klasy Testy
2. Nastepnie dla kazdej funkji przekazanej do testowania 
3. Sprawdza liczbe argumetnow jaka funkcja przyjmuje
4. Generuje `( 10*liczba argumentow +1 )` testow
5. Jesli liczba argumentow nie wynosi zero prosi uzytkownika o wpisanie argumentów testowych
6. Jesli argumenty wpisane prez uzytkonwika  nie beda sie zgadzły typem z arguemntami funkcji, poprosi o ponowne wpisanie.
7. Odpala funkcje na argumentach testowych  i nasluchuje printa oraz przyjmuje wartosci jaka zwroci
8. Jesli  zwroci None wynik bedzie tym co sie nasluchal jesli cos zwroci wynik bedzie tym co funkcja zwrocila a nasluchany (print) zostanie zignrowany
9. Testy zwracania i nasluchiwnia sie roznia. Stosuje metode nasluchiwania gdy wynikiem jest string. (co bedzie prowadzic do blędu jak wynikiem zwracanym jest string ale mam nadzieje ze to niemozliwy problem xd)
10. Z argumetnow i wyniku  tworzy metode testowa ktora bedzie znajdowac sie w klasie testy o nazwie `test_numerTestu_funkcjaTestowalna_argument`
   ```python
        def test_Nr1_Zadanie_21_argumenty_11(self):
            # przyklad testu nasluchiwnia test zwracania bedzie odrau bral wynik
            f = io.StringIO()
            with redirect_stdout(f):
                Zadanie_21(11)
            wynik = f.getvalue().strip()
            # wyniki sa  tablica by moc akceptowac kilka wariancji poprawnego wyniku 
            oczekiwany_wynik = ['3 4 5\n6 8 10']
            self.assertIn(wynik, oczekiwany_wynik)

```
10. Po napisaniu `liczba funkcji*( 10*liczba argumentow +1 )` metod testowych zakonczy klase Testy
11. napisze funkcje `odpal_testy` ktora bedzie odpalac testy
12. napisze funkcje `komenda` do odpalania komend  [Wiecej o komendach](#Komendy)

Po stworzeniu trzech plików funkcja utworzy plik `prototypBackup.py`, aby bezpiecznie móc usunąć prototyp. Plik prototypBackup.py jest ignorowany przez .gitignore, więc nie będzie dodawany do głównego repozytorium. Został stworzony, aby w przypadku błędnego stworzenia zadania z różnych powodów móc utworzyć zadanie na nowo (nie ma potrzeby usuwania folderu zadania, ponieważ funkcja nadpisze istniejące tam pliki). Funkcja `stworz_zadanie` dba o to, by nie usunąć pliku `prototypBackup`, dzięki czemu można tworzyć zadania do momentu zadowolenia z efektu końcowego.

Na tym konczy sie funkcja `stworz_rozwiazanie` jesli jednak komus nie podoba sie sposob w jaki pliki `rozwiazanie.py`, `szablon.py`, `testy.py` sa tworzone chcialby dodac jakas funkcjonalnosci lub inaczej tworzyc testy  zawsze moze stworzyc wlasna Strategie!

---
</details>

<details>
  <summary>🧠 Strategie</summary>

## Strategie 
moja strategia jest kiedys to napisac teraz to mi sie nie chce ale w skrocie to 
## strategia to taki swtich case 
i definiuje w jaki spoosb bedziemy tworzyc zadanie narazie to jest swtich case 1 mozliwosci bo jest 1 strategia `'bazowa'` ale w przyszlosci moze byc jakas strategia np  ze 
- `rozwiazania.py` jest  bez maina np bo kogos wkurza ze rozwiazanie jest dluzszym plikiem
-  `szablon` bez wywolania funkcji bo krocej
-  `testy.py` bez niepotrzebnych enterow bo i tak tam nikt nie zaglada po co marnowac pamiec
  to ktos stworzy taka strategie nazwie ja tam `mala` i jak uzyjemy strategi `mala` to tak to zadanie zostanie stworzone

no i kazda strategia to zbior 3 strategi jak zrobic dany plik wiec  w pliku skrypty sa StrategieTestow/ folder i tam trzeba stworzyc klase pochodna od bazowej o takiej samej nazwie jak nazwa pliku i mamy strategie testow teraz tylko w pliku strategieZestaw.py dodac jako funkcje nazwe naszej strategi i zeby zwracala jakie z 3 strategi chcemy z tych plikow mozna to laczyc jak sie chce.

</details>

<details>
  <summary> 💻 Komendy</summary>

## Komendy
W folderze skrypty/Komendy katalogu glownego mamy pliki komend. kazdy plik musi zawierac funkcje o takiej samej nazwie. I z poziomu prototypow/szablonow/rozwiazan/testow mozna ta funkcje wykonac.
Taka funkcjonalnosci pozwala w mega prosty sposob rozszerzac projekt o nowe komendy umozliwiajac coraz to fajniejsze funkcje pisania szablonow, prototypow czy ulepszanie testow

<details  >
  <summary>Spis Komend</summary>
  
  - `dodaj_testy` - w budowie
    ```python
    # dodaje  dodatkowe testy 
    komenda("dodaj_testy", funkcja, ilosci_dodatkowych_testow)
     ```
     
  - `dodaj_mozliwe_wyniki` - w budowie
    ```python
    # Do istniejacych juz wynikow testow funkcji dodaje kolejne mozliwe warienty na podstawie funkcji przeslanej
    komenda("dodaj_testy", funkcja)
     ```
  - `zwycieska_muzyka` - w budowie, lokalna
    ```python
    # Do testow danego zadania dodaje muzyka po zaliczeniu testow w szablonie
    # imo must have 
    komenda("zwycieska_muzyka", link_do_muzyki="https://www.youtube.com/watch?v=CpeJiGDVMGo" )
     ```
 - `szybka_funkcja` - w budowie
    ```python
    # szybkie testowanie funkcji na parametrach
    # dopoki nie przerwiesz bedziesz wpisywac input a komenda uzyje jej na funkcji i wypisze output
    komenda("szybka_funkcja", funkcja )
     ```
    
  - `StworzStruktureWDI`
    ```python
    # Nie bedzie wiecej uzywana i nawet nie da sie jej odpalic z poziomu plikow zadan takie zabezpieczenie
    # Ale dodaje jako taka ciekawostka oraz na przyszlosci do tworzenia struktur innych zadan
    komenda("StworzStruktureWDI")
     ```

</details>


- Jesli komenda ma dopis lokalna oznacza ze jej dzialanie nie moze wyjsci po za lokalne repozytorium. By uniknoc przypadkow ze ktos nie spodziwal ze mu poleci [najlepsza  domyslna piosenka zwycieska](https://www.youtube.com/watch?v=CpeJiGDVMGo) po napisaniu szablonu
- Zapis `link_do_muzyki="https://www.youtube.com/watch?v=CpeJiGDVMGo` oznacza ze zmienna `link_do_muzyki` jest opcjonalna i domyslnie uzyjemy `https://www.youtube.com/watch?v=CpeJiGDVMGo`
  

mam jeszcze duzo pomyslow na komendy ale nie chce pisac ich wszystkich poki co ich zasady to
- Kazda ma miec swoj plik nawet jakby plik mialby miec 20 linijek lub 100000 linijek
- Każda komenda musi być w pełni niezależna i działać poprawnie samodzielnie, ale może wywoływać inne komendy w ramach swoich działań [zgodnie z wzorcem łańcucha zobowiązań]( https://refactoring.guru/pl/design-patterns/chain-of-responsibility)

  
</details>

---

## 🤓 Kilka slów od Autora
Projekt wydaje się być znacznie ambitniejszy, niż sugeruje problem, jakim jest WDI, oraz forma, w jakiej jest realizowany — czyli pisanie na kartce a program nie ma dzialac ma byc ladny. Powstał jednak z myślą o tym, by uniknąć wielu mniejszych rozwiązań, ponieważ raczej nikt nie wykona wszystkich 200 zadań. 
Na początku nie sądziłem, że projekt rozwinie się do takiego stopnia. Uważam, że stał się bardziej systemem rozwiązań, szablonów i testów RST (stad nazwa), które planuje wykorzystać w innych zbiorach zadań lub przedmiotach. Tworzenie go dało mi fajny projekt w cv, fun i wiele doswiadczenia.I tak wgl, projekt srt nie tylko dlatego ze to skrot tez czytajac to mozna poczuc podobienstwo do slowa asSeRT xddd co za legenda ⭐⭐⭐



  
   
