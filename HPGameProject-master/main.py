import pygame
from character import Character
from load_other import load_image
from generate_cloud import Cloud
from health import HealthBar
from const import *
from database import add_to_database_1
import pygame.mixer

pygame.init()

clock = pygame.time.Clock()
game_over = False
last_move = 'right'
last_move_s = 'left'

time_update = pygame.time.get_ticks()
font = pygame.font.Font(None, 100)
text_font = pygame.font.Font(None, 50)
points = [0, 0] # очки игроков

healthing = HealthBar()

pygame.display.set_caption('hb')



def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def draw_count(text, font, size_text, x, y):
    image = font.render(text, True, size_text)
    screen.blit(image, (x, y))


def player_one(layer):
    for name in [['germiona', germiona_sprite, GERMIONA_SHEET], ['garri', garri_sprite, ANIMATION_SHEET_GARRI],
                 ['ron', ron_sprite, RON_SHEET], ['drako', drako_sprite, DRAKO_SHEET]]:
        if name[0] == layer:
            return Character(1, False, 200, 360, SPRITE_INFO, name[1], name[2])

def player_two(layer):
    for name in [['germiona', germiona_sprite, GERMIONA_SHEET], ['garri', garri_sprite, ANIMATION_SHEET_GARRI],
                 ['ron', ron_sprite, RON_SHEET], ['drako', drako_sprite, DRAKO_SHEET]]:
        if name[0] == layer:
            return Character(2, True, 700, 360, SPRITE_INFO, name[1], name[2])


class Shots:
    def __init__(self, player, x, y, facing, speed, type=5, info=SHOT_INFO):
        self.amount = info[0][0]
        self.amount1 = info[0][1]
        self.scale = info[1]
        self.sprite_index = 0
        self.shot_list = self.download_shots(shot_sprite, SHEET_SHOT)
        self.zero_x = x
        self.x, self.y = x + 10, y + 30
        self.player = player
        self.facing = facing
        if self.facing > 0:
            self.turn = True
        else:
            self.turn = False
        self.speed = speed
        self.type = type
        self.image1 = self.shot_list[self.sprite_index]
        self.change_clock = pygame.time.get_ticks()
        self.last_time = pygame.time.get_ticks()
        self.last_ind = 0
        self.last_img = last_img[self.last_ind]
        self.image = shot_image.get_rect(topleft=(self.x, self.y))

    def draw(self):
        picture = pygame.transform.flip(self.image1, self.turn, False)
        screen.blit(picture, (self.x, self.y))

    def draw_last_img(self):
        picture = pygame.transform.flip(self.last_img, self.turn, False)
        screen.blit(picture, (self.x, self.y))
    def download_shots(self, sprite, const):
        sprite_list= []
        for i in range(const[0]):
            img = sprite.subsurface(i * self.amount, 0, self.amount, self.amount1)
            sprite_list.append(pygame.transform.scale(img, (self.amount * self.scale, self.amount1 * self.scale)))
        return sprite_list

    def move(self, character_1, character_2, move):
        self.x += self.speed
        self.image = shot_image.get_rect(topleft=(self.x, self.y))
        self.update()
        if self.player == 1:
            if self.image.colliderect(character_2.rect.x, character_2.rect.y, 80, 180): # осуществляет проверку на столкновение
                if self.type == 0:
                    pygame.mixer.music.load('data/sound/depulso_contact.mp3')
                    pygame.mixer.music.play(1)
                    if move == 'right':
                        character_2.rect.x += 200
                    if move == 'left':
                        character_2.rect.x -= 200
                if self.type == 20:
                    pygame.mixer.music.load('data/sound/bomb_contact_sound.mp3')
                    pygame.mixer.music.play(1)
                if self.type == 5:
                    pygame.mixer.music.load('data/sound/exp_contact_sound.mp3')
                    pygame.mixer.music.play(1)

                if not healthing.shield_2:
                    healthing.draw_healthbar(self.type, 159, 46, 1, character_2)
                else:
                    if healthing.s2_hp > 0:
                        healthing.draw_shieldbar(self.type, 159, 46, 2, character_2)
                    else:
                        healthing.shield_2 = False
                return False

        if self.player == 2:
            if self.image.colliderect(character_1.rect.x, character_1.rect.y, 80, 180):
                if self.type == 0:
                    pygame.mixer.music.load('data/sound/depulso_contact.mp3')
                    pygame.mixer.music.play(1)
                    if move == 'right':
                        character_1.rect.x += 200
                    if move == 'left':
                        character_1.rect.x -= 200
                if self.type == 20:
                    pygame.mixer.music.load('data/sound/bomb_contact_sound.mp3')
                    pygame.mixer.music.play(1)
                if self.type == 5:
                    pygame.mixer.music.load('data/sound/exp_contact_sound.mp3')
                    pygame.mixer.music.play(1)
                if not healthing.shield_1:
                    healthing.draw_healthbar(self.type, 582, 46, 2, character_1)
                else:
                    if healthing.s1_hp > 0:
                        healthing.draw_shieldbar(self.type, 582, 46, 1, character_1)
                    else:
                        healthing.shield_1 = False
                return False
        if SCREEN_WIDTH - 40 >= self.x > 0:
            # screen.blit(shot_image, (self.x, self.y))
            self.draw()
            return True
        else:
            return False

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

    def last_image(self):
        decay_period = 80
        for i in range(5):
            if self.last_ind <= len(last_img):
                if pygame.time.get_ticks() - self.last_time > decay_period:
                    self.last_ind += 1
                    self.last_time = pygame.time.get_ticks()
                    self.draw_last_img()
        self.last_ind = 0


