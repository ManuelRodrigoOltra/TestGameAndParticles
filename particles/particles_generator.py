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
    CADENCE = 30
    def __init__(self):
        self.cadence_counter = self.CADENCE
        self.list_shots = []

    def add_shot(self, x0, y0, x1, y1, speed, scroll):
        self.x0 = x0 - scroll[0]
        self.y0 = y0 - scroll[1]
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
        if self.x1 - self.x0 < 0:
            return self.speed * mt.sin(self.get_angle())
        else:
            return -1 * self.speed * mt.sin(self.get_angle())

    def get_angle(self):

            y = self.y1-self.y0
            x = self.x1-self.x0

            if x is not 0:
                return mt.atan(y / x)
            else:
                if y < 0:
                    return -1 * mt.pi/2
                else:
                    return mt.pi / 2

    def itera_draw(self, win, scroll):

        for shot in self.list_shots:
            shot[0][0] += shot[1][0]
            shot[0][1] -= shot[1][1]
            pygame.draw.circle(win, (255, 255, 255), (int(shot[0][0] - scroll[0]), int(shot[0][1] - scroll[1])), 5)


            win.blit(self.circle_surf(20, (20, 20, 20)), (int(shot[0][0] - scroll[0] - 20), int(shot[0][1] - scroll[1] -20)),
                     special_flags=pygame.BLEND_RGB_ADD )

    def circle_surf(self, radius, color):
        surf = pygame.Surface((radius * 4, radius * 4))
        pygame.draw.circle(surf, color, (radius, radius), radius)
        surf.set_colorkey(0, 0)
        return surf

    def remove(self, index):
        del self.list_shots[index]




#Class from Dafluffypotato
class Spark():
    def __init__(self, loc, angle, speed, color, scale=1):
        self.loc = loc
        self.angle = angle
        self.speed = speed
        self.color = color
        self.scale = scale
        self.alive = True

    def point_towards(self, angle, rate):
        rotate_direction =((angle - self.angle + mt.pi * 3) % (mt.pi * 2)) - mt.pi
        try:
            rotate_sign = abs(rotate_direction)/rotate_direction
        except ZeroDivisionError:
            rotate_sign = 1
        if abs(rotate_direction) < rate:
            self.angle = angle
        else:
            self.angle += rate * rotate_sign

    def velocity_adjust(self, friction, force, terminal_velocity, dt):
        movement = self.calcualte_movement(dt)
        movement[1] = min(terminal_velocity, movement[1] + force * dt)
        movement[0] *- friction
        self.angle = mt.atan2(movement[1], movement[0])

    def calcualte_movement(self,dt):
        return [mt.cos(self.angle) * self.speed * dt, mt.sin(self.angle) * self.speed * dt]

    def move(self, dt):
        movement = self.calcualte_movement(dt)
        self.loc[0] += movement[0]
        self.loc[1] += movement[1]

        # self.angle += 0.1
        self.velocity_adjust(0.975, 0.2, 8, dt)
        self.speed -= 0.1

        if self.speed <=0:
            self.alive = False

    def draw(self, surf, offset=[0,0]):
        if self.alive:
            points = [
                [self.loc[0] + mt.cos(self.angle) * self.speed * self.scale, self.loc[1] + mt.sin(self.angle) * self.speed * self.scale],
                [self.loc[0] + mt.cos(self.angle + mt.pi/2) * self.speed * self.scale * 0.3, self.loc[1] + mt.sin(self.angle + mt.pi/2) * self.speed * self.scale * 0.3],
                [self.loc[0] - mt.cos(self.angle) * self.speed * self.scale * 3.5, self.loc[1] - mt.sin(self.angle) * self.speed * self.scale * 3.5],
                [self.loc[0] + mt.cos(self.angle - mt.pi/2) * self.speed * self.scale * 0.3, self.loc[1] + mt.sin(self.angle - mt.pi/2) * self.speed * self.scale * 0.3]
            ]
            pygame.draw.polygon(surf, self.color, points)


