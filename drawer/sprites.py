import pygame

class SpriteSheet():

    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert_alpha()
        self.control_animation_x = 0
        self.control_animation_y = 0

    def get_sprite (self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.set_colorkey((0,0,0))
        sprite.blit(self.sheet, (0,0), (x, y, width, height))
        return sprite

    def animation_mov(self, n_images_sheet_x, n_images_sheet_y):
        self.control_animation_x = self.control_animation_x + 0.1

        if self.control_animation_x > n_images_sheet_x:
            self.control_animation_x = 0

        if self.control_animation_y > n_images_sheet_y:
            self.control_animation_y = 0

        return self.control_animation_x // 1, self.control_animation_y // 1