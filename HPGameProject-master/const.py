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
# SKY = (27, 85, 131)
SKY = (66, 170, 255)
RED = (255, 0, 0)
FPS = 60
alpha = 128
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

garri_sprite = load_image(['garri.png'])
germiona_sprite = load_image(["germiona.png"])
ron_sprite = load_image(['ron.png'])
drako_sprite = load_image(['drako.png'])


# shot_sprite = pygame.image.load('data/shots/spritesheet_shots.png')
exp_image = pygame.image.load('data/exp_icon.png')
protego_image = pygame.image.load('data/protego_icon.png')
depulso_image = pygame.image.load('data/depulso_icon.png')
bombarda_image = pygame.image.load('data/bombarda_icon.png')
heal_image = pygame.image.load('data/heal_spell_icon.png')


shot_sprite = pygame.image.load('data/shots/spritesheet_blue_shot.png')
shot_image = pygame.image.load('data/shot.png')
last_shot = pygame.image.load('data/shots/dead_sprite.png')
last_img = []
for i in range(5):
    img = last_shot.subsurface(i * 120, 0, 120, 95)
    last_img.append(pygame.transform.scale(img, (120 * 0.4, 95 * 0.4)))

shield = pygame.image.load('data/ability/shield_test.png')
shield_image = pygame.transform.scale(shield, (190, 190))

hp_list = [['germiona', pygame.image.load('data/hp_germiona.png')],
           ['garri', pygame.image.load('data/hp_garri.png')],
           ['drako', pygame.image.load('data/hp_drako.png')],
           ['ron', pygame.image.load('data/hp_ron.png')]]

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
SIZE_SHOT_W = 120
SIZE_SHOT_H = 95
SIZE_SPRITE = 50

SCALE = 4 # увеличение спрайта
# SCALE_SHOT = 0.3
SCALE_SHOT = 0.4

SPRITE_INFO = [SIZE_SPRITE, SCALE]
SHOT_INFO = [[SIZE_SHOT_W, SIZE_SHOT_H], SCALE_SHOT]

SHEET_SHOT = [8]
ANIMATION_SHEET_GARRI = [1, 5, 3, 2, 1, 1]
GERMIONA_SHEET = [1, 6, 3, 2, 1, 1]
RON_SHEET = [1, 5, 3, 2, 1, 1]
DRAKO_SHEET = [1, 5, 3, 2, 1, 1]
