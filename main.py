# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame
from sys import exit
from drawer.sprites import SpriteSheet
from random import randint




class EvilWizard (pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.wizard_image_idle = pygame.image.load('assets/characters/EVil Wizard 2/Sprites/Idle.png').convert_alpha()
        self.image = pygame.Surface([250,250])
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect = self.wizard_image_idle.get_rect(center = (1024/2, 576/2))

    # def _idle (self, screen):
    #     self.wizard_show = pygame.surface(250,250)
    #     self.wizard_surface_idle = self.wizard_image_idle.scroll(250,0)
    #     screen.blit(self.wizard_surface_idle, self.wizard_show)






if __name__ == '__main__':
    pygame.init()
    screen_width, screen_height = 1024, 576
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('FistPyGame')
    clock = pygame.time.Clock()
    title_font = pygame.font.Font(None, 50)
    game_active = True
    idle = True
    player_gravity = 0

    sky_surface = pygame.image.load('assets/characters/Background/sky.png').convert()
    sky_box = sky_surface.get_rect(center = (screen_width/2, screen_height/2))

    # player = EvilWizard(0, 0)
    player = SpriteSheet('assets/characters/EVil Wizard 2/Sprites/Idle.png')
    player_run = SpriteSheet('assets/characters/EVil Wizard 2/Sprites/Run.png')

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
                        direction_right = True



                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        # Move left
                        direction_right = False

                    # if (event.key == pygame.K_w or event.key == pygame.K_UP) and player.player_box.y == 470:
                    if (event.key == pygame.K_w or event.key == pygame.K_UP):
                        animation = True
                        player_gravity -= 20


                    if event.key == pygame.K_f :
                        pass


                if event.type == pygame.KEYUP:
                        idle = True
                        direction = (0, 0)

            else:

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        game_active = True


        if game_active:

            screen.blit(sky_surface,sky_box)

            if idle:
                sprite = player.get_sprite(250 * player.animation_mov(8, 0)[0], 250 * player.animation_mov(8, 0)[1]
                                           , 250,250)
            else:
                    if direction_right:
                        sprite = player_run.get_sprite(250 * player.animation_mov(8, 0)[0],
                                                       250 * player.animation_mov(8, 0)[1]
                                                       , 250, 250)
                    else:
                        sprite = player_run.get_sprite(250 * player.animation_mov(8, 0)[0],
                                                       250 * player.animation_mov(8, 0)[1]
                                                       , 250, 250)
                        sprite = pygame.transform.flip(sprite, True, False)


            screen.blit(sprite, sprite.get_rect(center = (screen_width/2, screen_height/2)))


            pygame.display.update()
            clock.tick(60)