import pygame


class BasicPlayer():
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert_alpha()
        self.focus = False

    def get_sprite (self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.set_colorkey((0,0,0))
        sprite.blit(self.sheet, (0,0), (x, y, width, height))
        return sprite


class AnimatedPlayer(BasicPlayer):

    def __init__(self, animation_list):
        super(AnimatedPlayer, self).__init__(animation_list['idle'])
        self.control_animation_x = 0
        self.control_animation_y = 0

        self.jump_up = False
        self.fall = False

        self.direction_right = True

        self.animation_files = animation_list
        self.animation = 'idle'

        self.n_animated_frames_idle = 8
        self.n_animated_frames_jump = 2
        self.n_animated_frames_fall = 2
        self.n_animated_frames_right = 8
        self.n_animated_frames_left = 8
        self.n_animated_frames_down = 8

        self.load_animation_sheets()

    def load_animation_sheets(self):
        if self.animation_files['idle'] is not None:
            self.sheet_idle = pygame.image.load(self.animation_files['idle']).convert_alpha()
        if self.animation_files['jump'] is not None:
            self.sheet_jump = pygame.image.load(self.animation_files['jump']).convert_alpha()
        if self.animation_files['fall'] is not None:
            self.sheet_fall = pygame.image.load(self.animation_files['fall']).convert_alpha()
        if self.animation_files['right'] is not None:
            self.sheet_right = pygame.image.load(self.animation_files['right']).convert_alpha()
        if self.animation_files['left'] is not None:
            self.sheet_left = pygame.image.load(self.animation_files['left']).convert_alpha()
        if self.animation_files['down'] is not None:
            self.sheet_down = pygame.image.load(self.animation_files['down']).convert_alpha()

    def get_idle(self,x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.set_colorkey((0, 0, 0))
        sprite.blit(self.sheet_idle, (0, 0), (x, y, width, height))
        return sprite

    def get_jump(self,x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.set_colorkey((0, 0, 0))
        sprite.blit(self.sheet_jump, (0, 0), (x, y, width, height))
        if not self.direction_right:
            sprite = pygame.transform.flip(sprite, True, False)
        return sprite

    def get_fall(self,x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.set_colorkey((0, 0, 0))
        sprite.blit(self.sheet_fall, (0, 0), (x, y, width, height))
        if not self.direction_right:
            sprite = pygame.transform.flip(sprite, True, False)
        return sprite

    def get_right(self,x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.set_colorkey((0, 0, 0))
        sprite.blit(self.sheet_right, (0, 0), (x, y, width, height))
        return sprite

    def get_left(self,x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.set_colorkey((0, 0, 0))
        sprite.blit(self.sheet_left, (0, 0), (x, y, width, height))
        sprite = pygame.transform.flip(sprite, True, False)
        return sprite

    def get_down(self,x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.set_colorkey((0, 0, 0))
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        return sprite

    def get_attack(self,x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.set_colorkey((0, 0, 0))
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        return sprite

    def animation_itera(self, n_images_sheet_x, n_images_sheet_y):
        self.control_animation_x = self.control_animation_x + 0.1

        if self.control_animation_x > n_images_sheet_x:
            self.control_animation_x = 0

        if self.control_animation_y > n_images_sheet_y:
            self.control_animation_y = 0

        return self.control_animation_x // 1, self.control_animation_y // 1

