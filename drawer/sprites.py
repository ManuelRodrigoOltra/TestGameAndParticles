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
        super(AnimatedPlayer, self).__init__(animation_list[next(iter(animation_list))])
        self.control_animation_x = 0
        self.control_animation_y = 0

        self.jump = False
        self.fall = False

        self.right = True
        self.left = False

        self.speed_animation = (0.6, 0)

        self.animation = None

        self.x = 0
        self.y = 0

        self.move_speed = 1
        self.animation_files = animation_list

        self.width_sprite_animation = 0
        self.height_sprite_animation = 0

    def load_sheets(self, image): #TODO esto está mal, debería renderizar todo al inicio
        sprite_animation = pygame.image.load(image).convert_alpha()
        self.width_sprite_animation = sprite_animation.get_width()
        self.height_sprite_animation = sprite_animation.get_height()
        return sprite_animation

    def get_animation(self,animation, width_sprite, height_sprite):

        sprite = pygame.Surface([width_sprite, height_sprite])
        sprite.set_colorkey((0, 0, 0))
        if not self.animation == animation:
            sprite_animation = self.load_sheets(self.animation_files[animation])

        animation_frame = self.animation_itera (self.width_sprite_animation/width_sprite,
                                                self.height_sprite_animation/height_sprite)
        sprite.blit(sprite_animation,(width_sprite * animation_frame[0], height_sprite * animation_frame[1],
                                              width_sprite, height_sprite))
        if not self.right:
            sprite = pygame.transform.flip(sprite, True, False)
        return sprite

    def draw (self, win, animation, width_sprite, height_sprite):
        sprite = self.get_animation(animation, width_sprite, height_sprite)
        #TODO pensar como pasarle una posición generica y no un centro
        # sprite_box = sprite.get_rect(self.x, self.y, width_sprite, height_sprite)
        win.blit(sprite, (self.x, self.y, width_sprite, height_sprite))

    def animation_itera(self, n_images_sheet_x, n_images_sheet_y):
        self.control_animation_x = self.control_animation_x + self.speed_animation[0]
        self.control_animation_y = self.control_animation_y + self.speed_animation[1]

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
        for it in range(len(self.images_bg)):
            self.scroll_layer[it] = self.scroll_x * self.speed_scroll_layer[it]

            posicion_siguiente = self.images_rect[it].x - self.screen_width * (int(self.scroll_layer[it] // self.screen_width)+1)
            posicion_actual = self.images_rect[it].x - self.screen_width * (int(self.scroll_layer[it] // self.screen_width))

            win.blit(self.images_bg[it], (posicion_actual+self.scroll_layer[it], self.images_rect[it].y + self.scroll_y))
            win.blit(self.images_bg[it], (posicion_siguiente+self.scroll_layer[it], self.images_rect[it].y + self.scroll_y))

class BackGroundFile:
    def __init__(self, file_list, file_level):
        self.bg_file_list = file_list
        self.file_level = file_level
        self.img_render = []
        self.img_render_rect = []

        self.bg_render()

    def bg_render(self):
        n_it = 0
        for it in self.bg_file_list:
            self.img_render.append(pygame.image.load(it))
            self.img_render_rect.append(self.img_render[n_it].get_rect())
            n_it += 1

    def draw(self, win, width, height):
        for it_bg in range(len(self.file_level)):

            if not self.file_level[it_bg]:
                pass
            elif self.file_level[it_bg] == 1:
                self.img_render_rect[0].x = (width * (it_bg % 10))
                self.img_render_rect[0].y = (height * (it_bg - (it_bg % 10)))/10
                print(self.img_render_rect[0].y)
                win.blit(self.img_render[0], (self.img_render_rect[0].x, self.img_render_rect[0].y, width, height))

    def draw_bg_screen (self,win, width, height, pos_x, pos_y):
        pass