def play_g(p1, p2):
    character_1 = player_one(p1)
    character_2 = player_two(p2)

    run = True
    count = 3
    clock = pygame.time.Clock()
    game_over = False
    last_move = 'right'
    last_move_s = 'left'

    time_update = pygame.time.get_ticks()
    cooldawn_time_1 = pygame.time.get_ticks()
    cooldawn_second1 = pygame.time.get_ticks()
    cooldawn_time_2 = pygame.time.get_ticks()
    cooldawn_second2 = pygame.time.get_ticks()
    font = pygame.font.Font(None, 100)
    text_font = pygame.font.Font(None, 50)
    points = [0, 0]


    pygame.display.set_caption('Hogwarts Duel')

    all_shots = []
    all_shots_s = []

    index_background = 0
    chek_score_event = pygame.USEREVENT + 1
    pygame.time.set_timer(chek_score_event, 150)

    clouds = [Cloud() for _ in range(5)]

    while run:
        clock.tick(FPS)
        screen.fill(SKY)

        for cloud in clouds:
            cloud.move()
            cloud.draw()

        if (pygame.time.get_ticks() - cooldawn_time_1) >= 1500:
            screen.blit(exp_image, (175, 90))
        if (pygame.time.get_ticks() - cooldawn_time_2) >= 1500:
            screen.blit(exp_image, (575, 90))

        if (pygame.time.get_ticks() - cooldawn_second1) >= 15000 and p1 == 'garri':
            screen.blit(protego_image, (225, 90))
        if (pygame.time.get_ticks() - cooldawn_second2) >= 15000 and p2 == 'garri':
            screen.blit(protego_image, (625, 90))

        if (pygame.time.get_ticks() - cooldawn_second1) >= 7000 and p1 == 'ron':
            screen.blit(depulso_image, (225, 90))
        if (pygame.time.get_ticks() - cooldawn_second2) >= 7000 and p2 == 'ron':
            screen.blit(depulso_image, (625, 90))

        if (pygame.time.get_ticks() - cooldawn_second1) >= 7000 and p1 == 'germiona':
            screen.blit(bombarda_image, (225, 90))
        if (pygame.time.get_ticks() - cooldawn_second2) >= 7000 and p2 == 'germiona':
            screen.blit(bombarda_image, (625, 90))

        if (pygame.time.get_ticks() - cooldawn_second1) >= 10000 and p1 == 'drako':
            screen.blit(heal_image, (225, 90))
        if (pygame.time.get_ticks() - cooldawn_second2) >= 10000 and p2 == 'drako':
            screen.blit(heal_image, (625, 90))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
            if event.type == chek_score_event:
                index_background = (index_background + 1) % len(bg_img)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    return True
        screen.blit(bg_img[index_background], (0, 0))

        # background(bg_image)

        if count <= 0:
            character_1.move(SCREEN_WIDTH, SCREEN_HEIGHT)
            character_2.move(SCREEN_WIDTH, SCREEN_HEIGHT)
        else:
            draw_count(str(count), font, RED, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)
            if (pygame.time.get_ticks() - time_update) >= 1000:
                count -= 1
                time_update = pygame.time.get_ticks()

        for elem in hp_list:
            if elem[0] == p1:
                screen.blit(elem[1], (44, 29))
            elif elem[0] == p2:
                screen.blit(elem[1], (868, 29))

        character_1.update()
        character_2.update()

        pygame.draw.rect(screen, RED, (159, 46, 258, 11))
        pygame.draw.rect(screen, RED, (582, 46, 258, 11))

        healthing.draw_healthbar(0, 159, 46, 2, character_1)
        healthing.draw_healthbar(0, 582, 46, 1, character_2)

        screen.blit(hp_sprite, (20, 20))
        screen.blit(hp_sprite2, (580, 20))


        draw_text(str(points[0]) + ' : ' + str(points[1]), text_font, RED, SCREEN_WIDTH // 2 - 35, 30)

        character_1.draw(screen)
        character_2.draw(screen)

        if healthing.shield_1 == True:
            healthing.draw_shieldbar(0, 162, 73, 1, character_1)
            healthing.draw_shield(character_1)
            screen.blit(shield_hp, (160, 70))

        if healthing.shield_2 == True:
            healthing.draw_shieldbar(0, 592, 73, 2, character_2)
            healthing.draw_shield(character_2)
            screen.blit(shield_hp, (590, 70))


        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            last_move = 'left'

        if keys[pygame.K_d]:
            last_move = 'right'

        if keys[pygame.K_LEFT]:
            last_move_s = 'left'

        if keys[pygame.K_RIGHT]:
            last_move_s = 'right'

        if keys[pygame.K_RSHIFT]:
            if last_move_s == 'right':
                facing = 1.5
            else:
                facing = -1.5
            if (len(all_shots_s) < 1 and character_2.cooldown == 0 and count <= 0 and game_over == False and
                    abs(character_1.rect.x - character_2.rect.x) > 10 and (pygame.time.get_ticks() - cooldawn_time_2) >= 1500):
                all_shots_s.append(Shots(2, character_2.rect.x + (35 * facing), character_2.rect.y + 30, facing, 5 * facing))
                pygame.mixer.music.load('data/sound/spell_use_sound.mp3')
                pygame.mixer.music.play(1)
                cooldawn_time_2 = pygame.time.get_ticks()

        if keys[pygame.K_1]:
            if last_move == 'right':
                facing = 1.5
            else:
                facing = -1.5
            if (len(all_shots) < 1 and character_1.cooldown == 0 and count <= 0 and game_over == False
                    and abs(character_1.rect.x - character_2.rect.x) > 75 and (pygame.time.get_ticks() - cooldawn_time_1) >= 1500):
                all_shots.append(Shots(1, character_1.rect.x + (35 * facing), character_1.rect.y + 30, facing, 5 * facing))
                pygame.mixer.music.load('data/sound/spell_use_sound.mp3')
                pygame.mixer.music.play(1)
                cooldawn_time_1 = pygame.time.get_ticks()

        if keys[pygame.K_2]:
            if p1 == 'germiona':
                if last_move == 'right':
                    facing = 1.5
                else:
                    facing = -1.5
                if (len(all_shots) < 1 and character_1.cooldown == 0 and count <= 0 and game_over == False
                        and abs(character_1.rect.x - character_2.rect.x) > 100 and (pygame.time.get_ticks() - cooldawn_second1) >= 7000):
                    all_shots.append(Shots(1, character_1.rect.x + (35 * facing), 460, facing, 2 * facing, type=20))
                    pygame.mixer.music.load('data/sound/spell_use_sound.mp3')
                    pygame.mixer.music.play(1)
                    cooldawn_second1 = pygame.time.get_ticks()
            if p1 == 'ron':
                if last_move == 'right':
                    facing = 1.5
                else:
                    facing = -1.5
                if (len(all_shots) < 1 and character_1.cooldown == 0 and count <= 0 and game_over == False
                        and abs(character_1.rect.x - character_2.rect.x) > 100 and (pygame.time.get_ticks() - cooldawn_second1) >= 7000):
                    all_shots.append(Shots(1, character_1.rect.x + (35 * facing), character_1.rect.y + 30, facing, 8 * facing, type=0))
                    pygame.mixer.music.load('data/sound/spell_use_sound.mp3')
                    pygame.mixer.music.play(1)
                    cooldawn_second1 = pygame.time.get_ticks()
            if p1 == 'garri':
                if count <= 0 and (pygame.time.get_ticks() - cooldawn_second1) >= 15000 and game_over == False:
                    healthing.shield_1 = True
                    healthing.s1_hp = 15
                    healthing.blhp1 = 60
                    pygame.mixer.music.load('data/sound/spell_use_sound.mp3')
                    pygame.mixer.music.play(1)
                    cooldawn_second1 = pygame.time.get_ticks()
            if p1 == 'drako':
                if count <= 0 and (pygame.time.get_ticks() - cooldawn_second1) >= 10000 and game_over == False and healthing.p1_hp <= 90:
                    healthing.draw_healthbar(-10, 159, 46, 2, character_1)
                    print(healthing.p1_hp)
                    pygame.mixer.music.load('data/sound/spell_use_sound.mp3')
                    pygame.mixer.music.play(1)
                    cooldawn_second1 = pygame.time.get_ticks()

        if keys[pygame.K_RCTRL]:
            if p2 == 'germiona':
                if last_move_s == 'right':
                    facing = 1.5
                else:
                    facing = -1.5
                if (len(all_shots_s) < 1 and character_2.cooldown == 0 and count <= 0 and game_over == False
                        and abs(character_1.rect.x - character_2.rect.x) > 100 and (pygame.time.get_ticks() - cooldawn_second2) >= 7000):
                    all_shots_s.append(Shots(2, character_2.rect.x + (35 * facing), 460, facing, 2 * facing, type=20))
                    cooldawn_second2 = pygame.time.get_ticks()
            if p2 == 'ron':
                if last_move_s == 'right':
                    facing = 1.5
                else:
                    facing = -1.5
                if (len(all_shots_s) < 1 and character_2.cooldown == 0 and count <= 0 and game_over == False
                        and abs(character_1.rect.x - character_2.rect.x) > 100 and (pygame.time.get_ticks() - cooldawn_second2) >= 7000):
                    all_shots_s.append(Shots(2, character_2.rect.x + (35 * facing), character_2.rect.y + 30, facing, 8 * facing, type=0))
                    cooldawn_second2 = pygame.time.get_ticks()
            if p2 == 'garri':
                if (pygame.time.get_ticks() - cooldawn_second2) >= 7000 and game_over == False:
                    healthing.shield_2 = True
                    healthing.s2_hp = 15
                    healthing.blhp2 = 60
                    cooldawn_second2 = pygame.time.get_ticks()
            if p2 == 'drako':
                if count <= 0 and (pygame.time.get_ticks() - cooldawn_second2) >= 10000 and game_over == False and healthing.p2_hp <= 90:
                    healthing.draw_healthbar(-10, 582, 46, 1, character_2)
                    print(healthing.p2_hp)
                    cooldawn_second2 = pygame.time.get_ticks()


        for bul in all_shots:
            if not bul.move(character_1, character_2, last_move) or abs(bul.x - bul.zero_x) >= MAX_DISTANCE and bul.type != 20:
                bul.last_image()
                all_shots.pop(all_shots.index(bul))
        for shoot in all_shots_s:
            if not shoot.move(character_1, character_2, last_move_s) or abs(shoot.x - shoot.zero_x) >= MAX_DISTANCE and shoot.type != 20:
                shoot.last_image()
                all_shots_s.pop(all_shots_s.index(shoot))

        if game_over == False:
            if character_1.living == False:
                points[1] += 1
                add_to_database_1(p2)

                game_over = True
                pygame.mixer.music.load('data/sound/win_sound.mp3')
                pygame.mixer.music.play(1)
                fight_time = pygame.time.get_ticks()

            elif character_2.living == False:
                points[0] += 1
                add_to_database_1(p1)

                game_over = True
                pygame.mixer.music.load('data/sound/win_sound.mp3')
                pygame.mixer.music.play(1)
                fight_time = pygame.time.get_ticks()
        else:
            if character_1.living == False:
                draw_count(p2 + ' win!', font, RED, 320, 180)
            elif character_2.living == False:
                draw_count(p1 + ' win!', font, RED, 320, 180)
            if pygame.time.get_ticks() - fight_time > GAME_OVER_COOLDOWN:
                game_over = False
                count = 3
                character_1 = player_one(p1)
                character_2 = player_two(p2)
                healthing.update()

        pygame.display.flip()
        pygame.display.update()
    pygame.quit()
