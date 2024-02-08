import pygame
from const import screen, GREEN, BLUE, shield_image


class HealthBar:
    def __init__(self):
        self.p1_hp = 100
        self.p2_hp = 100
        self.grhp1 = 258
        self.grhp2 = 258

        self.s1_hp = 15
        self.blhp1 = 60
        self.s2_hp = 15
        self.blhp2 = 60

        self.shield_1 = False
        self.shield_2 = False

    def draw_healthbar(self, type, x, y, player, person=None):
        if player == 1:
            if not self.shield_2:
                self.p2_hp -= type
                self.grhp2 -= type * 2.58
            pygame.draw.rect(screen, GREEN, (x, y, self.grhp2, 11))
            if self.p2_hp <= 0:
                person.living = False
        elif player == 2:
            if not self.shield_1:
                self.p1_hp -= type
                self.grhp1 -= type * 2.58
            pygame.draw.rect(screen, GREEN, (x, y, self.grhp1, 11))
            if self.p1_hp <= 0:
                person.living = False

    def draw_shieldbar(self, type, x, y, player, person=None):
        if player == 1:
            self.s1_hp -= type
            self.blhp1 -= type * 4
            pygame.draw.rect(screen, BLUE, (x, y, self.blhp1 * 4.17, 13))
            if self.s1_hp <= 0:
                self.shield_1 = False

        elif player == 2:
            self.s2_hp -= type
            self.blhp2 -= type * 4
            pygame.draw.rect(screen, BLUE, (x, y, self.blhp2 * 4.17, 13))
            if self.s2_hp <= 0:
                self.shield_2 = False


    def update(self):
        self.p1_hp = 100
        self.p2_hp = 100
        self.grhp1 = 258
        self.grhp2 = 258

    def draw_shield(self, person):
        if not (person is None):
            screen.blit(shield_image, (person.rect.x - 60, person.rect.y))
