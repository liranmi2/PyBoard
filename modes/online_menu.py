
import pygame

from gui.menu_items import OnlineMenu as Menu
from gui.menu_items import BACKGROUND, BACK, BACK_G
from modes.online.create_game import main as creategamescreen
from modes.online.join_game import main as joingamescreen

createCoord = (250, 250, 270, 70)
joinCoord = (270, 350, 230, 70)


def draw_menu(screen):
    screen.blit(BACKGROUND, (0, 0))
    screen.blit(Menu.HEADING,  (270, 100))
    screen.blit(Menu.CREATE, createCoord[:2])
    screen.blit(Menu.JOIN, joinCoord[:2])
    screen.blit(BACK, (50, 550))


def main(screen):
    clock = pygame.time.Clock()
    while True:
        clock.tick(24)
        draw_menu(screen)
        x, y = pygame.mouse.get_pos()

        # Menu items will turn gray while hovering them
        if createCoord[0] < x < sum(createCoord[::2]) and createCoord[1] < y < sum(createCoord[1::2]):
            screen.blit(Menu.CREATE_G, createCoord[:2])

        if joinCoord[0] < x < sum(joinCoord[::2]) and joinCoord[1] < y < sum(joinCoord[1::2]):
            screen.blit(Menu.JOIN_G, joinCoord[:2])

        if 50 < x < 120 and 550 < y < 600:
            screen.blit(BACK_G, (50, 550))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return 0

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 50 < x < 120 and 550 < y < 600:
                    return 1
                if pygame.Rect(createCoord).collidepoint(pygame.mouse.get_pos()):
                    ret = creategamescreen(screen)
                    if ret == 0:
                        return 0
                if pygame.Rect(joinCoord).collidepoint(pygame.mouse.get_pos()):
                    ret = joingamescreen(screen)
                    if ret == 0:
                        return 0
        pygame.display.update()
