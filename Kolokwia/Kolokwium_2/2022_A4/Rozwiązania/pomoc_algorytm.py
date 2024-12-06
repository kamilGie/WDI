import pygame
import sys

WIDTH, HEIGHT = 800, 800
BOARD_SIZE = 7
TILE_SIZE = WIDTH // BOARD_SIZE
LIGHT_BROWN = (240, 210, 170)
DARK_BROWN = (200, 160, 120)
RED = (255, 69, 69, 150)
BEST_RED = (255, 0, 0, 200)
BLUE = (70, 130, 180)
LIGHT_BLUE = (135, 206, 250)
GREEN = (0, 255, 0)

KNIGHT_MOVES = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]


def is_valid(x, y):
    return 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE


def get_attacked_positions(board):
    attacked = set()
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == 1:
                for dx, dy in KNIGHT_MOVES:
                    nx, ny = row + dx, col + dy
                    if is_valid(nx, ny) and board[nx][ny] == 0:
                        attacked.add((nx, ny))
    return attacked


def get_attacked_positions_for_knight(x, y):
    return {(x + dx, y + dy) for dx, dy in KNIGHT_MOVES if is_valid(x + dx, y + dy)}


def reset_board():
    return [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]


# lekko zmieniony algormty by byl krotszy
def find_best_knight(board):
    best_position = None
    max_attacked = -1
    center = (BOARD_SIZE // 2, BOARD_SIZE // 2)
    min_distance = BOARD_SIZE

    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == 0:
                attacked_positions = get_attacked_positions_for_knight(row, col)
                combined_attacked = len(
                    attacked_positions.union(get_attacked_positions(board))
                )
                distance_to_center = max(abs(row - center[0]), abs(col - center[1]))
                if combined_attacked > max_attacked or (
                    combined_attacked == max_attacked
                    and distance_to_center < min_distance
                ):
                    best_position = (row, col)
                    max_attacked = combined_attacked
                    min_distance = distance_to_center

    return best_position


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("github.com/kamilGie/ASRT-WDI")
clock = pygame.time.Clock()


def draw_board(
    board,
    highlight_moves=None,
    attacked_positions=None,
    best_knight=None,
    knight_finished=False,
):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            color = LIGHT_BROWN if (row + col) % 2 == 0 else DARK_BROWN
            pygame.draw.rect( screen, color, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect( screen, (0, 0, 0), (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1,)
            if attacked_positions and (row, col) in attacked_positions:
                surface = pygame.Surface((TILE_SIZE, TILE_SIZE), pygame.SRCALPHA)
                surface.fill((255, 0, 0, 180))
                screen.blit(surface, (col * TILE_SIZE, row * TILE_SIZE))
            if board[row][col] == 1:
                knight_color = (0, 0, 0)
                if best_knight == (row, col):
                    knight_color = GREEN if knight_finished else (25, 25, 112)
                pygame.draw.circle( screen, knight_color, ( col * TILE_SIZE + TILE_SIZE // 2, row * TILE_SIZE + TILE_SIZE // 2,), TILE_SIZE // 4)


def main():
    board = reset_board()
    knights = []
    searching = False
    best_knight = None
    attacked_positions = set()
    knight_finished = False

    while True:
        screen.fill((0, 0, 0))
        draw_board( board, highlight_moves=None, attacked_positions=attacked_positions, best_knight=best_knight, knight_finished=knight_finished)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and not searching:
                x, y = pygame.mouse.get_pos()
                col, row = x // TILE_SIZE, y // TILE_SIZE
                if board[row][col] == 0:
                    board[row][col] = 1
                    knights.append((row, col))
                    attacked_positions = get_attacked_positions(board)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    board = reset_board()
                    knights = []
                    searching = False
                    best_knight = None
                    attacked_positions = set()
                    knight_finished = False
                elif event.key == pygame.K_SPACE and not searching:
                    searching = True

        if searching:
            best_knight = None
            for row in range(BOARD_SIZE):
                for col in range(BOARD_SIZE):
                    if board[row][col] == 0:
                        board[row][col] = 1
                        new_attacked_positions = get_attacked_positions(board)
                        draw_board( board, highlight_moves=None, attacked_positions=new_attacked_positions, best_knight=(row, col))
                        pygame.display.flip()
                        pygame.time.wait(300)
                        board[row][col] = 0

            best_knight = find_best_knight(board)
            if best_knight:
                row, col = best_knight
                board[row][col] = 1
                attacked_positions = get_attacked_positions(board)
                knight_finished = True

            searching = False


if __name__ == "__main__":
    main()
