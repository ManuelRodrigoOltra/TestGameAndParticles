# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame
from sys import exit
import math as mt
from drawer.sprites import AnimatedPlayer, BackGroundScroll, BackGroundFile
from random import randint
from common.utils import FPSCounter, debug, mouse_pointer
from particles.particles_generator import particles_basic, Particles_Shot, Spark
from drawer.back_ground import Background_Rect, Background_Particle_Square



#TO IMPLEMENT:
# BACKGROUND WITH RECTANBLES AND PARTICLES RANDOM APEARING
# SHOT GLOW IMPROVEMENT
# INCLUDE DIRECTION IN THE SPARKS (REVERSE NORMAL DIRECTION)
# MOUSE TIL THE END OF SCREEN (LEFT PART)
# TEST CRASH




FPS = 90

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
    hit_list = collision_test(rect, tiles)

    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_type['right'] = True
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
    # newRec = pygame.Rect(rect.x, rect.y, rect.width, rect.height)
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list



if __name__ == '__main__':

    pygame.init()

    collisions = {'top': False, 'bottom': False, 'left': False, 'right': False}

    game_map = load_map('C:/Users/manue/PycharmProjects/FirstGamePyGame/assets/scenes/level1')
    screen_width, screen_height = 1200, 1000 #600, 800
    # screen = pygame.display.set_mode((screen_width, screen_height))
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('FistPyGame')
    pygame.mouse.set_visible(False)

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
    shot_enable = True
    shot_cadence = 60/2
    bullet_speed = 15
    sparks = []

    moving_right = False
    moving_left = False

    key_state = pygame.key.get_pressed()

    jump_height = 80
    player_speed = 3

    scroll = [1664, 890]
    true_scroll = [1664, 890]


    #BackGround
    background_objects = [[0.25,[120,10,70,400]],[0.25,[280,30,40,400]],[0.5,[30,40, 90, 200]]]
    rects_to_draw = []
    n_rect_bg = 13
    bg_start_height = -500
    bg_sep_rect = 160
    bg_width_rect = 60
    bg_angle = 120

    bg_particles_square = []
    bg_particles_square_hole = []
    bg_enable_particle = True

    bg_color = [200,191,231]
    bg_rect_color = [147, 147, 255]
    spark_color = [166, 129, 0]


    n_frame = 0

    font = pygame.font.Font(None, 36)
    green = [255, 255, 255]
    fps_counter = FPSCounter(screen, font, clock, green, (150, 10))


    player = pygame.image.load('assets/characters/Characters/character_0001.png')
    # player_rect = player.get_rect(center=(screen_width/2, 0))
    player_rect = player.get_rect(center=(1664, 890))
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


    tiles_width = 32
    tiles_height = 32
    # tiles_width = tiles_1_rect.width
    # tiles_height = tiles_1_rect.height


    #particles----------------------------------------------------------------------------------------
    #[loc, velocity, timer]
    # particles = []
    particles = particles_basic(screen)
    shots = Particles_Shot()

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
                        if animation is not 'jump' and animation is not 'fall':
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
                        if animation is not 'jump' and animation is not 'fall':
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

            n_frame += 1
            if n_frame > FPS+1:
                n_frame = 0

            if collisions['bottom']:
                if player_movement[0] > 0:
                    animation='right'
                elif player_movement[0] < 0:
                    animation = 'left'
                else:
                    animation = 'idle'

            true_scroll[0] += (player_rect.x - true_scroll[0] - screen_width/2)/15
            true_scroll[1] += (player_rect.y - true_scroll[1] - screen_height/2)/15
            scroll = true_scroll.copy()
            scroll[0] = int(scroll[0])
            scroll[1] = int(scroll[1])

            #This pos is take as reference from the player
            offset_player = (player_rect.x - (screen_width / 2 + scroll[0]), 0)
            screen.fill(bg_color)


            #####################################################################################
            #BackGround particle generator
            if not bg_particles_square:
                for it in range(20):
                    bg_particles_square.append(
                        Background_Particle_Square([randint(0, screen_width), randint(0, screen_height)],
                                                   [randint(-3, 3) / 3, randint(10, 30) / 40],
                                                   randint(1, 20)))

            #TODO, revisar los cuadrados, no se generan nuevos
            # if int(n_frame/20) == 1 and bg_enable_particle:
            #     bg_enable_particle = False
            #     bg_particles_square.append(
            #         Background_Particle_Square([randint(0, screen_width), -40], [randint(-3, 3) / 3, randint(10, 30)/40],
            #                                    randint(1, 20)))
            # elif not bg_enable_particle and int(n_frame/20) is not 1:
            #     bg_enable_particle = True

            for i, bg_particle_square in sorted(enumerate(bg_particles_square)):
                if not 0 < bg_particle_square.loc[0] < screen_width or not -50 < bg_particle_square.loc[1] < screen_height:
                    bg_particles_square.pop(i)
                    bg_particles_square.append(
                        Background_Particle_Square([randint(0, screen_width), -40],
                                                   [randint(-3, 3) / 3, randint(10, 30) / 40],
                                                   randint(1, 20)))

            for bg_particle_square in bg_particles_square:
                bg_particle_square.move()
                surf_bg = pygame.transform.rotate(bg_particle_square.draw(), bg_particle_square.angle)
                screen.blit(surf_bg, bg_particle_square.loc)
