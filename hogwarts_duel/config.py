import pygame

pygame.init()
surface = pygame.display.Info()
width = int(surface.current_w)
height = int(surface.current_h)
size = width, height
screen = pygame.display.set_mode(size)
FPS = 100
chek_score_event = pygame.USEREVENT + 1
pygame.time.set_timer(chek_score_event, 1000)