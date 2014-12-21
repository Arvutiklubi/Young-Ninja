__author__ = 'Joonatan Samuel'

import pygame

pygame.init()

# Initiating Display
cube_size = 25
Width, Height = 40, 30
screen = pygame.display.set_mode((Width * cube_size, Height * cube_size))

# Player cube
dx, dy, ddx, ddy = 0, 0, 0, 0

player = pygame.Rect(0, 0, cube_size, cube_size)
player_color = (255, 255, 255)
speed, jump_power, gravity = 2, 8, 0.08

# Generate map out of rectangle objects
def generate_map(cubes_x):
    map_list = []
    # generates ground
    for i in range(cubes_x):
        map_list.append(pygame.Rect(i*cube_size, (Height - 1)*cube_size, cube_size, cube_size))

    return map_list

map_list = generate_map(55)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            # arrow keys
            if event.key == pygame.K_LEFT:
                dx = -speed
            elif event.key == pygame.K_RIGHT:
                dx = speed
            elif event.key == pygame.K_UP:
                dy = -jump_power
        elif event.type == pygame.KEYUP:
            # stop moving
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                dx = 0

    dy += gravity
    player.x += dx
    player.y += 2 + dy

    # Draw on screen
    screen.fill((0, 0, 0))
    screen.fill(player_color, player)

    for rect in map_list:
        screen.fill((100, 200, 200), rect)

    pygame.display.flip()
    pygame.time.wait(5)