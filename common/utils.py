import pygame

pygame.init()
font = pygame.font.Font(None, 30)


def debug(info, x=10, y=10):
    display_surface = pygame.display.get_surface()
    debug_surf = font.render(str(info), True, 'Black')
    debug_rect = debug_surf.get_rect(topleft=(x,y))
    display_surface.blit(debug_surf,debug_rect)



class FPSCounter:
    def __init__(self, win, font, clock, color, pos):
        self.win = win
        self.font = font
        self.clock = clock
        self.pos = pos
        self.color = color

        self.fps_text = self.font.render(str(int(self.clock.get_fps())) + "FPS", False, self.color)
        self.fps_text_rect = self.fps_text.get_rect(center=(self.pos[0], self.pos[1]))

    def render(self):
        self.win.blit(self.fps_text, self.fps_text_rect)

    def update(self):
        self.fps_text = self.font.render(str(int(self.clock.get_fps())) + "FPS", False, self.color)
        self.fps_text_rect = self.fps_text.get_rect(center=(self.pos[0], self.pos[1]))



def mouse_pointer(radius = 1):

    surface = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA, 32).convert_alpha()
    pygame.draw.circle(surface, [168, 50, 50], (radius, radius), radius, width=3)
    pygame.draw.circle(surface, [168, 50, 50], (radius, radius), 3, width=0)
    return surface

