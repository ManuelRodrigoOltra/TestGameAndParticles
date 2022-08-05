import pygame
import math as mt



class Background_Generator():

    def calc_rect(self,win,x, y, widht, height):
        #pygame.draw.polygon(win, )
        pass

    def lines (self, win, x, y, width, height, n_lin = 20 ):
        points = []
        for point in n_lin:
            points.append(())

        color_green = pygame.Color(50, 102, 14)
        pygame.draw.lines(win, color_green, False,)


class Background_Rect():
    def __init__(self, loc, color, angle=0, width=30, height=40):
        self.loc = loc
        self.angle = angle
        self.width = width
        self.height = height
        self.color = color

    #sig 1 up 0 down
    def move(self, dv, sig = 1):
        self.loc[0] += dv[0] * sig
        self.loc[1] += dv[1] * sig

    def draw(self, win):
        points = [
            [self.loc[0] + self.width/2, self.loc[1] + self.width/2 * mt.sin(self.angle) + self.height/2],
            [self.loc[0] + self.width/2, self.loc[1] + self.width/2 * mt.sin(self.angle) - self.height/2],
            [self.loc[0] - self.width/2, self.loc[1] - self.width/2 * mt.sin(self.angle)- self.height/2],
            [self.loc[0] - self.width/2, self.loc[1] - self.width/2 * mt.sin(self.angle) + self.height/2]]
        pygame.draw.polygon(win, self.color, points)




class Background_Particle_Square():
    def __init__(self, loc, vel, angle=0, width=20, height=20, width_line=0):
        self.loc = loc
        self.vel = vel
        self.angle = angle
        self.size = [width, height]
        self.width_line = width_line

    #sig 1 up 0 down

    def move(self):
        self.loc[0] += self.vel[0]
        self.loc[1] += self.vel[1]
        self.angle += 0.1


    def draw(self):
        surf = pygame.Surface((2*self.size[0], 2*self.size[1]))
        pygame.draw.rect(surf, [255, 255, 255], (0,0,
                         self.size[0], self.size[1]), width=self.width_line)
        # surf = pygame.transform.rotate(surf, self.angle)
        surf.set_colorkey(0, 0)
        return surf
