# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame
from sys import exit
from drawer.sprites import AnimatedPlayer, BackGroundScroll
from random import randint



#TODO examinar las key por igual cuando apretamos y levantamos
def key_conditions():
    pass

if __name__ == '__main__':
    pygame.init()
    screen_width, screen_height = 928, 793
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('FistPyGame')
    clock = pygame.time.Clock()
    title_font = pygame.font.Font(None, 50)
    game_active = True
    player_gravity = 0
    direction_player_right = True
    animation = 'idle'
    player_attack_speed = 0.5
    attack_animation = 0

    key_state = pygame.key.get_pressed()
    key_state_previous = pygame.key.get_pressed()

    jump_height = 80

    #Esto es un apanyo temporal
    moving = False

    move_background = (0, 0)

    floor = screen_height - 380


    # sky_surface = pygame.image.load('assets/characters/Background/sky.png').convert()
    # sky_box = sky_surface.get_rect(center = (screen_width/2, screen_height/2))





    animation_files = {'idle':'assets/characters/EVil Wizard 2/Sprites/Idle.png',
                       'right':'assets/characters/EVil Wizard 2/Sprites/Run.png',
                       'left': 'assets/characters/EVil Wizard 2/Sprites/Run.png',
                       'fall':'assets/characters/EVil Wizard 2/Sprites/Fall.png',
                       'jump':'assets/characters/EVil Wizard 2/Sprites/Jump.png',
                       'attack': 'assets/characters/EVil Wizard 2/Sprites/Attack1.png',
                       'hit': 'assets/characters/EVil Wizard 2/Sprites/Take hit.png',
                       'death': 'assets/characters/EVil Wizard 2/Sprites/Death.png',
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


    speed_scroll_layer = [0.05, 0.08, 0.2, 0.3, 0.4, 0.4, 0.5, 0.6, 0.6, 0.8, 1]

    back_gorund = BackGroundScroll(back_ground_imges, screen_width,screen_height, speed_scroll_layer)


    player = AnimatedPlayer(animation_files)
    sprite = player.get_animation(animation, 250, 250)

    player.x = (screen_width / 2) - 125 #125 es por la mitad de los 250 que mide la imagen
    player.y = floor

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if game_active:
                if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                    key_state_previous = key_state
                    key_state = pygame.key.get_pressed()
                if not key_state_previous == key_state:
                    if key_state[pygame.K_SPACE] and (animation is not 'jump' and animation is not 'fall'):
                        animation = 'attack'
                    elif key_state[pygame.K_s] or key_state[pygame.K_DOWN]:
                        pass
                    elif key_state[pygame.K_d] or key_state[pygame.K_RIGHT]:
                        # MOVE RIGHT
                        move_background = (-3, move_background[1])
                        player.right = True
                        player.left = False
                        if player.y == floor:
                            animation = 'right'
                        if key_state[pygame.K_w] or key_state[pygame.K_UP]:
                            animation = 'jump'
                    elif key_state[pygame.K_a] or key_state[pygame.K_LEFT]:
                        # MOVE LEFT
                        move_background = (+3, move_background[1])
                        player.right = False
                        player.left = True
                        if player.y == floor:
                            animation = 'left'
                        if key_state[pygame.K_w] or key_state[pygame.K_UP]:
                            animation = 'jump'
                    elif key_state[pygame.K_w] or key_state[pygame.K_UP]:
                        if player.y == floor:
                            animation = 'jump'
                    elif key_state[pygame.K_f] :
                        if animation_files['attack'] == 'assets/characters/EVil Wizard 2/Sprites/Attack1.png':
                            animation_files['attack'] = 'assets/characters/EVil Wizard 2/Sprites/Attack2.png'
                        else:
                            animation_files['attack'] = 'assets/characters/EVil Wizard 2/Sprites/Attack1.png'
                        player.animation_files = animation_files
                    else:
                        if player.y < floor:
                            animation = 'fall'
                        else:
                            animation = 'idle'
                        move_background = (0,0)
            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        game_active = True


        if game_active:

            back_gorund.scroll_x += move_background[0]
            back_gorund.scroll_y += move_background[1]
            back_gorund.draw(screen)

            sprite = player.get_animation(animation, 250, 250)

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
                if not direction_player_right:
                    sprite = pygame.transform.flip(sprite, True, False)

            #TODO revisar este floor
            floor = screen_height - 225
            player.y = floor + player_gravity
            screen.blit(sprite, (player.x,player.y,250,250))

            key_state = pygame.key.get_pressed()

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


            pygame.display.update()
            clock.tick(60)