# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame
from sys import exit
from drawer.sprites import AnimatedPlayer, BackGroundScroll, BackGroundFile
from random import randint
from common.utils import FPSCounter



#TODO examinar las key por igual cuando apretamos y levantamos
def key_conditions():
    pass


scene1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]



def move (rect, movement, tiles):
    collision_type = {'top': False, 'bottom': False, 'left': False, 'right': False}
    rect.x += movement[0]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_type['rigth'] = True
        if movement[0] < 0:
            rect.left = tile.right
            collision_type['left'] = True

    rect.y += movement[1]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_type['bottom'] = True
        if movement[1] < 0:
            rect.top = tile.bottom
            collision_type['top'] = True
    return rect, collision_type


def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list


if __name__ == '__main__':
    pygame.init()
    screen_width, screen_height = 600, 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('FistPyGame')
    clock = pygame.time.Clock()
    title_font = pygame.font.Font(None, 50)
    game_active = True
    player_gravity = 0
    direction_player_right = True
    animation = 'idle'
    player_attack_speed = 0.6
    attack_animation = 0
    move_speed = 5
    air_timer = 0


    moving_right = False
    moving_left = False

    key_state = pygame.key.get_pressed()

    jump_height = 80

    #Esto es un apanyo temporal
    moving = False
    move_background = (0, 0)


    ground_surface = pygame.image.load('assets/scenes/my assets/ground block 2.png')
    ground_box = ground_surface.get_rect(center = (0, 0))

    font = pygame.font.Font(None, 36)
    green = [255, 255, 255]
    fps_counter = FPSCounter(screen, font, clock, green, (150, 10))


    animation_files_player = {'idle':'assets/characters/EVil Wizard 2/Sprites/Idle.png',
                       'right':'assets/characters/EVil Wizard 2/Sprites/Run.png',
                       'left': 'assets/characters/EVil Wizard 2/Sprites/Run.png',
                       'fall':'assets/characters/EVil Wizard 2/Sprites/Fall.png',
                       'jump':'assets/characters/EVil Wizard 2/Sprites/Jump.png',
                       'attack': 'assets/characters/EVil Wizard 2/Sprites/Attack1.png',
                       'hit': 'assets/characters/EVil Wizard 2/Sprites/Take hit.png',
                       'death': 'assets/characters/EVil Wizard 2/Sprites/Death.png',
                       'down': None,
                       }

    tiles_surface = pygame.image.load('assets\scenes\Block\Tiles.png')
    tiles_rect = tiles_surface.get_rect()


    player = AnimatedPlayer(animation_files_player)
    player.move_speed = move_speed

    player.x = (screen_width / 2)
    player.y = (screen_height/2)
    player.speed_animation = (0.3, 0)
    player_movement = [0, 0]


    screen.fill((146, 244, 255))

########################################################################################################################
    ########################  BUCLE PRINCIPAL ########################
    while True:



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            ######################## ENTRADAS TECLADO ########################
            if game_active:

                if event.type == pygame.KEYDOWN:
                    key_state = pygame.key.get_pressed()

                    if event.key == pygame.K_SPACE and (animation is not 'jump' and animation is not 'fall'):
                        animation = 'attack'
                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        pass
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        # MOVE RIGHT
                        move_background = (-1 * move_speed, move_background[1])
                        player.right = True
                        player.left = False

                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        # MOVE LEFT
                        move_background = (move_speed, move_background[1])
                        player.right = False
                        player.left = True

                    if key_state[pygame.K_f] :
                        if animation_files_player['attack'] == 'assets/characters/EVil Wizard 2/Sprites/Attack1.png':
                            animation_files_player['attack'] = 'assets/characters/EVil Wizard 2/Sprites/Attack2.png'
                        else:
                            animation_files_player['attack'] = 'assets/characters/EVil Wizard 2/Sprites/Attack1.png'
                        player.animation_files = animation_files_player


                    if event.type == pygame.KEYUP:
                        key_state = pygame.key.get_pressed()

            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        game_active = True


        ######################## PASAMOS AL JUEGO ########################
        if game_active:


            #Pintamos el escenario
            tile_rects = []
            y = 0
            tiles_width = tiles_rect.width
            tiles_height = tiles_rect.height
            for row in scene1:
                x = 0
                for col in row:
                    if scene1[y][x] == 1:
                        screen.blit(tiles_surface, (tiles_rect.x + tiles_width * x, tiles_rect.y + tiles_height * y, tiles_width, tiles_height))
                        tile_rects.append(pygame.Rect(tiles_rect.x + tiles_width * x,tiles_rect.y + tiles_height * y, tiles_width, tiles_height))
                    x += 1
                y += 1



            if moving_right == True:
                player_movement[0] += 2
            if moving_left == True:
                player_movement[0] -= 2

            player_movement[1] += player_gravity
            player_gravity += 0.2
            if player_gravity > 3:
                player_gravity = 3

            player.x = player_movement[0]
            player.y = player_movement[1]

            player_rect = pygame.Rect(player.x, player.y, 250, 250)
            player_rect, collisions = move(player_rect, player_movement, tile_rects)


            if collisions['bottom'] == True:
                air_timer = 0
                player_gravity = 0
            else:
                air_timer += 1

            # screen.blit(player.get_animation(animation, 250,250), player_rect)
            if animation =='idle':
                pass
                #move_background = (0, 0)

            elif animation == 'jump':
                player_gravity -= 3

            elif animation == 'fall':
                player_gravity += 2

            elif animation == 'right':
                pass
            elif animation == 'left':
                pass
            elif animation == 'attack':
                attack_animation += player_attack_speed
                if attack_animation > 8:
                    attack_animation = 0
                if player.control_animation_x > 8:
                    if key_state[pygame.K_a] or key_state[pygame.K_LEFT]:
                        animation = 'left'
                        attack_animation = 0
                        player.right = False
                        player.left = True
                    elif key_state[pygame.K_d] or key_state[pygame.K_RIGHT]:
                        animation = 'right'
                        attack_animation = 0
                        player.right = True
                        player.left = False
                    else:
                        animation = 'idle'
                        move_background = (0, 0)

            else:
                animation = 'idle'
                move_background = (0, 0)
                player.left = True
                player.right = False



            player.draw(screen,animation, 250,250)

            fps_counter.render()
            fps_counter.update()
            pygame.display.update()
            clock.tick(60)