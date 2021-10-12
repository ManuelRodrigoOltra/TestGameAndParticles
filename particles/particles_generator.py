from random import randint
import math as mt
import pygame

class particles_basic:
    def __init__(self, win):
        self.pos = [250, 250]
        self.mov = [randint(0,20)/10-1, -2]
        self.size = randint(8,10)
        self.list_particles = []



    def itera_draw(self, win, scroll):
        for particle in self.list_particles:
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            particle[2] -= 0.1
            pygame.draw.circle(win, (255, 255, 255), (int(particle[0][0]) - scroll[0], int(particle[0][1]- scroll[1])), int(particle[2]))
            if particle[2] < 0.2:
                self.list_particles.remove(particle)



    def add_particle(self, pos, mov, size):
        self.list_particles.append([pos, mov, size])


    def clear_particles(self):
        self.list_particles.clear()


class particles_phisics(particles_basic):
    pass




class particles_shot(particles_basic):

    def __init__(self):
        self.list_shots = []

    def add_shot(self, x0, y0, x1, y1, speed):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.speed = speed
        self.list_shots.append([[x0, y0], [self.get_mov_x(), self.get_mov_y()]])

    def get_mov_x(self):
        if self.x1-self.x0 < 0:
            return -1 * self.speed*mt.cos(self.get_angle())
        else:
            return self.speed*mt.cos(self.get_angle())

    def get_mov_y(self):
        if self.y1 - self.y0 < 0:
            return -1 * self.speed * mt.sin(self.get_angle())
        else:
            return self.speed * mt.sin(self.get_angle())

    def get_trend(self):
        try:
            return mt.tan(abs(self.y1-self.y0)/abs(self.x1-self.x0))
        except:
            return 0

    def get_angle(self):
        return mt.atan(self.get_trend())

    def itera_draw(self, win):

        for shot in self.list_shots:
            shot[0][0] += shot[1][0]
            shot[0][1] += shot[1][1]
            pygame.draw.circle(win, (255, 255, 255), (int(shot[0][0]), int(shot[0][1])), 5)



    # def remove(self):
