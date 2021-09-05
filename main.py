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


file = [0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,
        0,1,1,1,1,1,0,0,0,0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 1, 1, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 1, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0,0,0,0,0,0,0,0,0,0]



if __name__ == '__main__':
    pygame.init()
    screen_width, screen_height = 460, 540
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

    key_state = pygame.key.get_pressed()
    key_state_previous = pygame.key.get_pressed()

    jump_height = 80

    #Esto es un apanyo temporal
    moving = False
    move_background = (0, 0)
    floor = screen_height - 100

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

    animation_files_enemy = {'idle':'assets/characters/Martial Hero 2/Sprites/Idle.png',
                       'right':'assets/characters/Martial Hero 2/Sprites/Run.png',
                       'left': 'assets/characters/Martial Hero 2/Sprites/Run.png',
                       'fall':'assets/characters/Martial Hero 2/Sprites/Fall.png',
                       'jump':'assets/characters/Martial Hero 2/Sprites/Jump.png',
                       'attack': 'assets/characters/Martial Hero 2/Sprites/Attack1.png',
                       'hit': 'assets/characters/Martial Hero 2/Sprites/Take hit.png',
                       'death': 'assets/characters/Martial Hero 2/Sprites/Death.png',
                       'down': None,
                       }

    back_ground_imges = ['assets/scenes/Free Pixel Art Forest/PNG/Background layers/Layer_0010_1.png',
                         'assets/scenes/Free Pixel Art Forest/PNG/Background layers/Layer_0009_2.png',
                         'assets/scenes/Free Pixel Art Forest/PNG/Background layers/Layer_0008_3.png',
                         'assets/scenes/Free Pixel Art Forest/PNG/Background layers/Layer_0007_Lights.png',
                         'assets/scenes/Free Pixel Art Forest/PNG/Background layers/Layer_0006_4.png',
                         'assets/scenes/Free Pixel Art Forest/PNG/Background layers/Layer_0005_5.png',
                         'assets/scenes/Free Pixel Art Forest/PNG/Background layers/Layer_0004_Lights.png',
                         'assets/scenes/Free Pixel Art Forest/PNG/Background layers/Layer_0003_6.png',
                         'assets/scenes/Free Pixel Art Forest/PNG/Background layers/Layer_0002_7.png',
                         'assets/scenes/Free Pixel Art Forest/PNG/Background layers/Layer_0001_8.png',
                         'assets/scenes/Free Pixel Art Forest/PNG/Background layers/Layer_0000_9.png']

    file_bg_images = ['assets\scenes\Block\Tiles.png']

    speed_scroll_layer = [0.05, 0.08, 0.2, 0.3, 0.4, 0.4, 0.5, 0.6, 0.6, 0.8, 1]

    # back_gorund = BackGroundScroll(back_ground_imges, screen_width,screen_height, speed_scroll_layer)
    back_ground = BackGroundFile(file_bg_images, file)
    player = AnimatedPlayer(animation_files_player)
    player.move_speed = move_speed

    enemy1 = AnimatedPlayer(animation_files_enemy)

    player.x = (screen_width / 2)
    player.y = floor
    player.speed_animation = (0.3, 0)

    enemy1.x = 2000
    enemy1.y = floor +200



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
                        print('dfasdf')
                        move_background = (-1 * move_speed, move_background[1])
                        player.right = True
                        player.left = False
                        if player.y == floor:
                            animation = 'right'
                        if (key_state[pygame.K_w] or key_state[pygame.K_UP]) and player.y == floor:
                            animation = 'jump'
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        # MOVE LEFT
                        move_background = (move_speed, move_background[1])
                        player.right = False
                        player.left = True
                        if player.y == floor:
                            animation = 'left'
                        if (key_state[pygame.K_w] or key_state[pygame.K_UP]) and player.y == floor:
                            animation = 'jump'
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        if player.y == floor:
                            animation = 'jump'

                    if key_state[pygame.K_f] :
                        if animation_files_player['attack'] == 'assets/characters/EVil Wizard 2/Sprites/Attack1.png':
                            animation_files_player['attack'] = 'assets/characters/EVil Wizard 2/Sprites/Attack2.png'
                        else:
                            animation_files_player['attack'] = 'assets/characters/EVil Wizard 2/Sprites/Attack1.png'
                        player.animation_files = animation_files_player

                    else:
                        if player.y < floor:
                            animation = 'fall'
                        else:
                            # animation = 'idle'
                            pass
                        move_background = (0,0)

                    if event.type == pygame.KEYUP:
                        key_state = pygame.key.get_pressed()
                        if event.key == pygame.K_SPACE and (player.y == floor):
                            if key_state[pygame.K_RIGHT] or key_state[pygame.K_d]:
                                animation = 'right'
                                player.right = True
                                player.left = False
                            if key_state[pygame.K_LEFT] or key_state[pygame.K_a]:
                                animation = 'left'
                                player.right = False
                                player.left = True

            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        game_active = True


        ######################## PASAMOS AL JUEGO ########################
        if game_active:

            # back_gorund.scroll_x += move_background[0]
            # back_gorund.scroll_y += move_background[1]
            # back_gorund.draw(screen)
            back_ground.draw(screen, screen_width/10, screen_height/10)

            if animation =='idle':
                move_background = (0, 0)

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



            player.y = floor + player_gravity

            # sprite_enemy1 = enemy1.get_animation(animation, 200, 200)
            # screen.blit(sprite_enemy1, (screen_width/2,screen_height/2,200,200))

            # Gravity
            # Logic after landing
            if player.y > floor:
                player.y = floor
                jump_acceleration = 0
                player_gravity = 0
                if animation == 'jump' or animation == 'fall':
                    if key_state[pygame.K_a] or key_state[pygame.K_LEFT]:
                        animation = 'left'
                        direction_player_right = False
                    elif key_state[pygame.K_d] or key_state[pygame.K_RIGHT]:
                        animation = 'right'
                        direction_player_right = True
                    else:
                        animation = 'idle'
                        move_background = (0, 0)

            if player.y < floor - jump_height:
                animation = 'fall'



            if key_state is not None:
                if player.y == floor:
                    if animation == 'right' and not(key_state[pygame.K_d] or key_state[pygame.K_RIGHT]):
                        print('fasdf')
                        animation = 'idle'
                        direction_player_right = True
                        move_background = (0, 0)
                    if animation == 'left' and not(key_state[pygame.K_a] or key_state[pygame.K_LEFT]):
                        animation = 'idle'
                        direction_player_right = False
                        move_background = (0, 0)



            player.draw(screen,animation, 250,250, player.x, player.y)

            fps_counter.render()
            fps_counter.update()
            pygame.display.update()
            clock.tick(60)