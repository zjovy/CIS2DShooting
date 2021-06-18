'''
The characters, enemies, and background image:
https://craftpix.net/freebies/free-wraith-tiny-style-2d-sprites/
https://craftpix.net/freebies/free-elven-land-game-battle-backgrounds/
''''

import pygame
from random import randrange

# initialising The Game Space
pygame.init()

# size of the screen
width = 1150
height = 800

game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption("2D Shooting")

# upload images of character, background, and enemy
# and resize each image
character = pygame.image.load('Moving00.png')
mainRole = pygame.transform.scale(character, (250, 200))
bg = pygame.image.load('game_background_1.png')
bgSize = pygame.transform.scale(bg, (1150, 800))
enemy = pygame.image.load('Enemy1.png')
newEnemy = pygame.transform.scale(enemy, (250, 200))

x = (width * 0.5)
y = (height * 0.5)

enemy_x_pos = 0
enemy_y_pos = randrange(height)
enemy_speed = 2

# originate the location of character
def add_enemy_at_location(x, y):
    game_display.blit(newEnemy, (x, y))

# originate random location of enemy
def add_character_at_location(x,y):
    game_display.blit(mainRole,(x,y))

width_of_character = 60
width_of_enemy = 60
height_of_character = 91
height_of_enemy = 91

# when the collision happens, the game ends or the character loses health (plan)
def collosion_has_occured():
    enemy_top_right_x = enemy_x_pos + width_of_enemy
    enemy_top_right_y = enemy_y_pos
    enemy_bottom_right_x = enemy_x_pos + width_of_enemy
    enemy_bottom_right_y = enemy_y_pos - height_of_enemy

    character_top_left_x = x
    character_top_left_y = y
    character_bottom_left_x = x
    character_bottom_left_y = y - height_of_character

    if enemy_bottom_right_x >= character_top_left_x and enemy_bottom_right_y <= character_top_left_y and enemy_bottom_right_y >=character_bottom_left_y:
        return True
    if enemy_top_right_x >= character_top_left_x and enemy_top_right_y <= character_top_left_y and enemy_top_right_y >=character_bottom_left_y:
        return True

    return False

# boolean variables for character movement
move_left = False
move_right = False
move_down = False
move_up = False

# Game Looper
running = True
while running:
    # Testing For Events
    # Events Section
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Character movement
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_RIGHT):
                move_right = True
            if(event.key == pygame.K_LEFT):
                move_left = True
            if(event.key == pygame.K_DOWN):
                move_down = True
            if(event.key == pygame.K_UP):
                move_up = True
        elif(event.type == pygame.KEYUP):
            if (event.key == pygame.K_RIGHT):
                move_right = False
            if (event.key == pygame.K_LEFT):
                move_left = False
            if (event.key == pygame.K_DOWN):
                move_down = False
            if (event.key == pygame.K_UP):
                move_up = False
    # Speed of movement
    if(move_right):
        x += 2
    if(move_left):
        x -= 2
    if(move_up):
        y -= 2
    if(move_down):
        y += 2

    # Enemy movement and location
    enemy_x_pos += enemy_speed
    if enemy_x_pos >= width:
        enemy_x_pos = 0
        enemy_y_pos = randrange(height)

    # Boundary of the game
    if y <= 0:
        move_up = False
    if y >= height - height_of_character*2:
        move_down = False
    if x <= -100:
        move_left = False
    if x >= width- width_of_character*3:
        move_right = False


    # Draw Section
    game_display.blit(bgSize, (0, 0))
    add_character_at_location(x,y)
    add_enemy_at_location(enemy_x_pos, enemy_y_pos)

    if collosion_has_occured():
        running = False

    pygame.display.update()

pygame.quit()
