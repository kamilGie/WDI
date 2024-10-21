import os
import inspect
import io
from contextlib import redirect_stdout
from TemplateGenerator import (
    DolKlasyTestow,
    MetodaKlasyTestow,
    GoraKlasyTestow,
)


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
    res = GoraKlasyTestow(numerTestu)
    for funkcja in funkcje:
        signature = inspect.signature(funkcja)
        num_args = len(signature.parameters)

        for _ in range(num_args * 10 + 1):
            argumenty = ()
            if num_args == 1:
                user_input = input("Podaj argument Testowy: ")
                argumenty = tuple(map(int, user_input.split()))
            if num_args > 1:
                user_input = input(
                    f"Podaj {num_args} argumenty testowe, oddzielone spacją: "
                )
                argumenty = tuple(map(int, user_input.split()))
            f = io.StringIO()
            with redirect_stdout(f):
                funkcja(*argumenty)
            wynik = f.getvalue().strip()
            print(f"wynik dla tego testu to {wynik}")
            res += MetodaKlasyTestow(numerTestu, argumenty, f.getvalue().strip())

    res += "\n"
    res += DolKlasyTestow(numerTestu)
    return res


def PrzeniesRozwiazanie_PrzygotujSzablon(filePath, numerTestu):
    sciezkaRozwiazania = filePath + "rozwiazanie" + str(numerTestu) + ".py"
    sciezkaSzablonu = filePath + "szablon" + str(numerTestu) + ".py"

    with open(sciezkaSzablonu, "r") as file:
        lines = file.readlines()

    with open(sciezkaRozwiazania, "w") as file:
        # testy importuja funkcje z szablonu wiec zeby nie dawac sugesti usuwamy z rozwiazania testy
        for line in lines:
            if not f"Testy{numerTestu}" in line:
                file.write(line)

    with open(sciezkaSzablonu, "w") as file:
        # pisze tresci
        indexKonca = indexLiniKoncaOpisu(lines)
        file.writelines(lines[0 : indexKonca + 1])

        # zapisuje do pliku tylko wtedy gdy nie jestem w ciele funkcji
        LiniaCialaFunkcji = False
        for line in lines[indexKonca + 1 :]:
            if line.startswith("def "):
                # jak bedzie kilka funkcji to daje \n by nie bylo na sobie
                if LiniaCialaFunkcji:
                    file.write("\n\n\n")

                file.write(line.replace("\n", "") + " ...")
                LiniaCialaFunkcji = True

            if 'if __name__ == "__main__":\n' in line:
                file.write("\n\n\n")
                LiniaCialaFunkcji = False

            if not LiniaCialaFunkcji:
                if not "StworzTesty" in line:
                    file.write(line)

        file.write(f"    Testy{numerTestu}.uruchom()")


def StworzTesty(numerZadania, sciezkaPliku, funkcje):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    new_file_path = os.path.join(current_dir, "../", sciezkaPliku + "/")

    sciezkaTestow = new_file_path + "testy" + str(numerZadania) + ".py"
    with open(sciezkaTestow, "w") as file:
        file.write(GenerujTest(numerZadania, funkcje))

    # wywalone w solid ta funkcja robi 2 rzeczy
    PrzeniesRozwiazanie_PrzygotujSzablon(new_file_path, numerZadania)
