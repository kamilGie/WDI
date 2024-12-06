import pygame
import time
from math import inf


# STAŁE
SHOW_PAWN = False
SHOW_FORBIDDEN = True
COMPARE = True
# Parametry gry
WINDOW_SIZE = 600
BOARD_COLOR = (235, 235, 208)
HIGHLIGHT_COLOR = (255, 102, 102)
KING_COLOR = (102, 178, 255)
PIECE_COLOR = (178, 34, 34)
GRID_COLOR = (0, 0, 0)
FPS = 60


# tu mozna podmienic na swoja funkcje king i sprawdzac czy sie zgadza z wizalizacja liczba ruchow
#  w terminalu bedzie liczba ruchow przez funkcje a w programie bedzie wyswietlana ilosci ruchow
def king(N, L):
    # dodaje nie legalne ruchy czyli pozycje pionkow wraz z ich atakami
    forbidden = set()
    for px, py in L:
        forbidden.add((px, py))
        forbidden.add((px - 1, py - 1))
        forbidden.add((px - 1, py + 1))

    def maximize_moves(x, y, prev_move=None):
        """zwroci maxymalna ilosci ruchow do konca lub -inf jak sie nie da dotrzec do konca"""
        if not (0 <= x < N and 0 <= y < N) or (x, y) in forbidden:
            return -inf  # nie legalny ruch

        if (x, y) == (N - 1, N - 1):
            return 0  # Cel osiągnięty

        # krol moze porszuac sie tylko w prawo gore dol
        # zeby wrocim tam gdzie byl musial by po ruchu w gore
        # pojsc w dol nie ma innej opcji
        res = -inf
        if prev_move != "up":  # czy moge w dol
            res = max(res, maximize_moves(x + 1, y, "down"))
        if prev_move != "down":  # czy moge w gore
            res = max(res, maximize_moves(x - 1, y, "up"))
        res = max(res, (maximize_moves(x, y + 1)))  # W prawo

        # zwracam maxymalna liczbe ruchow najlepszego ruchu wraz z ruchem na pozycje tego ruchu
        return res + 1

    result = maximize_moves(0, 0)
    return None if result == -inf else result


def kingOrginalny(N, L):
    forbidden = set()
    for px, py in L:
        forbidden.add((px, py))
        forbidden.add((px - 1, py - 1))
        forbidden.add((px - 1, py + 1))

    def maximize_moves(x, y, prev_move=None):
        if not (0 <= x < N and 0 <= y < N) or (x, y) in forbidden:
            return -inf
        if (x, y) == (N - 1, N - 1):
            return 0
        res = -inf
        if prev_move != "up":
            res = max(res, maximize_moves(x + 1, y, "down"))
        if prev_move != "down":
            res = max(res, maximize_moves(x - 1, y, "up"))
        res = max(res, maximize_moves(x, y + 1))
        return res + 1

    path = []

    # ta wersja sprawdza czy mamy path jak mamy zwroci true
    def find_path(x, y, moves_left, prev_move=None):
        if moves_left < 0 or not (0 <= x < N and 0 <= y < N) or (x, y) in forbidden:
            return False
        if (x, y) == (N - 1, N - 1):
            path.append((x, y))
            return True

        if prev_move != "up" and maximize_moves(x + 1, y, "down") == moves_left - 1:
            if find_path(x + 1, y, moves_left - 1, "down"):
                path.append((x, y))
                return True
        if prev_move != "down" and maximize_moves(x - 1, y, "up") == moves_left - 1:
            if find_path(x - 1, y, moves_left - 1, "up"):
                path.append((x, y))
                return True
        if maximize_moves(x, y + 1) == moves_left - 1:
            if find_path(x, y + 1, moves_left - 1):
                path.append((x, y))
                return True

    result = maximize_moves(0, 0)
    if result != -inf:
        find_path(0, 0, result)
    return (None, None) if result == -inf else (result, path[::-1])


