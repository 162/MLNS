import pygame
from math import log, atan


class FeatureMap():
    def __init__(self):
        self.map = []

    def load(self, path, width, height, mode):
        r = 1
        array = [[0 for j in range(height)] for i in range(width)]
        img = pygame.image.load(path)
        for x in range(width):
            for y in range(height):
                clr = img.get_at((x, y))
                if mode == "a":
                    array[x][y] = (clr[0]+clr[1]+clr[2])/3
                if mode == "r":
                    array[x][y] = clr[0]
                if mode == "g":
                    array[x][y] = clr[1]
                if mode == "b":
                    array[x][y] = clr[2]
                if mode == "c":
                    s = 0
                    n = 0
                    for i in range(max(0, x-r), min(width, x+r+1)):
                        for j in range(max(0, y-r), min(height, y+r+1)):
                            n += 1
                            clr2 = img.get_at((i, j))
                            s += sum((float(clr[i])-clr2[i])**2 for i in range(3))**0.5
                    array[x][y] = s/n
                    #print array[x][y]
        self.map = array

    def normalize(self, compress=False):
        max_point = 0
        min_point = 1000000
        if compress:
            self.map = [[log((max(0, i-0.2))**0.1+0.1) for i in j] for j in self.map]
        for x in range(len(self.map)):
            for y in range(len(self.map[0])):
                if max_point < self.map[x][y]:
                    max_point = self.map[x][y]
                if min_point > self.map[x][y]:
                    min_point = self.map[x][y]
        k = 255/float(max_point-min_point)
        self.map = [[i-min_point for i in j] for j in self.map]
        self.map = [[int(i*k) for i in j] for j in self.map]

    def __add__(self, other):
        result = FeatureMap()
        result.map = [[self.map[i][j] + other.map[i][j] for j in range(len(self.map[i]))]
                      for i in range(len(self.map))]
        return result

    def __div__(self, other):
        self.map = [[self.map[i][j]/other for j in range(len(self.map[i]))]
                    for i in range(len(self.map))]

    def draw(self, x0, y0, scale, save_as=None):
        DISPLAY = (len(self.map)*scale, len(self.map[0])*scale)
        pygame.init()
        flags = pygame.DOUBLEBUF | pygame.HWSURFACE
        # screen = pygame.display.set_mode(DISPLAY)
        screen = pygame.display.set_mode(DISPLAY, flags)
        pygame.display.set_caption("Naive Attention Model")
        background = pygame.Surface(DISPLAY)
        background.fill(pygame.Color("#000000"))
        for x in range(len(self.map)):
            for y in range(len(self.map[0])):
                rect = pygame.Rect(x*scale+x0, y*scale+y0, scale, scale)
                clr = max(int(self.map[x][y]), 0)
                pygame.draw.rect(screen, pygame.Color(clr, clr, clr, 255), rect)
            pygame.display.update()
        if save_as:
            pygame.image.save(screen, save_as)
        raise SystemExit

    def draw2(self, x0, y0, scale, save_as=None):
        DISPLAY = (len(self.map)*scale, len(self.map[0])*scale)
        pygame.init()
        flags = pygame.DOUBLEBUF | pygame.HWSURFACE
        # screen = pygame.display.set_mode(DISPLAY)
        screen = pygame.display.set_mode(DISPLAY, flags)
        pygame.display.set_caption("Naive Attention Model")
        background = pygame.Surface(DISPLAY)
        background.fill(pygame.Color("#000000"))
        for x in range(len(self.map)):
            for y in range(len(self.map[0])):
                rect = pygame.Rect(x*scale+x0, y*scale+y0, scale, scale)
                clr = max(int(self.map[x][y]), 0)
                if clr < 128:
                    pygame.draw.rect(screen, pygame.Color(2*clr, 2*clr, 127-clr, 255), rect)
                else:
                    pygame.draw.rect(screen, pygame.Color(255, 511-2*clr, 0, 255), rect)
            pygame.display.update()
        if save_as:
            pygame.image.save(screen, save_as)
        raise SystemExit


def draw_multiple(features, x0, y0, scale, save_as=None, bw=True):
    number = len(features)
    summed = features[0]+features[1]
    for i in range(2, len(features)):
        summed = summed + features[i]
    summed/number
    if bw:
        summed.draw(x0, y0, scale, save_as)
    else:
        summed.draw2(x0, y0, scale, save_as)