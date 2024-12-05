import pygame
import sys
from itertools import combinations
from itertools import permutations
import random

N = 8
CELL_SIZE = 80

# Kolory
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (139, 69, 19)
LIGHT_GREEN = (144, 238, 144)
TRANSPARENT_BROWN = ( 139, 69, 19, 100)


def draw_board(screen, t, w, removed_towers):
    intersection_cells = set()

    for col1, col2 in combinations(removed_towers, 2):
        row1 = w[col1]
        row2 = w[col2]

        intersection_cells.add((row1, col2))
        intersection_cells.add((row2, col1))

    for row in range(N):
        for col in range(N):

            if (row, col) in intersection_cells:
                pygame.draw.rect( screen, LIGHT_GREEN, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            else:
                color = WHITE if (row + col) % 2 == 0 else BLACK
                pygame.draw.rect( screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            font = pygame.font.Font(None, 36)
            text = font.render(str(t[row][col]), True, (0, 0, 200))
            text_rect = text.get_rect( center=( col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2,))
            screen.blit(text, text_rect)

    for col, row in enumerate(w):
        if col not in removed_towers:
            pygame.draw.line( screen, RED, (0, row * CELL_SIZE + CELL_SIZE // 2), (N * CELL_SIZE, row * CELL_SIZE + CELL_SIZE // 2), 10,)
            pygame.draw.line( screen, RED, (col * CELL_SIZE + CELL_SIZE // 2, 0), (col * CELL_SIZE + CELL_SIZE // 2, N * CELL_SIZE), 10,)

    for col, row in enumerate(w):
        if col not in removed_towers:
            pygame.draw.circle( screen, BROWN, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3,)
        else:
            # Wieża zabrana - rysowanie przezroczystej wieży
            tower_surface = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
            pygame.draw.circle( tower_surface, TRANSPARENT_BROWN, (CELL_SIZE // 2, CELL_SIZE // 2), CELL_SIZE // 3,)
            screen.blit(tower_surface, (col * CELL_SIZE, row * CELL_SIZE))


def main():
    pygame.init()
    screen = pygame.display.set_mode((N * CELL_SIZE, N * CELL_SIZE))
    pygame.display.set_caption("Wieże na szachownicy")
    clock = pygame.time.Clock()

    # Generowanie danych tablicy T i W
    t = [[random.randint(1, 9) for _ in range(N)] for _ in range(N)]
    all_permutations = list(permutations(range(N)))
    w = random.choice(all_permutations)  # Losowo wybieramy jedną permutację

    removed_towers = set()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Obsługa kliknięć myszą
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                col = x // CELL_SIZE
                if col in removed_towers:
                    removed_towers.remove(col)
                elif len(removed_towers) < 2:
                    removed_towers.add(col)

        screen.fill(BLACK)
        draw_board(screen, t, w, removed_towers)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
