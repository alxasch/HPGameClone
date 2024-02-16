import pygame
from load_other import load_image, load_sound
from character import Character


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
GAME_OVER_COOLDOWN = 3000
MAX_DISTANCE = 350

BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BROWN = (73, 36, 0)
# SKY = (27, 85, 131)
SKY = (66, 170, 255)
RED = (165, 42, 42)
FPS = 60
alpha = 128
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


garri_sprite = load_image(['garri.png'])
germiona_sprite = load_image(["germiona.png"])
ron_sprite = load_image(['ron.png'])
drako_sprite = load_image(['drako.png'])

stat = load_image(['menu', 'statistic.png'])
static_sprite = pygame.transform.scale(stat, (530, 270))

name_font = pygame.font.Font("data/font/Seminaria.ttf", 23)
point_font = pygame.font.Font("data/font/Seminaria.ttf", 50)
count_font = pygame.font.Font("data/font/Seminaria.ttf", 150)
score_font = pygame.font.Font("data/font/Seminaria.ttf", 100)

# shot_sprite = pygame.image.load('data/shots/spritesheet_shots.png')
exp_image = load_image(['exp_icon.png'])
protego_image = load_image(['protego_icon.png'])
depulso_image = load_image(['depulso_icon.png'])
bombarda_image = load_image(['bombarda_icon.png'])
heal_image = load_image(['heal_spell_icon.png'])

star_image = load_image(['ability', 'star.png'])
sprite_star = []
for k in range(7):
    img = star_image.subsurface(k * 602, 0, 602, 489)
    sprite_star.append(pygame.transform.scale(img, (602 * 0.4, 489 * 0.4)))
bomb_sprite = load_image(['shots', 'bomb_sprite.png'])

shot_sprite = load_image(['shots', 'spritesheet_blue_shot.png'])
shot_image = load_image(['shot.png'])

last_shot = load_image(['shots', 'dead_fireball.png'])
last_img = []
for i in range(5):
    img = last_shot.subsurface(i * 100, 0, 100, 100)
    last_img.append(pygame.transform.scale(img, (100 * 1, 100 * 1)))

bomb_dead = load_image(['shots', 'bomb_dead.png'])
last_bomb = []
for i in range(8):
    img = bomb_dead.subsurface(i * 60, 0, 60, 60)
    last_bomb.append(pygame.transform.scale(img, (60 * 2, 60 * 2)))

shield = load_image(['ability', 'shield_test.png'])
shield_image = pygame.transform.scale(shield, (190, 190))

hp_list = [[name, load_image([f'hp_{name}.png'])] for name in ['germiona', 'garri', 'drako', 'ron']]

hp_list = [[el[0], pygame.transform.scale(el[1], (90, 90))] for el in hp_list]

hp_icon = load_image(['icon_hp.png'])
hp_sprite = pygame.transform.scale(hp_icon, (400, 110))
hp_sprite2 = pygame.transform.flip(hp_sprite, True, False)

hp_blue = load_image(['blue_hp.png'])
shield_hp = pygame.transform.scale(hp_blue, (255, 20))

cloud_imgs = [pygame.image.load("data/background/cloudy1.png").convert_alpha(),
              pygame.image.load("data/background/cloudy2.png").convert_alpha(),
              pygame.image.load("data/background/cloudy3.png").convert_alpha()]

bg_img = [pygame.image.load(f'data/background/flag{i}.png') for i in range(1, 6)]
bg_img = list(pygame.transform.scale(x, (SCREEN_WIDTH, SCREEN_HEIGHT)) for x in bg_img)

# SIZE_SHOT = 150
SIZE_SHOT_W, SIZE_SHOT_H = 120, 95
SIZE_BOMB_W, SIZE_BOMB_H = 20, 30
SIZE_SPRITE = 50

SCALE = 4 # увеличение спрайта
# SCALE_SHOT = 0.3
SCALE_SHOT = 0.4
SCALE_BOMB = 2

SPRITE_INFO = [SIZE_SPRITE, SCALE]
SHOT_INFO = [[SIZE_SHOT_W, SIZE_SHOT_H], SCALE_SHOT]
BOMB_INFO = [[SIZE_BOMB_W, SIZE_BOMB_H], SCALE_BOMB]

SHEET_SHOT = [8]
SHEET_BOMB = [7]
ANIMATION_SHEET_GARRI = [1, 5, 3, 2, 1, 1]
GERMIONA_SHEET = [1, 6, 3, 2, 1, 1]
RON_SHEET = [1, 5, 3, 2, 1, 1]
DRAKO_SHEET = [1, 5, 3, 2, 1, 1]
