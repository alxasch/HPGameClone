import pygame
import sys
import os
from load_other import load_sound, load_image
from load_image_button import LoadImage
from main import play_g
from const import *
import pygame.mixer
from database import get_the_value


pygame.init()


BLACK = (0, 0, 0)
FPS = 100
width = 1000
height = 600

surface = pygame.display.Info()
size = width, height
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Hogwarts Duel')
check_score_event = pygame.USEREVENT + 1
pygame.time.set_timer(check_score_event, 1000)
clock = pygame.time.Clock()

# создание кнопок
button_start = LoadImage(width / 2 - (242 / 2), 300, 252, 74,
                         ['menu', 'start_but.png'], ['menu', 'start_but_2.png'])
button_options = LoadImage(width / 2 - (242 / 2), 400, 252, 74,
                         ['menu', 'option_but.png'], ['menu', 'option_but_2.png'])
button_exit = LoadImage(width / 2 - (242 / 2), 500, 252, 74,
                         ['menu', 'exit_but.png'], ['menu', 'exit_but_2.png'])
button_back = LoadImage(20, 20, 100, 50,['menu', 'back_but.png'], ['menu', 'back_but-2.png'])
garri_page = LoadImage(width / 2 - 200, 300, 129, 176,
                       ['menu', 'garri.png'])
germiona_page = LoadImage(width / 2 - 71, 300, 129, 176,
                       ['menu', 'germiona.png'])
ron_page = LoadImage(width / 2 + 58, 300, 129, 176,
                       ['menu', 'ron.png'])
drako_page = LoadImage(width / 2 + 187, 300, 129, 176,
                       ['menu', 'drako.png'])
# cur_sprite = pygame.sprite.Group()
# sprite = pygame.sprite.Sprite()
# sprite.image = load_image(['menu', 'cursor.png'])
# sprite.rect = sprite.image.get_rect()
# cur_sprite.add(sprite)


def options():
    run = True
    fon = pygame.transform.scale(load_image(['menu', 'fon_option_2.jpg']), (width, height))
    while run:
        screen.fill(BLACK)
        screen.blit(fon, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    shading()
                    run = False
            if event.type == pygame.MOUSEBUTTONDOWN and button_back.pressure:
                shading()
                run = False
            button_back.mouse_event(event)
        button_back.pressure_test(pygame.mouse.get_pos())
        button_back.update(screen)
        pygame.display.flip()


def menu_game():
    run = True
    change = 1
    play = False
    player1, player2 = False, False
    fon = pygame.transform.scale(load_image(['menu', 'fon_menu_play.jpg']), (width, height))
    print(get_the_value())
    while run:
        screen.fill(BLACK)
        screen.blit(fon, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    shading()
                    for btn in [germiona_page, garri_page, ron_page, drako_page]:
                        btn.choice = False
                        btn.selected_color = (0, 0, 0, 0)
                    run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for btn in [[germiona_page, 'germiona'], [garri_page, 'garri'], [ron_page, 'ron'], [drako_page, 'drako']]:
                    btn[0].pressure_test([x, y])
                    if btn[0].pressure and change == 1 and not btn[0].choice:
                        btn[0].selected_color = (255, 0, 0)
                        btn[0].choice = True
                        change = 2
                        player1 = btn[1]
                    elif btn[0].pressure and change == 2 and not btn[0].choice:
                        btn[0].selected_color = (27, 42, 207)
                        btn[0].choice = True
                        change = 0
                        player2 = btn[1]
                        play = True
                        print('p1: ' + player1, 'p2: ' + player2)
            if event.type == pygame.MOUSEBUTTONDOWN and button_back.pressure:
                shading()
                for btn in [germiona_page, garri_page, ron_page, drako_page]:
                    btn.choice = False
                    btn.selected_color = (0, 0, 0, 0)
                run = False
            button_back.mouse_event(event)
        button_back.pressure_test(pygame.mouse.get_pos())
        for but in [germiona_page, garri_page, button_back, ron_page, drako_page]:
            but.update(screen)
            if but.choice:
                pygame.draw.rect(screen, but.selected_color, (but.x, but.y, but.width, but.height), 5)
        if play:
            pygame.mixer.music.stop()
            shading()
            for btn in [germiona_page, garri_page, ron_page, drako_page]:
                btn.choice = False
                btn.selected_color = (0, 0, 0, 0)
            play_g(player1, player2)
            run = False
        pygame.display.flip()

#def cursor():
    #x, y = pygame.mouse.get_pos()
    #sprite.rect.x = x
    #sprite.rect.y = y
    #cur_sprite.draw(screen)


def terminate():
    pygame.quit()
    sys.exit()


def menu_start():
    running = True
    pygame.mixer.music.load('data/sound/main_theme.mp3')
    pygame.mixer.music.play(-1)
    fon = pygame.transform.scale(load_image(['menu', 'hogvarts_2.jpg']), (width, height))
    # name = pygame.transform.scale(load_image(['menu', 'name.png']), (width / 2, 100))
    screen.blit(fon, (0, 0))
    # screen.blit(name, (100, 100))
    # pygame.mouse.set_visible(False)
    while running:
        screen.fill(BLACK)
        screen.blit(fon, (0, 0))
        # screen.blit(name, (100, 100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            # if pygame.mouse.get_focused():
                # cursor()
            if event.type == pygame.MOUSEBUTTONDOWN and button_options.pressure:
                shading()
                options()
            if event.type == pygame.MOUSEBUTTONDOWN and button_start.pressure:
                shading()
                menu_game()
            if event.type == pygame.MOUSEBUTTONDOWN and button_exit.pressure:
                terminate()
            for button in [button_start, button_options, button_exit]:
                button.mouse_event(event)
        for button in [button_start, button_options, button_exit]:
            button.pressure_test(pygame.mouse.get_pos())
            button.update(screen)
        pygame.display.flip()
        clock.tick(FPS)


def shading(): # затемнение экрана
    alpha = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen2 = pygame.Surface((width, height))
        screen2.fill(BLACK)
        screen2.set_alpha(alpha)
        screen.blit(screen2, (0, 0))
        alpha += 5
        if alpha >= 105:
            alpha = 255
            running = False
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    menu_start()