import pygame
import time

WHITE = (255, 255, 252)
LIGHT_GRAY = (200, 200, 200)
DARK_GRAY = (50, 50, 50)
RED = (255, 0, 0)
TRANSPARENT_RED = (255, 0, 0, 80)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)


def draw_board(screen, board, size, current_row, current_col, highlight=False):
    screen.fill(WHITE)
    tile_size = size // 8
    font = pygame.font.SysFont("Arial", 20, bold=True)

    attacked_positions = set()
    for row, col in enumerate(board):
        if col != -1 and row < current_row:
            for i in range(8):
                attacked_positions.add((row, i))
                attacked_positions.add((i, col))
                if 0 <= row + i < 8 and 0 <= col + i < 8:
                    attacked_positions.add((row + i, col + i))
                if 0 <= row - i < 8 and 0 <= col - i < 8:
                    attacked_positions.add((row - i, col - i))
                if 0 <= row + i < 8 and 0 <= col - i < 8:
                    attacked_positions.add((row + i, col - i))
                if 0 <= row - i < 8 and 0 <= col + i < 8:
                    attacked_positions.add((row - i, col + i))

    for row in range(8):
        for col in range(8):
            color = LIGHT_GRAY if (row + col) % 2 == 0 else DARK_GRAY
            pygame.draw.rect( screen, color, (col * tile_size, row * tile_size, tile_size, tile_size))

            if (row, col) in attacked_positions:
                surface = pygame.Surface((tile_size, tile_size), pygame.SRCALPHA)
                surface.fill(TRANSPARENT_RED)
                screen.blit(surface, (col * tile_size, row * tile_size))

    for row, col in enumerate(board):
        if col != -1:
            queen_color = GREEN if highlight else RED
            pygame.draw.circle( screen, queen_color, (col * tile_size + tile_size // 2, row * tile_size + tile_size // 2), tile_size // 3,)

            text_surface = font.render(f"Rekurencja {row + 1}", True, WHITE)
            text_rect = text_surface.get_rect(
                center=(
                    col * tile_size + tile_size // 2,
                    row * tile_size + tile_size // 4,
                )
            )

            # Zapobieganie wychodzeniu napisu poza planszę
            if text_rect.left < 0:
                text_rect.left = 0  
            if text_rect.right > size:
                text_rect.right = size 
            if text_rect.top < 0:
                text_rect.top = 0
            if text_rect.bottom > size:
                text_rect.bottom = size

            screen.blit(text_surface, text_rect)

    if 0 <= current_row < 8 and 0 <= current_col < 8:
        pygame.draw.circle( screen, RED, ( current_col * tile_size + tile_size // 2, current_row * tile_size + tile_size // 2,), tile_size // 3)


def main():
    pygame.init()
    board_size = 600
    screen = pygame.display.set_mode((board_size, board_size))
    pygame.display.set_caption("github.com/kamilGie/ASRT-WD")

    board = [-1] * 8
    current_row, current_col = 0, 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if current_row < 8:
            if current_col < 8:
                board[current_row] = current_col
                draw_board(screen, board, board_size, current_row, current_col)
                pygame.display.flip()
                time.sleep(0.05)

                if all(
                    board[j] != current_col
                    and abs(board[j] - current_col) != abs(j - current_row)
                    for j in range(current_row)
                ):
                    current_row += 1
                    current_col = 0
                else:
                    board[current_row] = -1
                    current_col += 1
            else:
                board[current_row] = -1
                current_row -= 1
                if current_row >= 0:
                    current_col = board[current_row] + 1
                    board[current_row] = -1
        else:
            draw_board(screen, board, board_size, -1, -1, highlight=True)
            pygame.display.flip()
            time.sleep(1)

            current_row -= 1
            current_col = board[current_row] + 1
            board[current_row] = -1

    pygame.quit()


if __name__ == "__main__":
    main()
