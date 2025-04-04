import pygame
import time
import random
import sys

# Initial game speed
snake_speed = 10

# Screen dimensions
window_x, window_y = 800, 600

# Colors
black, white, red, green, blue, yellow, cyan, purple = (0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (160,32,240)
background_colors = [black, blue, yellow, cyan]
current_bg_color = black

# Initialize pygame
pygame.init()

# Setup game window
pygame.display.set_caption('Snake Game')
game_window = pygame.display.set_mode((window_x, window_y))

# Frame rate controller
fps = pygame.time.Clock()

# Snake initial settings
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

# Food types with weights
food_types = {
    "small": {"color": white, "score": 10},
    "medium": {"color": purple, "score": 20},
    "large": {"color": red, "score": 30}
}

def generate_food():
    """Generate random food position ensuring it does not spawn on the snake or outside bounds."""
    while True:
        position = [random.randrange(1, window_x // 10) * 10, random.randrange(1, window_y // 10) * 10]
        if position not in snake_body:
            food_type = random.choices(list(food_types.keys()), weights=[0.6, 0.3, 0.1])[0]  # Small: 60%, Medium: 30%, Large: 10%
            return position, food_type

# Fruit settings
fruit_position, fruit_type = generate_food()
fruit_spawn = True
fruit_timer = time.time() if fruit_type == "large" else None

direction = 'RIGHT'
change_to = direction

# Score and Level tracking
score = 0
level = 1

def show_score_and_level(color, font, size):
    """Display score and level on the screen."""
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render(f'Score: {score}', True, color)
    level_surface = score_font.render(f'Level: {level}', True, color)
    game_window.blit(score_surface, score_surface.get_rect(topleft=(10, 10)))
    game_window.blit(level_surface, level_surface.get_rect(topright=(window_x - 10, 10)))

def game_over():
    font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = font.render(f'Your Score: {score}', True, red)
    game_over_rect = game_over_surface.get_rect(center=(window_x/2, window_y/4))
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

def check_wall_collision():
    """Check if the snake hits the wall."""
    if snake_position[0] < 0 or snake_position[0] >= window_x or snake_position[1] < 0 or snake_position[1] >= window_y:
        game_over()

count = 0

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_UP:
                change_to = 'UP'
            elif event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Validate direction change
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    elif change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    elif change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    elif change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Move the snake
    if direction == 'UP':
        snake_position[1] -= 10
    elif direction == 'DOWN':
        snake_position[1] += 10
    elif direction == 'LEFT':
        snake_position[0] -= 10
    elif direction == 'RIGHT':
        snake_position[0] += 10

    # Check for wall collision
    check_wall_collision()

    # Snake growth mechanism
    snake_body.insert(0, list(snake_position))
    if snake_position == fruit_position:
        score += food_types[fruit_type]["score"]
        fruit_spawn = False
        
        # Increase speed and change background color every 50 points
        if (score - count) >= 50:
            count = score
            snake_speed += 2
            current_bg_color = background_colors[(score // 50) % len(background_colors)]
            level += 1  # Increase level
        
        # Grow the snake by 2-3 segments after 50 points
        if score < 50:
            snake_body.append(snake_body[-1])
        else:
            for _ in range(random.randint(2, 3)):
                snake_body.append(snake_body[-1])
    else:
        snake_body.pop()

    if not fruit_spawn or (fruit_type == "large" and time.time() - fruit_timer >= 5):
        fruit_position, fruit_type = generate_food()
        fruit_spawn = True
        fruit_timer = time.time() if fruit_type == "large" else None

    # Render game elements
    game_window.fill(current_bg_color)
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, food_types[fruit_type]["color"], pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    # Check for self-collision
    if any(block == snake_position for block in snake_body[1:]):
        game_over()

    # Display score and level
    show_score_and_level(white, 'times new roman', 35)
    pygame.display.update()
    fps.tick(snake_speed)