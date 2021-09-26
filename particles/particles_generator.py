from random import randint
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

