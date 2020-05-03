import pygame
import os
import random

# Run module
pygame.init()

# Centering the game window
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Game Screen / Display
scr_wdh = 800
scr_wdh_cr = int(scr_wdh / 2)
scr_hgt = 800
scr_hgt_cr = int(scr_hgt / 2)
scr_color = (0, 0, 0)

screen = pygame.display.set_mode((scr_wdh, scr_hgt))
pygame.display.set_caption("Snake by marsiekiera")

# Snake attributes, snake speed - lower=slower
snake_color = (0, 102, 0)
snake_size = int(scr_wdh / 20)
snake_speed = 8

# Main Game
clock = pygame.time.Clock()

font_style = pygame.font.SysFont("Arial", snake_size)
score_font = pygame.font.SysFont("Verdana", int(snake_size / 2))


def Your_score(score):
    value = score_font.render("Your score: " + str(score), True, (255, 255, 0))
    screen.blit(value, [0, 0])


def snake(snake_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, snake_color, [x[0], x[1], snake_size, snake_size])


def messsage(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [snake_size, scr_hgt_cr])


def game_loop():
    game_over = False
    game_close = False

    # Start position and movement of Snake
    x1 = scr_wdh_cr
    y1 = scr_hgt_cr
    x1_change = 0
    y1_change = 0

    snake_List = []
    Lenght_of_snake = 1

    # Snake food
    food_x = random.randrange(0, scr_wdh - snake_size, snake_size)
    food_y = random.randrange(0, scr_hgt - snake_size, snake_size)
    food_color = (255, 255, 0)

    while not game_over:

        while game_close == True:
            screen.fill(scr_color)
            messsage("GAME OVER. Press Q to Quit or P to Play again", (255, 255, 0))
            Your_score((Lenght_of_snake - 1))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = - snake_size
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_size
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_size
                    y1_change = 0
                elif event.key == pygame.K_LEFT:
                    x1_change = - snake_size
                    y1_change = 0

        if x1 > scr_wdh or x1 < 0 or y1 > scr_hgt or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(scr_color)
        pygame.draw.rect(screen, food_color, [food_x, food_y, snake_size, snake_size])  # food
        # snake
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_List.append(snake_head)
        if len(snake_List) > Lenght_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_head:
                game_close = True
        snake(snake_size, snake_List)
        Your_score(Lenght_of_snake - 1)
        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = random.randrange(0, scr_wdh - snake_size, snake_size)
            food_y = random.randrange(0, scr_hgt - snake_size, snake_size)
            Lenght_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()