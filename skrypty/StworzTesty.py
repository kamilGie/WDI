import os
import inspect
import io
from contextlib import redirect_stdout
from TemplateGenerator import DolKlasyTestow, metodaKlasyTestow, GoraKlasyTestow


def ApendOnKeyword(file_path, new_content, keyword):
    with open(file_path, "r") as file:
        lines = file.readlines()  # Odczytaj wszystkie linie z pliku

    # Otwórz plik do zapisu
    with open(file_path, "w") as file:
        for line in lines:
            if keyword in line:
                file.write(line.replace(keyword, new_content))  # Dopisz nowe dane
            else:
                file.write(line)  # Zapisz oryginalne linie


# prosze niech ktos wymysli cos lepszego xd
# to jest totlanie glupia i do usuniecia funkcja ale nie mam pomyslu jak narazie
def usunZmienneFunkcjiOdpalTesty(file_path):
    keyword = "odpalTesty("
    with open(file_path, "r") as file:
        lines = file.readlines()  # Odczytaj wszystkie linie z pliku

    # Otwórz plik do zapisu
    with open(file_path, "w") as file:
        for line in lines:
            if keyword in line:
                file.write("    " + keyword + ")")
            else:
                file.write(line)  # Zapisz oryginalne linie


def indexLiniKoncaOpisu(lines):
    ramkaOpisu = "# ====================================================================================================>"
    licznikRamek = 0
    for i, line in enumerate(lines):
        if ramkaOpisu in line:
            licznikRamek += 1
        if licznikRamek >= 2:
            return i
    return 0


def GenerujTest(numerTestu, funkcje):
    wynik = GoraKlasyTestow(numerTestu)
    for funkcja in funkcje:
        signature = inspect.signature(funkcja)
        num_args = len(signature.parameters)

        for _ in range(num_args * 10 + 1):
            argumenty = ()
            if num_args > 0:
                user_input = input(
                    f"Podaj {num_args} argumenty testowe, oddzielone spacją: "
                )
                argumenty = tuple(map(int, user_input.split()))
            f = io.StringIO()
            with redirect_stdout(f):
                funkcja(*argumenty)
            wynik += metodaKlasyTestow(numerTestu, argumenty, f.getvalue().strip())

    wynik += "\n"
    wynik += DolKlasyTestow(numerTestu)
    return wynik


def PrzeniesRozwiazanie(filePath, numerTestu):
    sciezkaRozwiazania = filePath + "rozwiazanie" + str(numerTestu) + ".py"
    sciezkaSzablonu = filePath + "szablon" + str(numerTestu) + ".py"

    with open(sciezkaSzablonu, "r") as file:
        lines = file.readlines()

    with open(sciezkaRozwiazania, "w") as file:
        file.writelines(lines)

    with open(sciezkaSzablonu, "w") as file:
        indexKonca = indexLiniKoncaOpisu(lines)
        file.writelines(lines[0 : indexKonca + 1])
        LiniaCialaFunkcji = False
        for line in lines[indexKonca + 1 :]:
            if line.startswith("def "):
                if LiniaCialaFunkcji:
                    file.write("\n\n\n")

                file.write(line.replace("\n", "") + " ...")
                LiniaCialaFunkcji = True

            if 'if __name__ == "__main__":\n' in line:
                file.write("\n\n\n")
                LiniaCialaFunkcji = False

            if not LiniaCialaFunkcji:
                file.write(line)


def StworzTesty(numerTestu, sciezkaPliku, funkcje):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    new_file_path = os.path.join(current_dir, "../", sciezkaPliku + "/")

    sciezkaTestow = new_file_path + "testy" + str(numerTestu) + ".py"
    sciezkaSzablonu = new_file_path + "szablon" + str(numerTestu) + ".py"
    ApendOnKeyword(
        sciezkaTestow,
        GenerujTest(numerTestu, funkcje),
        "### TU BEDA TESTY ###",
    )

    sciezkaSzablonu = new_file_path + "szablon" + str(numerTestu) + ".py"
    ApendOnKeyword(
        sciezkaSzablonu,
        "odpalTesty",
        "StworzTesty",
    )
    usunZmienneFunkcjiOdpalTesty(sciezkaSzablonu)

    PrzeniesRozwiazanie(new_file_path, numerTestu)
