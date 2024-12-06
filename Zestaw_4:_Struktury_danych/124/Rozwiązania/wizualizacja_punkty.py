import pygame
import sys

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20
BACKGROUND_COLOR = (200, 200, 200)
GRID_COLOR = (50, 50, 50)
POINT_COLOR = (255, 0, 0)
SQUARE_COLOR = (0, 0, 255)
SQUARE_ACTIVE_COLOR = (0, 255, 0)
SQUARE_INACTIVE_COLOR = (255, 0, 0)

def draw_grid(screen):
    for x in range(0, SCREEN_WIDTH, GRID_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, SCREEN_HEIGHT), 1)
    for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (SCREEN_WIDTH, y), 1)
    pygame.draw.line(screen, GRID_COLOR, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT), 2)
    pygame.draw.line(screen, GRID_COLOR, (0, SCREEN_HEIGHT // 2), (SCREEN_WIDTH, SCREEN_HEIGHT // 2), 2)

def transform_coordinates(x, y):
    return SCREEN_WIDTH // 2 + x * GRID_SIZE, SCREEN_HEIGHT // 2 - y * GRID_SIZE

def draw_points(screen, points):
    for point in points:
        transformed_point = transform_coordinates(point[0], point[1])
        pygame.draw.circle(screen, POINT_COLOR, transformed_point, 5)

def draw_square(screen, square, color):
    pygame.draw.rect(screen, color, square["rect"], 2)

def check_collision(square, points):
    for point in points:
        px, py = transform_coordinates(point[0], point[1])
        if square["rect"].x <= px <= square["rect"].x + square["rect"].width and square["rect"].y <= py <= square["rect"].y + square["rect"].height:
            return True
    return False

def toggle_point(points, grid_x, grid_y):
    point = (grid_x, grid_y)
    if point in points:
        points.remove(point)
    else:
        points.append(point)

def check_square_corners(square, points):
    corners = [
        (square["rect"].x, square["rect"].y),  
        (square["rect"].x + square["rect"].width, square["rect"].y),
        (square["rect"].x, square["rect"].y + square["rect"].height),
        (square["rect"].x + square["rect"].width, square["rect"].y + square["rect"].height),
    ]

    for corner in corners:
        corner_grid_x = (corner[0] - SCREEN_WIDTH // 2) // GRID_SIZE
        corner_grid_y = -(corner[1] - SCREEN_HEIGHT // 2) // GRID_SIZE
        if (corner_grid_x, corner_grid_y) not in points:
            return False
    return True

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("github.com/kamilGie/ASRT-WDI")
clock = pygame.time.Clock()

points = []

square = {
    "rect": pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 0, 0),
    "growth_rate": GRID_SIZE,
    "active": True,
    "size": 0,
}

last_update_time = pygame.time.get_ticks()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            grid_x = (mouse_x - SCREEN_WIDTH // 2) // GRID_SIZE
            grid_y = -(mouse_y - SCREEN_HEIGHT // 2) // GRID_SIZE
            toggle_point(points, grid_x, grid_y)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                square["rect"] = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 0, 0)
                square["active"] = True
                square["size"] = 0
            if event.key == pygame.K_r:
                points = []

    current_time = pygame.time.get_ticks()
    if current_time - last_update_time > 700:
        last_update_time = current_time
        if square["active"]:
            square["size"] += 1
            square["rect"] = pygame.Rect(
                SCREEN_WIDTH // 2 - square["growth_rate"] * square["size"],
                SCREEN_HEIGHT // 2 - square["growth_rate"] * square["size"],
                square["growth_rate"] * (2 * square["size"]),
                square["growth_rate"] * (2 * square["size"]),
            )
            if check_collision(square, points):
                square["active"] = False

    square_color = SQUARE_COLOR

    if not square["active"]:
        if check_square_corners(square, points):
            square_color = SQUARE_ACTIVE_COLOR
        else:
            square_color = SQUARE_INACTIVE_COLOR

    screen.fill(BACKGROUND_COLOR)
    draw_grid(screen)
    draw_points(screen, points)
    draw_square(screen, square, square_color)
    pygame.display.flip()
    clock.tick(60)
