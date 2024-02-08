import pygame
from load_other import load_sound, load_image


class LoadImage:
    def __init__(self, x, y, width, height, img, image_after_click=None, sound=None):
        self.x, self.y = x, y
        self.pressure = False
        self.choice = False
        self.selected_color = (0, 0, 0, 0)
        self.change = 1
        self.width, self.height = width, height
        self.sound = sound
        self.image_past = image_after_click
        if self.sound:
            self.sound = load_sound(sound)
        self.image = pygame.transform.scale(load_image(img, -1), (width, height))
        if self.image_past:
            self.image_past = pygame.transform.scale(load_image(image_after_click, -1), (width, height))
        self.button = self.image.get_rect(topleft=(x, y))

    def pressure_test(self, m_pos):
        self.pressure = self.button.collidepoint(m_pos)

    def update(self, screen):
        if self.pressure and self.image_past:
            page = self.image_past
        else:
            page = self.image
        screen.blit(page, self.button.topleft)

    def mouse_event(self, event):
        if self.pressure and event.type == pygame.MOUSEBUTTONDOWN and event.type == 1:
            if self.sound:
                self.sound.play()
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))


