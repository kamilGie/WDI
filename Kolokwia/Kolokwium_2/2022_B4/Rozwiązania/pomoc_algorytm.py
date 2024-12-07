""" Ten kod jest bardzo pogmatwany i przekombinowany i jest w nim wiele niepotrzebnego kodu
    jest tak bo poczatkowo planowalem dodac algorymt bardziej oplacalnego wyszukiwnia niz brute force
    jednak im wiecej sie ucze tego przedmiotu tym bardziej rozumiem ze najwazniejsze to zeby kod dzialal
    i nie ma co kombinowac jak rozwiazanie jest proste wiec dodalem najprostsze rozwiazanie i jego wizualizacje
"""

import pygame
import sys
import time


WINDOW_SIZE = 600
GRID_SIZE = 8
CELL_SIZE = WINDOW_SIZE // GRID_SIZE
BG_COLOR_LIGHT = (240, 240, 240)
BG_COLOR_DARK = (200, 200, 200)
ROOK_COLOR = (0, 0, 255)
ROOK_UNDISCOVERED_COLOR = (0, 0, 255)
ATTACKED_COLOR = (255, 0, 0, 100)
HIGHLIGHT_COLOR = (0, 150, 255, 100)
ERROR_COLOR = (255, 0, 0)
HIGHLIGHT_FIRST_FREE_COLOR = (255, 255, 0, 100)
MOVE_EFFECT_COLOR = (0, 255, 0, 100)
ROOK_MOVED_COLOR = (100, 100, 100)


def draw_grid(screen):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            color = BG_COLOR_LIGHT if (row + col) % 2 == 0 else BG_COLOR_DARK
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, color, rect)


def draw_board(
    screen,
    grid,
    attacked,
    highlight=None,
    move_effect=None,
    processed_rooks=None,
    discovered_rooks=None,
):
    if processed_rooks is None:
        processed_rooks = set()
    if discovered_rooks is None:
        discovered_rooks = set()

    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)

            if highlight and highlight == (row, col):
                highlight_surf = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
                highlight_surf.fill(HIGHLIGHT_FIRST_FREE_COLOR)
                screen.blit(highlight_surf, rect.topleft)

            if move_effect and move_effect == (row, col):
                move_surf = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
                move_surf.fill(MOVE_EFFECT_COLOR)
                screen.blit(move_surf, rect.topleft)

            if attacked[row][col]:
                attack_surf = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
                attack_surf.fill(ATTACKED_COLOR)
                screen.blit(attack_surf, rect.topleft)

            if grid[row][col]:
                if (row, col) in processed_rooks:
                    color = ROOK_MOVED_COLOR
                elif (row, col) in discovered_rooks:
                    color = ROOK_COLOR
                else:
                    color = ROOK_UNDISCOVERED_COLOR

                pygame.draw.circle(screen, color, rect.center, CELL_SIZE // 3)


# to jest naprawde dluga i brzydka funkcja ale nie chce mi sie tego poprawiac i tak nikt tego nie bedzie czytal xd oby
def find_and_move_rook(grid, screen):
    """
    Przesuwa każdą wieżę po kolei na każde możliwe pole.
    Jeśli żadna konfiguracja nie szachuje całej planszy, wraca do pierwotnego stanu.
    """
    original_positions = [
        (r, c) for r in range(GRID_SIZE) for c in range(GRID_SIZE) if grid[r][c]
    ]

    for original_r, original_c in original_positions:
        # Testujemy przesunięcie wieży na każde pole planszy.
        for target_row in range(GRID_SIZE):
            for target_col in range(GRID_SIZE):
                if grid[target_row][target_col]:
                    continue  # Pole jest już zajęte.

                # Przenieś wieżę na nowe pole.
                grid[original_r][original_c] = False
                grid[target_row][target_col] = True

                # Rysowanie planszy.
                screen.fill((0, 0, 0))
                draw_grid(screen)
                draw_board(
                    screen,
                    grid,
                    calculate_attacked(grid),
                    highlight=(target_row, target_col),
                )
                pygame.display.flip()
                time.sleep(0.1)

                # Sprawdź, czy cała plansza jest szachowana.
                if all_attacked(calculate_attacked(grid)):
                    # Sukces, wyświetlamy efekt.
                    for _ in range(3):
                        glow_surf = pygame.Surface(
                            (WINDOW_SIZE, WINDOW_SIZE), pygame.SRCALPHA
                        )
                        glow_color = (0, 255, 0, 100)
                        glow_surf.fill(glow_color)
                        screen.blit(glow_surf, (0, 0))
                        pygame.display.flip()
                        time.sleep(0.2)
                        screen.fill((0, 0, 0))
                        draw_grid(screen)
                        draw_board(screen, grid, calculate_attacked(grid))
                        pygame.display.flip()
                        time.sleep(0.2)

                    return True

                # Cofnij ruch, jeśli to nie rozwiązanie.
                grid[target_row][target_col] = False
                grid[original_r][original_c] = True

                # Rysowanie cofnięcia ruchu.
                screen.fill((0, 0, 0))
                draw_grid(screen)
                draw_board(
                    screen,
                    grid,
                    calculate_attacked(grid),
                    highlight=(original_r, original_c),
                )
                pygame.display.flip()
                time.sleep(0.1)

    # Jeśli żadna konfiguracja nie działa, zwróć False.
    return False


def calculate_attacked(grid):
    attacked = [[False] * GRID_SIZE for _ in range(GRID_SIZE)]

    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if grid[row][col]:
                for i in range(GRID_SIZE):
                    attacked[row][i] = True
                    attacked[i][col] = True

    return attacked


def all_attacked(attacked):
    return all(all(row) for row in attacked)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("github.com/kamilGie/ASRT-WDI")
    clock = pygame.time.Clock()

    grid = [[False] * GRID_SIZE for _ in range(GRID_SIZE)]
    search_mode = False

    while True:
        screen.fill((0, 0, 0))
        draw_grid(screen)
        attacked = calculate_attacked(grid)
        draw_board(screen, grid, attacked)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                col, row = event.pos[0] // CELL_SIZE, event.pos[1] // CELL_SIZE
                grid[row][col] = not grid[row][col]
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    search_mode = True

        if search_mode:
            if find_and_move_rook(grid, screen):
                search_mode = False
            else:
                for _ in range(3):
                    screen.fill(ERROR_COLOR)
                    pygame.display.flip()
                    time.sleep(0.2)
                    screen.fill((0, 0, 0))
                    draw_grid(screen)
                    draw_board(screen, grid, attacked)
                    pygame.display.flip()
                    time.sleep(0.2)
                search_mode = False

        pygame.display.flip()
        clock.tick(30)


if __name__ == "__main__":
    main()
