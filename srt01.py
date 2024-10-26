# ====================================================================================================>
# Zadanie 1
# Proszę napisać program poszukujący trójkątów Pitagorejskich w których długość przekątnej
# jest mniejsza od liczby N wprowadzonej z klawiatury.
# ====================================================================================================>


def Zadanie_1(n):
    for a in range(1, n):
        for b in range(a, n):
            c = (a * a + b * b) ** 0.5
            if c.is_integer() and c < n:
                print(a, b, int(c))


if __name__ == "__main__":

    #  def Zadanie_1(n):

