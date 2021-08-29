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

        self.jump = False
        self.fall = False

        self.right = True
        self.left = False

        self.speed_animation = 0.3

        self.animation = None

        self.x = 0
        self.y = 0

        self.animation_files = animation_list

        self.width_sprite_animation = 0
        self.height_sprite_animation = 0

    def load_sheets(self, image):
        sprite_animation = pygame.image.load(image).convert_alpha()
        self.width_sprite_animation = sprite_animation.get_width()
        self.height_sprite_animation = sprite_animation.get_height()
        return sprite_animation

    def get_animation(self,animation, width, height):

        sprite = pygame.Surface([width, height])
        sprite.set_colorkey((0, 0, 0))
        if not self.animation == animation:
            sprite_animation = self.load_sheets(self.animation_files[animation])


        animation_frame = self.animation_itera (self.width_sprite_animation/width, self.height_sprite_animation/height)
        # sprite.blit(sprite_animation, (self.x, self.y), (width * animation_frame[0], height * animation_frame[1], width, height))
        sprite.blit(sprite_animation, (0, 0),
                    (width * animation_frame[0], height * animation_frame[1], width, height))
        if not self.right:
            sprite = pygame.transform.flip(sprite, True, False)
        return sprite

    def animation_itera(self, n_images_sheet_x, n_images_sheet_y):
        self.control_animation_x = self.control_animation_x + 0.1
        self.control_animation_y = self.control_animation_y + 0.1

        if self.control_animation_x > n_images_sheet_x:
            self.control_animation_x = 0

        if self.control_animation_y > n_images_sheet_y:
            self.control_animation_y = 0

        return self.control_animation_x // 1, self.control_animation_y // 1


class BackGround:
    def __init__(self, image):
        self.image = image
        self.images_bg = []
        self.images_rect = []


class BackGroundScroll (BackGround):

    def __init__(self, image_list, screen_width, screen_height, speed_scroll_layer):
        self.images_bg = []
        self.images_rect = []
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.scroll_x = 0
        self.scroll_layer = [0]*len(image_list)
        self.scroll_y = 0
        self.speed_scroll_layer = speed_scroll_layer

        #TODO esta var es una chapucilla, arreglaralo cuando se pueda
        self.first_draw = True

        for it in range(len(image_list)):
            self.images_bg.append(pygame.image.load(image_list[it]).convert_alpha())
            self.images_rect.append(self.images_bg[it].get_rect(center=(screen_width / 2, screen_height / 2)))


    def draw(self, win):
        #TODO la primera layer es el fond, no necesitamos hacer scroll
        if self.first_draw:
            win.blit(self.images_bg[0], self.images_rect[0])
            self.images_bg.remove(self.images_bg[0])
            self.first_draw = False


        for it in range(len(self.images_bg)):
            self.scroll_layer[it] = self.scroll_x * self.speed_scroll_layer[it]

            posicion_siguiente = self.images_rect[it].x - self.screen_width * (int(self.scroll_layer[it] // self.screen_width)+1)
            posicion_actual = self.images_rect[it].x - self.screen_width * (int(self.scroll_layer[it] // self.screen_width))

            win.blit(self.images_bg[it], (posicion_actual+self.scroll_layer[it], self.images_rect[it].y + self.scroll_y))
            win.blit(self.images_bg[it], (posicion_siguiente+self.scroll_layer[it], self.images_rect[it].y + self.scroll_y))






