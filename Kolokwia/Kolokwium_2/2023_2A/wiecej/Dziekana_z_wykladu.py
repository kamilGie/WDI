# ====================================================================================================>
# Zadanie 2A, 2024-01-04
# Ogród składa sie z 𝑁2
# jednakowych kwadratowych działek. Posiada on dwa wejścia, jedno w lewym
# górnym rogu od strony północnej, drugie w prawym dolnym rogu od strony południowej. Dokładnie
# na środkach niektórych działek ustawiono obustronne lustra pod katem 45° albo 135° tak, że patrzący
# przez wejście północne widzi osobę stojącą przy wejściu południowym.
# (tu jest zdjecie znajdjace sie w folderze)
# Do ogrodu przyszedł zły człowiek i przekręcił dwa lustra, każde o 90°. Proszę napisać funkcję
# napraw(ogrod) poprawiającą położenie luster, tak aby przywrócić widoczność pomiędzy oboma
# wejściami. Ogród jest reprezentowany jako dwuwymiarowa tablica wypełniona spacjami. Lustra
# feprezentowane sa odpowiednio jako znaki: /i\\ .
# ====================================================================================================>
# wykład 2024-01-08

#       ^
#       0
#   < 3   1 >
#       2
#       V

end = None

N = 6

ogr = [["." for _ in range(N)] for _ in range(N)]

# brak kary za napisanie '\'
ogr[3][0] = "\\"
ogr[3][2] = "\\"
ogr[4][2] = "/"
ogr[4][5] = "/"

# print(*ogr,sep='\n')


def wypisz(ogr):
    for w in range(N):
        for k in range(N):
            print(ogr[w][k], end="")
        end
        print()
    end


end

wypisz(ogr)


def promien(ogr):
    # błąd 1:
    # na [0][0] może stać zwierciadło, zaczynając na 0,0 omijamy je
    w, k = 0, 0
    kier = 2

    skok = ((-1, 0), (0, 1), (1, 0), (0, -1))
    P = (1, 0, 3, 2)
    L = (3, 2, 1, 0)

    while True:
        # print(w,k)
        w, k = w + skok[kier][0], k + skok[kier][1]

        if ogr[w][k] == "\\":
            kier = L[kier]
        elif ogr[w][k] == "/":
            kier = P[kier]
        elif w == N - 1 and k == N - 1:
            return True  # error !!! [sic]
        elif not (0 <= w < N and 0 <= k < N):
            return False
    end

    # Co do tego "error !!!":
    # Garkowi chodzi o to, że nie bierze pod uwagę sytuacji, gdzie w prawym
    # dolnym rogu jest zwierciadło. Większym problemem imo jest to, że nie
    # bierze pod uwagę kierunku, w którym leci promień. Dziura w ścianie jest
    # tylko od dołu.


end

print(promien(ogr))


def zmien(ogr, w, k):
    if ogr[w][k] == "/":
        ogr[w][k] = "\\"
    else:
        ogr[w][k] = "/"


end


def napraw(ogr):
    lz = []
    for w in range(N):
        for k in range(N):
            if ogr[w][k] != ".":
                lz.append((w, k))  # "Za appenda nie będziemy karać"
    end

    print(lz)

    Z = len(lz)

    for i in range(Z - 1):
        for j in range(i + 1, Z):
            # na wykładzie wyjął zmienianie lz[i] poza pętlę
            zmien(ogr, lz[i][0], lz[i][1])
            zmien(ogr, *lz[j])
            if promien(ogr):
                return
            zmien(ogr, *lz[i])
            zmien(ogr, *lz[j])
        end
    end
    print("error")


end

napraw(ogr)
wypisz(ogr)
