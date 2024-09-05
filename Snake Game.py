import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

# Snake block size and speed
BLOCK_SIZE = 20
SPEED = 10

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')

# Clock to control the speed of the game
clock = pygame.time.Clock()

# Font for displaying score
font = pygame.font.SysFont(None, 30)

def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])

def display_score(score):
    text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(text, [10, 10])

def game_loop():
    # Initial position of the snake
    snake_list = []
    snake_length = 1
    snake_head = [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2]
    snake_list.append(snake_head)

    # Initial position of the food
    food_pos = [random.randrange(1, (SCREEN_WIDTH // BLOCK_SIZE)) * BLOCK_SIZE,
                random.randrange(1, (SCREEN_HEIGHT // BLOCK_SIZE)) * BLOCK_SIZE]

    # Initial direction of the snake
    direction = 'RIGHT'

    # Initial score
    score = 0

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    direction = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    direction = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    direction = 'RIGHT'

        # Move the snake
        if direction == 'UP':
            snake_head[1] -= BLOCK_SIZE
        elif direction == 'DOWN':
            snake_head[1] += BLOCK_SIZE
        elif direction == 'LEFT':
            snake_head[0] -= BLOCK_SIZE
        elif direction == 'RIGHT':
            snake_head[0] += BLOCK_SIZE

        # Check for collisions with boundaries
        if snake_head[0] >= SCREEN_WIDTH or snake_head[0] < 0 or snake_head[1] >= SCREEN_HEIGHT or snake_head[1] < 0:
            game_over = True

        # Check for collisions with itself
        if snake_head in snake_list[:-1]:
            game_over = True

        # If the snake eats the food
        if snake_head == food_pos:
            score += 1
            snake_length += 1
            food_pos = [random.randrange(1, (SCREEN_WIDTH // BLOCK_SIZE)) * BLOCK_SIZE,
                        random.randrange(1, (SCREEN_HEIGHT // BLOCK_SIZE)) * BLOCK_SIZE]

        # Update snake's length
        snake_list.append(list(snake_head))
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Refresh the screen
        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, [food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE])
        draw_snake(snake_list)
        display_score(score)
        pygame.display.update()

        # Control game speed
        clock.tick(SPEED)
        
    print("Game over!")
    pygame.quit()
    sys.exit()

# Start the game loop
game_loop()
