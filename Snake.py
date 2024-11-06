import pygame
import random

pygame.init()

# Screen dimensions
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# Snake properties
snake_block = 10
snake_speed = 15
x1 = screen_width / 2
y1 = screen_height / 2

# Initial snake length
length_of_snake = 1
snake_List = []
snake_List.append([x1, y1])

# Food coordinates
food_x = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
food_y = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0

# Game over flag
game_over = False

# Movement control
x_change = 0
y_change = 0

def your_snake(snake_block, snake_list):
    for i in range(len(snake_list)):
        if i % 2 == 0:
            pygame.draw.rect(screen, blue, [snake_list[i][0], snake_list[i][1], snake_block, snake_block])
        else:
            pygame.draw.rect(screen, yellow, [snake_list[i][0], snake_list[i][1], snake_block, snake_block])

def your_food(foodx, food_y):
    pygame.draw.rect(screen, green, [food_x, food_y, snake_block, snake_block])

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -snake_block
                y_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = snake_block
                y_change = 0
            elif event.key == pygame.K_UP:
                y_change = -snake_block
                x_change = 0
            elif event.key == pygame.K_DOWN:
                y_change = snake_block
                x_change = 0

    # Update snake position
    x1 += x_change
    y1 += y_change

    # Check for collision with boundaries
    if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
        game_over = True

    # Check for self-collision
    for x in snake_List[:-1]:
        if x == [x1, y1]:
            game_over = True

    # Add new head to snake list
    snake_List.append([x1, y1])

    # Remove the tail segment if the snake is growing
    if len(snake_List) > length_of_snake:
        del snake_List[0]

    # Draw the game elements
    screen.fill(white)
    your_snake(snake_block, snake_List)
    your_food(food_x, food_y)
    pygame.display.update()

    # Check for food collision
    if x1 == food_x and y1 == food_y:
        length_of_snake += 1
        food_x = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
        food_y = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0

    pygame.time.Clock().tick(snake_speed)

pygame.quit()
quit()