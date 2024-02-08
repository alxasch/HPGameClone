import pygame


class Character:
    def __init__(self, player, turn, x, y, info, sprite, const):
        self.amount = info[0] # получаем размер квадрата для одной анимационной картинки
        self.scale = info[1]
        self.player = player
        self.turn = turn
        self.rect = pygame.Rect((x, y, 80, 180))
        self.sprite_list = self.sprite_download(sprite, const)
        self.vertical = 0
        self.action = 2 #0-death #1-run #2-stay #3-attack #4-jump
        self.sprite_index = 0
        self.image = self.sprite_list[self.action][self.sprite_index]
        self.change_clock = pygame.time.get_ticks()
        self.living = True
        self.jump = False
        self.run = False
        self.attack = False
        self.cooldown = 0

    def draw(self, surface):
        picture = pygame.transform.flip(self.image, self.turn, False)
        surface.blit(picture, (self.rect.x - 60, self.rect.y))

    def sprite_download(self, sprite, const):
        sprite_list= []
        for y, elem in enumerate(const):
            img_list = []
            for i in range(elem):
                img = sprite.subsurface(i * self.amount, y * self.amount, self.amount, self.amount)
                img_list.append(pygame.transform.scale(img, (self.amount * self.scale, self.amount * self.scale)))
            sprite_list.append(img_list)
        return  sprite_list

    def move(self, sw, sh):
        SPEED = 5
        GRAVITATION = 1
        self.run = False
        self.attack = False

        sx = 0
        sy = 0

        key = pygame.key.get_pressed()
        if self.player == 1:
            if key[pygame.K_a]:
                sx = -SPEED
                self.turn = True
                self.run = True
            if key[pygame.K_d]:
                sx = SPEED
                self.turn = False
                self.run = True
            if key[pygame.K_w] and not self.jump:
                self.vertical = -17
                self.jump = True
            if key[pygame.K_1]:
                self.attack = True

        if self.player == 2:
            if key[pygame.K_LEFT]:
                sx = -SPEED
                self.turn = True
                self.run = True
            if key[pygame.K_RIGHT]:
                sx = SPEED
                self.turn = False
                self.run = True
            if key[pygame.K_UP] and not self.jump:
                self.vertical = -17
                self.jump = True
            if key[pygame.K_KP1]:
                self.attack = True

        self.vertical += GRAVITATION
        sy += self.vertical

        if self.cooldown > 0:
            self.cooldown -= 1

        if self.rect.left + sx < 0:
            sx = -self.rect.left
        if self.rect.right + sx > sw:
            sx = sw - self.rect.right
        if self.rect.bottom + sy > sh - 60:
            self.vertical = 0
            self.jump = False
            sy = sh - 60 - self.rect.bottom

        self.rect.x += sx
        self.rect.y += sy

    def update(self):
        decay_period = 250
        if not self.living:
            self.update_action(0)
        elif self.attack == True and self.cooldown == 0:
            self.update_action(3)
        elif self.jump == True:
            self.update_action(4)
        elif self.run == True:
            self.update_action(1)
            decay_period = 100
        else:
            self.update_action(2)
        try:
            self.image = self.sprite_list[self.action][self.sprite_index] # обновление изображения
            # проверяем время с момента последней смены картинки спрайта
            if pygame.time.get_ticks() - self.change_clock > decay_period:
                self.sprite_index += 1
                self.change_clock = pygame.time.get_ticks()
            if self.sprite_index >= len(self.sprite_list[self.action]):
                if self.living == False:
                    self.sprite_index = len(self.sprite_list[self.action]) - 1
                else:
                    self.sprite_index = 0
                    if self.action == 3:
                        self.cooldown = 100
        except IndexError:
            self.sprite_index = 0

    def update_action(self, new):
        if new != self.action:
            self.action = new
            self.sprite_index = 0
            self.change_clock = pygame.time.get_ticks()