# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame
from sys import exit
from drawer.sprites import AnimatedPlayer, BackGroundScroll, BackGroundFile
from random import randint
from common.utils import FPSCounter


def load_map(path):
    map = []
    file = open(path + '.txt', 'r')
    data = file.read()
    file.close()
    data = data.split('\n')
    for row in data:
        map.append(list(row))
    return map



def move (rect, movement, tiles):
    collision_type = {'top': False, 'bottom': False, 'left': False, 'right': False}
    rect.x += movement[0]
    hit_list = collision_test(rect, tiles, 1)

    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_type['right'] = True
        if movement[0] < 0:
            rect.left = tile.right
            collision_type['left'] = True
    rect.y += movement[1]
    hit_list = collision_test(rect, tiles, 1)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_type['bottom'] = True
        if movement[1] < 0:
            rect.top = tile.bottom
            collision_type['top'] = True

    return rect, collision_type


def collision_test(rect, tiles, shrink_rect):
    hit_list = []
    newRec = pygame.Rect(rect.x, rect.y, rect.width/shrink_rect, rect.height)
    for tile in tiles:
        if newRec.colliderect(tile):
            hit_list.append(tile)
    return hit_list




if __name__ == '__main__':

    pygame.init()

    collisions = {'top': False, 'bottom': False, 'left': False, 'right': False}

    game_map = load_map('C:/Users/manue/PycharmProjects/FirstGamePyGame/assets/scenes/level1')
    screen_width, screen_height = 600, 800
    # screen = pygame.display.set_mode((screen_width, screen_height))
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('FistPyGame')

    clock = pygame.time.Clock()
    title_font = pygame.font.Font(None, 50)

    game_active = True

    vertical_momentum = 0
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
    player_speed = 3

    scroll = [0,0]
    true_scroll = [0,0]

    background_objects = [[0.25,[120,10,70,400]],[0.25,[280,30,40,400]],[0.5,[30,40, 90, 200]]]



    font = pygame.font.Font(None, 36)
    green = [255, 255, 255]
    fps_counter = FPSCounter(screen, font, clock, green, (150, 10))

    # animation_files_player = {'idle':'assets/characters/EVil Wizard 2/Sprites/Idle.png',
    #                    'right':'assets/characters/EVil Wizard 2/Sprites/Run.png',
    #                    'left': 'assets/characters/EVil Wizard 2/Sprites/Run.png',
    #                    'fall':'assets/characters/EVil Wizard 2/Sprites/Fall.png',
    #                    'jump':'assets/characters/EVil Wizard 2/Sprites/Jump.png',
    #                    'attack': 'assets/characters/EVil Wizard 2/Sprites/Attack1.png',
    #                    'hit': 'assets/characters/EVil Wizard 2/Sprites/Take hit.png',
    #                    'death': 'assets/characters/EVil Wizard 2/Sprites/Death.png',
    #                    'down': None,
    #                    }

    player = pygame.image.load('assets/characters/Characters/character_0001.png')
    player_rect = player.get_rect(center=(screen_width/2, 0))
    player_rect = pygame.Rect(player_rect.center[0], player_rect.center[1], player_rect.width-5, player_rect.height)
    player_movement = [0, 0]

    # tiles_surface = pygame.image.load('assets\scenes\Block\Tiles.png')
    tiles_surface = pygame.image.load('assets\scenes\Block/Tile_1.png')
    tiles_rect = tiles_surface.get_rect()

    tiles_1_surface = pygame.image.load('assets\scenes\Block/T1.png').convert_alpha()
    tiles_1_rect = tiles_1_surface.get_rect()
    tiles_1_rect.height = tiles_1_rect.height - 15


    tiles_2_surface = pygame.image.load('assets\scenes\Block/Tiles_2.png').convert_alpha()
    tiles_2_rect = tiles_1_surface.get_rect()

    tree_1_surface = pygame.image.load('assets\scenes\Block/tree_1.png').convert_alpha()
    tree_1_rect = tree_1_surface.get_rect()

    # player = AnimatedPlayer(animation_files_player)
    # player.move_speed = move_speed
    # player_sprite= player.get_animation(animation,250,250)
    # player_rect = pygame.Rect(0,0,60,98)
    #
    # player_rect.x = screen_width/2
    #
    # player.speed_animation = (0.3, 0)
    # player_movement = [0, 0]

    tiles_rects = []
    tiles_width = 35
    tiles_height = 35
    # tiles_width = tiles_1_rect.width
    # tiles_height = tiles_1_rect.height

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
                        animation = 'right'
                        moving_right = True
                        moving_left = False

                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        # MOVE RIGHT
                        if air_timer < 30 and not (collisions['bottom'] or collisions['top']):
                            animation = 'jump'
                            vertical_momentum += -5

                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        # MOVE LEFT
                        animation = 'left'
                        moving_right = False
                        moving_left = True


                    # if key_state[pygame.K_f] :
                    #     if animation_files_player['attack'] == 'assets/characters/EVil Wizard 2/Sprites/Attack1.png':
                    #         animation_files_player['attack'] = 'assets/characters/EVil Wizard 2/Sprites/Attack2.png'
                    #     else:
                    #         animation_files_player['attack'] = 'assets/characters/EVil Wizard 2/Sprites/Attack1.png'
                    #     player.animation_files = animation_files_player


                if event.type == pygame.KEYUP:
                    key_state = pygame.key.get_pressed()

                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        moving_right = False
                        moving_left = False

                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        moving_left = False
                        moving_right = False



            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        game_active = True


        ######################## PASAMOS AL JUEGO ########################
        if game_active:
            true_scroll[0] += (player_rect.x - true_scroll[0] - screen_width/2)/15
            true_scroll[1] += (player_rect.y - true_scroll[1] - screen_height/2)/15
            scroll = true_scroll.copy()
            scroll[0] = int(scroll[0])
            scroll[1] = int(scroll[1])

            screen.fill((146, 244, 255))


            pygame.draw.rect(screen,(7,80,75), pygame.Rect(0,120,300,80))

            for background_object in background_objects:
                obj_rect = pygame.Rect(background_object[1][0] - scroll[0] * background_object[0],
                                       background_object[1][1] - scroll[1] * background_object[0],
                                       background_object[1][2],  background_object[1][3])
                if background_object[0] == 0.5:
                    pygame.draw.rect(screen,(14,222,150), obj_rect)
                else:
                    pygame.draw.rect(screen, (7, 80, 75), obj_rect)


            #Pintamos el escenario
            tile_rects = []
            fill_screen = (screen_width/tiles_width + (player_rect.x - scroll[0])/tiles_width,
                           screen_height/tiles_height + (player_rect.y - scroll[1])/tiles_height)
            #fill_screen = (screen_width/tiles_width,screen_height/tiles_height )
            pos_center_tiles = (player_rect.x/tiles_width,player_rect.y/tiles_height)

            limits_width = (round(pos_center_tiles[0] + fill_screen[0]/2), round(pos_center_tiles[0] - fill_screen[0]/2))
            limits_height = (round(pos_center_tiles[1] + fill_screen[1]/2),round(pos_center_tiles[1] - fill_screen[1]/2))
            y = 0
            for row in game_map:
                x = 0
                if limits_height[0] > y > limits_height[1]:
                    for col in row:
                        if limits_width[0] > x > limits_width[1]:


                            if game_map[y][x] == str(1):
                                pos_tiles_x = (tiles_1_rect.x + tiles_width * x) - scroll[0]
                                pos_tiles_y = (tiles_1_rect.y + tiles_height * y) - scroll[1]
                                tiles_show_x = abs(player_rect.x - scroll[0] - pos_tiles_x) < screen_width/2 + 5 * tiles_width
                                tiles_show_y = abs(player_rect.y - scroll[1] - pos_tiles_y) < screen_height/2 + 5 * tiles_height
                                if tiles_show_x and tiles_show_y:
                                    screen.blit(tiles_1_surface, (pos_tiles_x, pos_tiles_y))
                                    tile_rects.append(pygame.Rect(tiles_1_rect.x + tiles_width * x,tiles_1_rect.y + 5 + tiles_height * y, tiles_width, tiles_height-5))

                            if game_map[y][x] == str(2):
                                pos_tiles_x = (tiles_rect.x + tiles_width * x) - scroll[0]
                                pos_tiles_y = (tiles_rect.y + tiles_height * y) - scroll[1]
                                tiles_show_x = abs(player_rect.x - scroll[0] - pos_tiles_x) < screen_width/2 + 5 * tiles_width
                                tiles_show_y = abs(player_rect.y - scroll[1] - pos_tiles_y) < screen_height/2 + 5 * tiles_height
                                if tiles_show_x and tiles_show_y:
                                    screen.blit(tree_1_surface, (pos_tiles_x, pos_tiles_y - tree_1_rect.height))
                                    # tile_rects.append(pygame.Rect(tiles_rect.x + tiles_width * x,tiles_rect.y + tiles_height * y, tiles_width, tiles_height))
                        x += 1
                y += 1

            player_movement[0] = 0
            if moving_right == True:
                player_movement[0] += player_speed
            if moving_left == True:
                player_movement[0] -= player_speed

            if collisions['bottom'] == True:
                air_timer = 0
                vertical_momentum = 0

            elif collisions['top'] == True:
                air_timer = 10000
                vertical_momentum = 0
            else:
                air_timer += 1


            vertical_momentum += 0.1

            if vertical_momentum > 6:
                vertical_momentum = 6

            if collisions['bottom']:
                vertical_momentum = 0

            player_movement[1] = vertical_momentum

            # player_sprite = player.get_animation(animation, 250,250)
            # screen.blit(player_sprite, player_rect)



            screen.blit(player, (player_rect.x - scroll[0], player_rect.y - scroll[1]))
            player_rect, collisions = move(player_rect, player_movement, tile_rects)






            fps_counter.render()
            fps_counter.update()
            pygame.display.update()
            clock.tick(60)