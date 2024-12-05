import pygame
import copy
import sys


# pisze to o 3 w nocy moga byc bledy a napewno nie jest optymalnie


# to mozna zmieniac dla innych wiuzalizacji ale musi byc 6 na 6
GRID = [
    ["", "", "", "", "", ""],
    ["\\", "", "\\", "", "", ""],
    ["", "", "\\", "", "\\", ""],
    ["", "", "", "", "", ""],
    ["", "", "", "", "/", "/"],
    ["", "", "", "", "", ""],
]

# Inicjalizacja Pygame

pygame.init()

# Stałe
WINDOW_SIZE = 600
GRID_SIZE = 6
CELL_SIZE = WINDOW_SIZE // GRID_SIZE
WHITE = (255, 255, 255)
BLACK = (40, 40, 40)
RED = (255, 99, 71)
BLUE = (70, 130, 180)
GREEN = (34, 139, 34)
BLACK_GREEN = (0, 51, 0)
TEXT_COLOR = (255, 223, 0)  # Jasny żółty

VARIABLE_COLOR = (173, 216, 230)  # Jasny niebieski
NONE = 0
MIRROR_45 = 1
MIRROR_135 = 2


# Utwórz siatkę z losowo umieszczonymi lustrami
def create_grid(initial_grid):

    grid = []
    for row in initial_grid:
        grid_row = []
        for cell in row:
            if cell == "":
                grid_row.append(NONE)
            elif cell == "\\":
                grid_row.append(MIRROR_45)
            elif cell == "/":
                grid_row.append(MIRROR_135)
        grid.append(grid_row)
    return grid


def draw_grid(screen, grid):
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if (x, y) in highlighted_cells:
                pygame.draw.rect(screen, highlight_color, rect)
            else:
                pygame.draw.rect(screen, WHITE, rect, 1)
            pygame.draw.rect(screen, WHITE, rect, 1)
            if grid[y][x] == MIRROR_45:
                pygame.draw.line(
                    screen,
                    BLUE,
                    (x * CELL_SIZE, y * CELL_SIZE),
                    ((x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE),
                    5,
                )
            elif grid[y][x] == MIRROR_135:
                pygame.draw.line(
                    screen,
                    BLUE,
                    ((x + 1) * CELL_SIZE, y * CELL_SIZE),
                    (x * CELL_SIZE, (y + 1) * CELL_SIZE),
                    5,
                )


def trace_path(grid):
    path = []
    x, y = 0, 0  # Start w lewym górnym rogu
    dx, dy = 0, 1  # Kierunek na wschód (prawo)

    while 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE:
        path.append((x, y))

        if grid[y][x] == MIRROR_45:
            dx, dy = dy, dx  # Odbicie na 45 stopni
        elif grid[y][x] == MIRROR_135:
            dx, dy = -dy, -dx  # Odbicie na 135 stopni

        x, y = x + dx, y + dy

    return path


def draw_path(screen, path):
    for i in range(len(path) - 1):
        x1, y1 = path[i]
        x2, y2 = path[i + 1]
        start_pos = (x1 * CELL_SIZE + CELL_SIZE // 2, y1 * CELL_SIZE + CELL_SIZE // 2)
        end_pos = (x2 * CELL_SIZE + CELL_SIZE // 2, y2 * CELL_SIZE + CELL_SIZE // 2)
        pygame.draw.line(screen, RED, start_pos, end_pos, 5)  # Czerwony laser


def toggle_mirror(grid, grid_x, grid_y):
    # Zmiana typu lustra
    if grid[grid_y][grid_x] == MIRROR_45:
        grid[grid_y][grid_x] = MIRROR_135
    elif grid[grid_y][grid_x] == MIRROR_135:
        grid[grid_y][grid_x] = MIRROR_45


def Zadanie_2A(ogrod):  # Generator stanów luster
    n = len(ogrod)
    ns = n**2
    for i in range(ns):
        if ogrod[i // n][i % n] in ["/", "\\"]:  # zawiera lustro
            for j in range(i + 1, ns):  # wszystkie lustra po indeksie i
                yield (i // n, i % n, j // n, j % n)  # Zwracanie starego stanu
    return None


highlighted_cells = []  # Przechowuje współrzędne dwóch wyróżnionych luster
highlight_color = (255, 255, 0)
# Główna pętla
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("github.com/kamilGie/ASRT-WDI")
generator = Zadanie_2A(GRID)  # Tworzymy generator
grid = create_grid(GRID)
n = len(grid)
running = True
last_time = pygame.time.get_ticks()
interval = 200  # Interwał w milisekundach
znalazl_lusta = False
obrocil_lustra = False
grid_original = copy.deepcopy(grid)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Zmieniaj stan co określony czas
    current_time = pygame.time.get_ticks()
    if current_time - last_time >= interval:
        try:
            grid = copy.deepcopy(grid_original)
            y1, x1, y2, x2 = next(generator)

            if grid[y1][x1] > 0 and grid[y2][x2] > 0:
                toggle_mirror(grid, x1, y1)
                toggle_mirror(grid, x2, y2)
                interval = 1000
                highlight_color = (200, 200, 200)
            else:
                interval = 150
                highlight_color = (100, 100, 100)

            highlighted_cells = []
            highlighted_cells.append((x1, y1))
            highlighted_cells.append((x2, y2))

        except StopIteration:
            print("Koniec generatora")
            running = False  # Kończymy, jeśli generator się skończy
        last_time = current_time

    screen.fill(BLACK_GREEN)  # Zielone tło
    draw_grid(screen, grid)

    path = trace_path(grid)
    if path[-1] == (n - 1, n - 1):
        break

    draw_path(screen, path)

    pygame.display.flip()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(GREEN)  # Zielone tło
    draw_grid(screen, grid)

    path = trace_path(grid)

    draw_path(screen, path)

    pygame.display.flip()
pygame.quit()
sys.exit()
