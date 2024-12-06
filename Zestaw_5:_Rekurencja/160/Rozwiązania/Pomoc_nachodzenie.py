import pygame

pygame.init()

szerokosc_okna = 800
wysokosc_okna = 600
okno = pygame.display.set_mode((szerokosc_okna, wysokosc_okna))
pygame.display.set_caption("github.com/kamilGie/ASRT-WDI")

# Kolory
kolor_kwadratu1 = (72, 209, 204)
kolor_kwadratu2 = (255, 165, 0)
kolor_linii = (255, 69, 0)
tlo_kolor = (30, 30, 30)
kolor_napisu = (255, 255, 255)

bok_kwadratu = 100
kwadraty = [(100, 100), (300, 200)]

czcionka = pygame.font.SysFont("Arial", 36)
aktualnie_przeciagany = None
przesuniety_x = 0
przesuniety_y = 0


def rysuj_linie_i_napis(
    punkty1, punkty2, index1, index2, tekst, offset_x=0, offset_y=0
):
    pygame.draw.line(okno, kolor_linii, punkty1[index1], punkty2[index2], 3)
    srodek_x = (punkty1[index1][0] + punkty2[index2][0]) // 2 + offset_x
    srodek_y = (punkty1[index1][1] + punkty2[index2][1]) // 2 + offset_y
    napis = czcionka.render(tekst, True, kolor_napisu)
    okno.blit(napis, (srodek_x, srodek_y))


def rysuj_relacje_nachodzenia(punkty_kwadrat1, punkty_kwadrat2):
    # relacje sa na odwrot bo w grach uklad jest od gorny lewej
    if punkty_kwadrat1[2][0] <= punkty_kwadrat2[0][0]:
        rysuj_linie_i_napis(
            punkty_kwadrat1, punkty_kwadrat2, 2, 0, "lewo", offset_x=-20
        )
    if punkty_kwadrat1[0][0] >= punkty_kwadrat2[2][0]:
        rysuj_linie_i_napis(
            punkty_kwadrat1, punkty_kwadrat2, 0, 2, "prawo", offset_x=20
        )
    if punkty_kwadrat1[3][1] <= punkty_kwadrat2[1][1]:
        rysuj_linie_i_napis(
            punkty_kwadrat1, punkty_kwadrat2, 3, 1, "góra", offset_y=-30
        )
    if punkty_kwadrat1[1][1] >= punkty_kwadrat2[3][1]:
        rysuj_linie_i_napis(punkty_kwadrat1, punkty_kwadrat2, 1, 3, "dół", offset_y=10)


dziala = True
while dziala:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dziala = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i, (x, y) in enumerate(kwadraty):
                if (
                    x <= event.pos[0] <= x + bok_kwadratu
                    and y <= event.pos[1] <= y + bok_kwadratu
                ):
                    aktualnie_przeciagany = i
                    przesuniety_x, przesuniety_y = event.pos[0] - x, event.pos[1] - y
                    break
        elif event.type == pygame.MOUSEBUTTONUP:
            aktualnie_przeciagany = None
        elif event.type == pygame.MOUSEMOTION:
            if aktualnie_przeciagany is not None:
                x, y = kwadraty[aktualnie_przeciagany]
                nowy_x = event.pos[0] - przesuniety_x
                nowy_y = event.pos[1] - przesuniety_y
                kwadraty[aktualnie_przeciagany] = (nowy_x, nowy_y)

    okno.fill(tlo_kolor)

    for i, (x, y) in enumerate(kwadraty):
        kolor = kolor_kwadratu1 if i == 0 else kolor_kwadratu2
        pygame.draw.rect(okno, kolor, (x, y, bok_kwadratu, bok_kwadratu))
        tekst = czcionka.render(f"K{i + 1}", True, kolor_napisu)
        okno.blit(tekst, (x + 10, y + 10))

    if len(kwadraty) == 2:
        (x1, y1), (x2, y2) = kwadraty
        punkty_kwadrat1 = [
            (x1, y1),
            (x1 + bok_kwadratu, y1),
            (x1 + bok_kwadratu, y1 + bok_kwadratu),
            (x1, y1 + bok_kwadratu),
        ]
        punkty_kwadrat2 = [
            (x2, y2),
            (x2 + bok_kwadratu, y2),
            (x2 + bok_kwadratu, y2 + bok_kwadratu),
            (x2, y2 + bok_kwadratu),
        ]
        rysuj_relacje_nachodzenia(punkty_kwadrat1, punkty_kwadrat2)

    pygame.display.flip()

pygame.quit()
