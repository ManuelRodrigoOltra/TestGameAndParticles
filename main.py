# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame
from sys import exit
from drawer.sprites import AnimatedPlayer
from random import randint





if __name__ == '__main__':
    pygame.init()
    screen_width, screen_height = 1024, 576
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('FistPyGame')
    clock = pygame.time.Clock()
    title_font = pygame.font.Font(None, 50)
    game_active = True
    player_gravity = 0
    direction_player_right = True
    animation = 'idle'

    jump_height = 80


    floor = screen_height - 180


    sky_surface = pygame.image.load('assets/characters/Background/sky.png').convert()
    sky_box = sky_surface.get_rect(center = (screen_width/2, screen_height/2))

    animation_files = {'idle':'assets/characters/EVil Wizard 2/Sprites/Idle.png',
                       'right':'assets/characters/EVil Wizard 2/Sprites/Run.png',
                       'left': 'assets/characters/EVil Wizard 2/Sprites/Run.png',
                       'fall':'assets/characters/EVil Wizard 2/Sprites/Fall.png',
                       'jump':'assets/characters/EVil Wizard 2/Sprites/Jump.png',
                       'down': None, 'attack': None,}

    player = AnimatedPlayer(animation_files)

    sprite = player.get_idle(250 * player.animation_itera(8, 0)[0], 250 * player.animation_itera(8, 0)[1]
                               , 250, 250)
    sprite_rect = sprite.get_rect(midbottom=(screen_width / 2, 0))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if game_active:
                if event.type == pygame.KEYDOWN:
                    key_state = pygame.key.get_pressed()
                    idle = False

                    if event.key == pygame.K_SPACE:
                        # ATTACK
                        animation = 'attack'


                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:

                        pass

                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        # MOVE RIGHT
                        if sprite_rect.y == floor:
                            player.direction_right = True
                            animation = 'right'

                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        # MOVE LEFT
                        if sprite_rect.y == floor:
                            player.direction_right = False
                            animation = 'left'

                    # if (event.key == pygame.K_w or event.key == pygame.K_UP) and sprite_rect.y == floor:
                    if (event.key == pygame.K_w or event.key == pygame.K_UP):
                        if sprite_rect.y == floor:
                            animation = 'jump'

                    if event.key == pygame.K_f :
                        pass

                if event.type == pygame.KEYUP:
                    key_state = pygame.key.get_pressed()

                    if animation == 'move_right' or animation == 'move_left':
                            if sprite_rect.y == floor:
                                animation = 'idle'
                                direction = (0, 0)

            else:

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        game_active = True


        if game_active:

            screen.blit(sky_surface,sky_box)

            if animation =='idle':
                sprite = player.get_idle(250 * player.animation_itera(8, 0)[0], 250 * player.animation_itera(8, 0)[1]
                                            , 250,250)
                if not direction_player_right:
                    sprite = pygame.transform.flip(sprite, True, False)

            elif animation == 'jump':
                player_gravity -= 3
                sprite = player.get_jump(250 * player.animation_itera(2, 0)[0], 250 * player.animation_itera(2, 0)[1]
                                     , 250, 250)
                if not direction_player_right:
                    sprite = pygame.transform.flip(sprite, True, False)

            elif animation == 'fall':
                player_gravity += 2
                sprite = player.get_fall(250 * player.animation_itera(2, 0)[0], 250 * player.animation_itera(2, 0)[1]
                                     , 250, 250)
                if not direction_player_right:
                    sprite = pygame.transform.flip(sprite, True, False)

            elif animation == 'right':
                sprite = player.get_right(250 * player.animation_itera(8, 0)[0], 250 * player.animation_itera(8, 0)[1]
                                     , 250, 250)
            elif animation == 'left':
                sprite = player.get_left(250 * player.animation_itera(8, 0)[0], 250 * player.animation_itera(8, 0)[1]
                                          , 250, 250)



            # elif animation == 'move_right':
            #     sprite = player_run.get_sprite(250 * player.animation_mov(8, 0)[0],
            #                                    250 * player.animation_mov(8, 0)[1]
            #                                    , 250, 250)
            # elif animation == 'move_left':
            #     sprite = player_run.get_sprite(250 * player.animation_mov(8, 0)[0],
            #                                    250 * player.animation_mov(8, 0)[1]
            #                                    , 250, 250)
            #     sprite = pygame.transform.flip(sprite, True, False)
            #
            # elif animation == 'jump':
            #
            #     if jump_up:
            #         jump_acceleration -= 3
            #         player_gravity = 0
            #         sprite = player_jump.get_sprite(250 * player.animation_mov(2, 0)[0],
            #                                         250 * player.animation_mov(2, 0)[1]
            #                                         , 250, 250)
            #         if not direction_player_right:
            #             sprite = pygame.transform.flip(sprite, True, False)
            #
            #     else:
            #         # jump_acceleration = jump_height
            #         player_gravity += 2
            #
            #         sprite = player_fall.get_sprite(250 * player.animation_mov(2, 0)[0],
            #                                     250 * player.animation_mov(2, 0)[1]
            #                                     , 250, 250)
            #
            #
            #         if not direction_player_right:
            #             sprite = pygame.transform.flip(sprite, True, False)

            else:
                sprite = player.get_sprite(250 * player.animation_itera(8, 0)[0], 250 * player.animation_itera(8, 0)[1]
                                           , 250,250)
                animation = 'idle'
                if not direction_player_right:
                    sprite = pygame.transform.flip(sprite, True, False)

            # if idle:
            #     sprite = player.get_sprite(250 * player.animation_mov(8, 0)[0], 250 * player.animation_mov(8, 0)[1]
            #                                , 250,250)
            # else:
            #     if jump:
            #         sprite = player_fall.get_sprite(250 * player.animation_mov(2, 0)[0],
            #                                        250 * player.animation_mov(2, 0)[1]
            #                                        , 250, 250)
            #
            #     elif direction_right:
            #         sprite = player_run.get_sprite(250 * player.animation_mov(8, 0)[0],
            #                                        250 * player.animation_mov(8, 0)[1]
            #                                        , 250, 250)
            #     else:
            #         sprite = player_run.get_sprite(250 * player.animation_mov(8, 0)[0],
            #                                        250 * player.animation_mov(8, 0)[1]
            #                                        , 250, 250)
            #         sprite = pygame.transform.flip(sprite, True, False)

            floor = screen_height - 180
            sprite_rect.y = floor + player_gravity
            screen.blit(sprite, sprite_rect)

            # Gravity
            if sprite_rect.y > floor:
                sprite_rect.y = floor
                jump_acceleration = 0
                player_gravity = 0
                if animation == 'jump' or animation == 'fall':
                    animation = 'idle'

            if sprite_rect.y < floor - jump_height:
                animation = 'fall'



            pygame.display.update()
            clock.tick(60)