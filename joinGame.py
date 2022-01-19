
import pygame

# from ext.pyBox import TextBox
from gui.items import JoinGameScreen as Menu
from gui.items import BACKGROUND, BACK, BACK_G
# from onlinemenu import main as onlinemenu


def draw_screen(screen):
    screen.blit(BACKGROUND, (0, 0))
    screen.blit(Menu.ENTER,  (180, 100))
    screen.blit(BACK, (50, 550))


# def play():


def main(screen):
    clock = pygame.time.Clock()
    # box = TextBox(FONT, (0, 0, 0), (65, 350, 200, 35))
    while True:
        clock.tick(24)
        draw_screen(screen)
        x, y = pygame.mouse.get_pos()

        # # Menu items will turn gray while hovering them
        # if localCoord[0] < x < sum(localCoord[::2]) and localCoord[1] < y < sum(localCoord[1::2]):
        #     screen.blit(Menu.LOCAL_G, localCoord[:2])
        #
        # if onlineCoord[0] < x < sum(onlineCoord[::2]) and onlineCoord[1] < y < sum(onlineCoord[1::2]):
        #     screen.blit(Menu.ONLINE_G, onlineCoord[:2])
        #
        # if 50 < x < 120 and 550 < y < 600:
        #     screen.blit(BACK_G, (50, 550))
        #
        # for event in pygame.event.get():
        #
        #     if event.type == pygame.QUIT:
        #         return 0
        #
        #     elif event.type == pygame.MOUSEBUTTONDOWN:
        #         x, y = event.pos
        #         if 50 < x < 120 and 550 < y < 600:
        #             return 1
        #         # if localCoord[0] < x < sum(localCoord[::2]) and localCoord[1] < y < sum(localCoord[1::2]):
        #         #     play()
        #         if onlineCoord[0] < x < sum(onlineCoord[::2]) and onlineCoord[1] < y < sum(onlineCoord[1::2]):
        #             ret = onlinemenu(screen)
        #             if ret == 0:
        #                 return 0
        pygame.display.update()
