import pygame
import sys
import random
from const import cloud_imgs, SCREEN_WIDTH, SCREEN_HEIGHT, screen


class Cloud:
    def __init__(self):
        self.image = random.choice(cloud_imgs)
        self.x = random.randint(-100, SCREEN_WIDTH)
        self.y = random.randint(250, SCREEN_HEIGHT)
        self.speed = random.randint(1, 2)

    def move(self):
        self.x += self.speed
        if self.x > SCREEN_WIDTH:
            self.x = -self.image.get_width()
            self.y = random.randint(0, SCREEN_HEIGHT)

    def draw(self):
        screen.blit(self.image, (self.x, self.y))