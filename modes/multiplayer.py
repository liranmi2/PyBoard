
import pygame

from gui.menu_items import MultiplayerMenu as Menu
from gui.menu_items import BACKGROUND, BACK, BACK_G
from modes.online_menu import main as onlinemenu
from engine.moves import play


localCoord = (330, 250, 120, 70)
onlineCoord = (320, 350, 130, 70)


def draw_menu(screen):
    screen.blit(BACKGROUND, (0, 0))
    screen.blit(Menu.LOCATE,  (180, 100))
    screen.blit(Menu.LOCAL, localCoord[:2])
    screen.blit(Menu.ONLINE, onlineCoord[:2])
    screen.blit(BACK, (50, 550))


def main(screen):
    clock = pygame.time.Clock()
    while True:
        clock.tick(24)
        draw_menu(screen)
        x, y = pygame.mouse.get_pos()

        # Menu items will turn gray while hovering them
        if localCoord[0] < x < sum(localCoord[::2]) and localCoord[1] < y < sum(localCoord[1::2]):
            screen.blit(Menu.LOCAL_G, localCoord[:2])

        if onlineCoord[0] < x < sum(onlineCoord[::2]) and onlineCoord[1] < y < sum(onlineCoord[1::2]):
            screen.blit(Menu.ONLINE_G, onlineCoord[:2])

        if 50 < x < 120 and 550 < y < 600:
            screen.blit(BACK_G, (50, 550))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return 0

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 50 < x < 120 and 550 < y < 600:
                    return 1
                if pygame.Rect(onlineCoord).collidepoint(pygame.mouse.get_pos()):
                    ret = onlinemenu(screen)
                    if ret == 0:
                        return 0
                if pygame.Rect(localCoord).collidepoint(pygame.mouse.get_pos()):
                    ret = play(screen, "multiplayer")
                    if ret == 0:
                        return 0

        pygame.display.update()
