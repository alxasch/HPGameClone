import pygame


class StarAnima:
    def __init__(self, x, y, sprite, screen):
        self.screen = screen
        self.x = x
        self.y = y
        self.shot_list = sprite
        self.sprite_index = 0
        self.change_clock = pygame.time.get_ticks()
        self.image1 = self.shot_list[self.sprite_index]

    def draw(self):
        picture = pygame.transform.flip(self.image1, True, False)
        self.screen.blit(picture, (self.x, self.y))

    def move(self):
        pass

    def update(self):
        decay_period = 80
        try:
            self.image1 = self.shot_list[self.sprite_index]
            if pygame.time.get_ticks() - self.change_clock > decay_period:
                self.sprite_index += 1
                self.change_clock = pygame.time.get_ticks()
            if self.sprite_index >= len(self.shot_list):
                self.sprite_index = 0
        except IndexError:
            self.sprite_index = 0