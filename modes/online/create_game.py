
import pygame

from gui.menu_items import CreateGameScreen as Menu
from gui.menu_items import BACKGROUND, BACK, BACK_G, SOON
from gui.menu_items import ipaddress


def draw_screen(screen):
    screen.blit(BACKGROUND, (0, 0))
    screen.blit(Menu.WAIT,  (150, 200))
    screen.blit(Menu.IP, (250, 320))
    screen.blit(ipaddress("192.168.1.15"),  (300, 370))
    s = pygame.Surface((750, 650))
    s.set_alpha(128)
    s.fill((0, 0, 0))
    screen.blit(s, (0, 0))
    screen.blit(SOON, (200, 270))
    screen.blit(BACK, (50, 550))


def main(screen):
    clock = pygame.time.Clock()
    while True:
        clock.tick(24)
        draw_screen(screen)
        x, y = pygame.mouse.get_pos()

        if 50 < x < 120 and 550 < y < 600:
            screen.blit(BACK_G, (50, 550))
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return 0

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 50 < x < 120 and 550 < y < 600:
                    return 1
        pygame.display.update()
