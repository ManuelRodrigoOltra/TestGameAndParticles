# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame
from sys import exit
from drawer.sprites import SpriteSheet
from random import randint





if __name__ == '__main__':
    pygame.init()
    screen_width, screen_height = 1024, 576
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('FistPyGame')
    clock = pygame.time.Clock()
    title_font = pygame.font.Font(None, 50)
    game_active = True
    # idle = True
    player_gravity = 0
    direction_right = False
    animation = 'idle'


    sky_surface = pygame.image.load('assets/characters/Background/sky.png').convert()
    sky_box = sky_surface.get_rect(center = (screen_width/2, screen_height/2))

    player = SpriteSheet('assets/characters/EVil Wizard 2/Sprites/Idle.png')
    player_run = SpriteSheet('assets/characters/EVil Wizard 2/Sprites/Run.png')
    player_fall = SpriteSheet('assets/characters/EVil Wizard 2/Sprites/Fall.png')

    floor = screen_height - 180

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
                        attack = True

                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        pass

                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        # Move right
                        animation = 'move_right'
                        direction_right = True



                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        # Move left
                        animation = 'move_left'
                        direction_right = False

                    # if (event.key == pygame.K_w or event.key == pygame.K_UP) and sprite_rect.y == floor:
                    if (event.key == pygame.K_w or event.key == pygame.K_UP):
                        animation = 'jump'
                        player_gravity -= 120


                    if event.key == pygame.K_f :
                        pass


                if event.type == pygame.KEYUP:
                        if animation == 'move_right' or animation == 'move_left':
                            animation = 'idle'
                        direction = (0, 0)

            else:

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        game_active = True


        if game_active:

            screen.blit(sky_surface,sky_box)


            if animation =='idle':
                sprite = player.get_sprite(250 * player.animation_mov(8, 0)[0], 250 * player.animation_mov(8, 0)[1]
                                           , 250,250)
            elif animation == 'move_right':
                sprite = player_run.get_sprite(250 * player.animation_mov(8, 0)[0],
                                               250 * player.animation_mov(8, 0)[1]
                                               , 250, 250)
            elif animation == 'move_left':
                sprite = player_run.get_sprite(250 * player.animation_mov(8, 0)[0],
                                               250 * player.animation_mov(8, 0)[1]
                                               , 250, 250)
                sprite = pygame.transform.flip(sprite, True, False)

            elif animation == 'jump':
                sprite = player_fall.get_sprite(250 * player.animation_mov(2, 0)[0],
                                                250 * player.animation_mov(2, 0)[1]
                                                , 250, 250)
            else:
                sprite = player.get_sprite(250 * player.animation_mov(8, 0)[0], 250 * player.animation_mov(8, 0)[1]
                                           , 250,250)
                animation = 'idle'













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

            sprite_rect = sprite.get_rect(center=(screen_width/2, 0))
            floor = screen_height - 180
            sprite_rect.y = floor + player_gravity
            screen.blit(sprite, sprite_rect)


            # Gravity
            if sprite_rect.y > floor:
                sprite_rect.y = floor
                if animation == 'jump':
                    animation = 'idle'
            else:
                player_gravity += 3


            pygame.display.update()
            clock.tick(60)