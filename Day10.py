
import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
BLOCK = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

font = pygame.font.SysFont(None, 30)

WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLACK = (0,0,0)

snake = [(100,100)]
direction = "RIGHT"

food_x = random.randrange(0, WIDTH, BLOCK)
food_y = random.randrange(0, HEIGHT, BLOCK)

clock = pygame.time.Clock()

score = 0
running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                direction = "UP"

            elif event.key == pygame.K_DOWN:
                direction = "DOWN"

            elif event.key == pygame.K_LEFT:
                direction = "LEFT"

            elif event.key == pygame.K_RIGHT:
                direction = "RIGHT"

    head_x, head_y = snake[0]

    if direction == "UP":
        head_y -= BLOCK

    elif direction == "DOWN":
        head_y += BLOCK

    elif direction == "LEFT":
        head_x -= BLOCK

    elif direction == "RIGHT":
        head_x += BLOCK

    snake.insert(0, (head_x, head_y))

    if head_x == food_x and head_y == food_y:

        score += 1
        food_x = random.randrange(0, WIDTH, BLOCK)
        food_y = random.randrange(0, HEIGHT, BLOCK)

    else:
        snake.pop()

    if (
        head_x < 0 or head_x >= WIDTH or
        head_y < 0 or head_y >= HEIGHT or
        (head_x, head_y) in snake[1:]
    ):
        running = False

    screen.fill(BLACK)

    pygame.draw.rect(screen, RED,
                     (food_x, food_y, BLOCK, BLOCK))

    for segment in snake:
        pygame.draw.rect(screen, GREEN,
                         (segment[0], segment[1], BLOCK, BLOCK))

    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(10)

pygame.quit()