import random

import pygame

from typuspocus import interpol

boundsRect = pygame.Rect(0, 200, 700, 400)


class Varitaje:
    def __init__(self):
        self.location = {
            False: ((0, 300), (300, 600)),
            True: ((300, 300), (700, 600))
        }
        self.last = True
        self.step = 0
        self.max = 9
        self.prev = None
        self.inter = None
        self.points = []
        self.generatePoint()
        self.pos = 400, 400

    def generatePoint(self):
        where = self.location[self.last]
        self.last = not self.last
        inicio, fin = where
        rand = random.randint(inicio[0], fin[0]), random.randint(inicio[1], fin[1])
        self.points.append(rand)

    def nextpos(self):
        if len(self.points) <= 0:
            self.generatePoint()
        if self.step % self.max == 0:
            self.step = 0
            self.inter = interpol.MadamBezier(self.pos, self.points.pop(0), self.inter)
        self.step += 1
        self.pos = self.inter.getAt((1 / self.max) * (self.step - 1))
        return self.pos
