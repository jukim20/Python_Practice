import pygame
import random
class ImgBase:
    def __init__(self,filename, x, y, w, h, speed):
        self.img = pygame.image.load(filename)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = speed