def draw_board(
    screen,
    N,
    cell_size,
    pieces,
    forbidden,
    king_pos=None,
    visited=None,
    show_pieces=SHOW_PAWN,
    highlight_forbidden=True,
):
    font = pygame.font.SysFont("Arial", cell_size // 2, bold=True)  # Ładna czcionka

    for row in range(N):
        for col in range(N):
            rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
            color = BOARD_COLOR if (row + col) % 2 == 0 else (200, 200, 200)

            # Podświetlanie pól atakowanych przez pionki
            if highlight_forbidden and (row, col) in forbidden:
                color = HIGHLIGHT_COLOR

            # Podświetlanie odwiedzonych pól
            if visited and (row, col) in visited:
                color = (173, 216, 230)  # Jasnoniebieski

            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, GRID_COLOR, rect, 1)

            # Rysowanie numeru ruchu na odwiedzonych polach
            if visited and (row, col) in visited:
                move_num = visited[(row, col)]
                text = font.render(str(move_num), True, (0, 0, 255))  # Niebieski tekst

                # Wyśrodkowanie tekstu
                text_rect = text.get_rect(
                    center=(
                        col * cell_size + cell_size // 2,
                        row * cell_size + cell_size // 2,
                    )
                )
                screen.blit(text, text_rect)

    # Rysowanie pionków, jeśli `show_pieces` jest True
    if show_pieces:
        for px, py in pieces:
            pygame.draw.circle(
                screen,
                PIECE_COLOR,
                ((py + 0.5) * cell_size, (px + 0.5) * cell_size),
                cell_size // 3,
            )

    # Rysowanie króla
    if king_pos:
        kx, ky = king_pos
        pygame.draw.circle(
            screen,
            KING_COLOR,
            ((ky + 0.5) * cell_size, (kx + 0.5) * cell_size),
            cell_size // 3,
        )


def main():
    N = 8  # Rozmiar szachownicy
    pieces = []  # Lista pionków
    forbidden = set()
    path = []
    king_pos = (0, 0)
    path_index = 0
    visited = {}  # Słownik przechowujący odwiedzone pola i numer ruchu
    animating = False
    show_pieces = True  # Zmienna decydująca o wyświetlaniu pionków

    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("github.com/kamilGie/ASRT-WDI")
    clock = pygame.time.Clock()

    cell_size = WINDOW_SIZE // N
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Toglować pionki poprzez kliknięcie
                x, y = event.pos
                row, col = y // cell_size, x // cell_size
                if (row, col) in pieces:
                    pieces.remove((row, col))  # Usuwanie pionka
                elif (row, col) != (0, 0) and (row, col) != (N - 1, N - 1):
                    pieces.append((row, col))  # Dodawanie pionka
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Obliczanie ścieżki i pokazywanie pól atakowanych
                    forbidden.clear()
                    for px, py in pieces:
                        forbidden.add((px, py))
                        forbidden.add((px - 1, py - 1))
                        forbidden.add((px - 1, py + 1))

                    # Po naciśnięciu spacji usuwamy pionki, tylko atakowane pola są widoczne
                    show_pieces = SHOW_PAWN

                    screen.fill((0, 0, 0))
                    draw_board(
                        screen,
                        N,
                        cell_size,
                        pieces,
                        forbidden,
                        king_pos,
                        highlight_forbidden=SHOW_FORBIDDEN,
                    )
                    pygame.display.flip()
                    pygame.time.delay(1000)  # Pokazanie atakowanych pól na sekundę

                    if COMPARE:
                        print(king(N, pieces))

                    _, path = kingOrginalny(N, pieces)
                    path_index = 0
                    visited.clear()
                    animating = True
                elif event.key == pygame.K_r:
                    # Reset króla do pozycji początkowej i usunięcie podświetlenia atakowanych pól
                    king_pos = (0, 0)
                    animating = False
                    path = []
                    visited.clear()
                    forbidden.clear()  # Usunięcie podświetlonych pól atakowanych
                    show_pieces = True  # Przywrócenie widoczności pionków

        # Animowanie króla
        if animating and path and path_index < len(path):
            king_pos = path[path_index]
            visited[king_pos] = path_index  # Numer ruchu
            path_index += 1
            if path_index == len(path):
                animating = False
            time.sleep(0.2)  # Opóźnienie między ruchami

        # Rysowanie planszy
        screen.fill((0, 0, 0))
        draw_board(
            screen, N, cell_size, pieces, forbidden, king_pos, visited, show_pieces
        )
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