########################################################################################################################
            if not bg_particles_square_hole:
                for it in range(20):
                    bg_particles_square_hole.append(
                        Background_Particle_Square([randint(0, screen_width), randint(0, screen_height)],
                                                   [randint(-3, 3) / 3, -1*randint(10, 30) / 40],
                                                   randint(20, 50),80, 80,5))


            for i, bg_particle_square_hole in sorted(enumerate(bg_particles_square_hole)):
                if not -100 < bg_particle_square_hole.loc[0] < screen_width+100 or not -200 < bg_particle_square_hole.loc[1] < screen_height +150:
                    bg_particles_square_hole.pop(i)
                    bg_particles_square_hole.append(
                        Background_Particle_Square([randint(0, screen_width), screen_height + 80],
                                                   [randint(-3, 3) / 3, -1 * randint(10, 30) / 40],
                                                   randint(20, 50),80, 80,5))

            for bg_particle_square_hole in bg_particles_square_hole:
                bg_particle_square_hole.move()
                surf_bg = pygame.transform.rotate(bg_particle_square_hole.draw(), bg_particle_square_hole.angle)
                screen.blit(surf_bg, bg_particle_square_hole.loc)

#########################################################################################################

            if not rects_to_draw:
                for rect_bg in range(n_rect_bg):
                    rects_to_draw.append(Background_Rect([screen_width/2, (rect_bg*bg_sep_rect) + bg_start_height],
                                                         bg_rect_color, bg_angle, screen_width, bg_width_rect))

            for i, rect_to_draw in sorted(enumerate(rects_to_draw)):
                rect_to_draw.move([0,0.3], 1)
                rect_to_draw.draw(screen)
                if rect_to_draw.loc[1] > screen_height*2:
                    rects_to_draw.pop(i)
                if i==0 and rect_to_draw.loc[1] > bg_start_height + bg_sep_rect:
                    rects_to_draw.insert(0,
                        Background_Rect([screen_width/2, bg_start_height], bg_rect_color, bg_angle,
                                        screen_width, bg_width_rect))





            #####################################################################################
            if int(n_frame/20) and (n_frame/20)%1 == 0 and animation is not 'idle':
                p_pos = [player_rect.midbottom[0],
                            player_rect.midbottom[1]-7]
                p_mov = [-player_movement[0]/4, - player_movement[1]/8]
                p_size = randint(8,10)
                particles.add_particle(p_pos, p_mov, p_size)
                particles.itera_draw(screen, scroll)

            particles.itera_draw(screen, scroll)

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
                                tiles_show_x = abs(player_rect.x - scroll[0] - pos_tiles_x) < \
                                               screen_width/2 + 5 * tiles_width
                                tiles_show_y = abs(player_rect.y - scroll[1] - pos_tiles_y) < \
                                               screen_height/2 + 5 * tiles_height
                                if tiles_show_x and tiles_show_y:
                                    screen.blit(tiles_1_surface, (pos_tiles_x, pos_tiles_y))
                                    tile_rects.append(pygame.Rect(tiles_1_rect.x + tiles_width * x,
                                                                  tiles_1_rect.y + 5 + tiles_height * y,
                                                                  tiles_width, tiles_height-5))

                            if game_map[y][x] == str(2):
                                pos_tiles_x = (tiles_rect.x + tiles_width * x) - scroll[0]
                                pos_tiles_y = (tiles_rect.y + tiles_height * y) - scroll[1]
                                tiles_show_x = abs(player_rect.x - scroll[0] - pos_tiles_x) < \
                                               screen_width/2 + 5 * tiles_width
                                tiles_show_y = abs(player_rect.y - scroll[1] - pos_tiles_y) < \
                                               screen_height/2 + 5 * tiles_height
                                if tiles_show_x and tiles_show_y:
                                    screen.blit(tree_1_surface, (pos_tiles_x - 24, pos_tiles_y - tree_1_rect.height +32))
                        x += 1
                y += 1

            player_movement[0] = 0
            if moving_right == True:
                player_movement[0] += player_speed
            if moving_left:
                player_movement[0] -= player_speed

            if collisions['bottom']:
                air_timer = 0
                vertical_momentum = 0

            elif collisions['top']:
                air_timer = 10000
                vertical_momentum = 0
            else:
                air_timer += 1

            vertical_momentum += 0.2

            if vertical_momentum > 6:
                vertical_momentum = 6

            if collisions['bottom']:
                vertical_momentum = 0

            player_movement[1] = vertical_momentum

            if player_movement == [0, 0]:
                animation = 'idle'

            mx, my = pygame.mouse.get_pos()
            ml, mc, mr = pygame.mouse.get_pressed(3)


            if ml and shot_enable:
                shots.add_shot(player_rect.x, player_rect.y, mx + offset_player[0], my + offset_player[1], bullet_speed, scroll)
                shot_enable = False
                shot_cadence = 30

            if shot_cadence > 0:
                shot_cadence -= 1
            else:
                shot_cadence = 0
                shot_enable = True

            for i, spark in sorted(enumerate(sparks), reverse=True):
                spark.move(1)
                spark.draw(screen, scroll)
                if not spark.alive:
                    sparks.pop(i)


            index_to_remove = []
            for it in range(len(shots.list_shots)):
                rect_shot = pygame.Rect(shots.list_shots[it][0][0], shots.list_shots[it][0][1], 2.5, 2.5)
                collision_shot = collision_test(rect_shot, tile_rects)
                if collision_shot:
                    for sp in range(15):
                        sparks.append(Spark([shots.list_shots[it][0][0],shots.list_shots[it][0][1]], mt.radians(randint(0,360)),randint(1,3), spark_color, 2))
                    index_to_remove.append(it)

                elif abs(player_rect.x - shots.list_shots[it][0][0]) > screen_width/2 or abs(player_rect.y - shots.list_shots[it][0][1]) > screen_height/2:
                    index_to_remove.append(it)

            index_to_remove.sort(reverse=True)
            for rm_indx in index_to_remove:
                shots.remove(rm_indx)

            shots.itera_draw(screen, scroll)
            screen.blit(mouse_pointer(radius=10), (mx + offset_player[0],my + offset_player[1]))

            screen.blit(player, (player_rect.x - scroll[0], player_rect.y - scroll[1]))
            player_rect, collisions = move(player_rect, player_movement, tile_rects)


            fps_counter.render()
            fps_counter.update()
            pygame.display.update()
            clock.tick(FPS)