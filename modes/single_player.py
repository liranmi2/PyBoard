
import pygame

from gui.menu_items import SinglePlayerMenu as Menu
from gui.menu_items import BACKGROUND, BACK, BACK_G
from engine.moves import play


easyCoord = (330, 240, 90, 70)
mediumCoord = (305, 310, 140, 70)
hardCoord = (330, 380, 90, 70)


def draw_menu(screen):
    screen.blit(BACKGROUND, (0, 0))
    screen.blit(Menu.LEVEL, (210, 100))
    screen.blit(Menu.EASY, easyCoord[:2])
    screen.blit(Menu.MEDIUM, mediumCoord[:2])
    screen.blit(Menu.HARD, hardCoord[:2])
    screen.blit(BACK, (50, 550))


def main(screen):
    clock = pygame.time.Clock()
    while True:
        clock.tick(24)
        draw_menu(screen)
        x, y = pygame.mouse.get_pos()

        # Menu items will turn gray while hovering them
        if pygame.Rect(easyCoord).collidepoint(pygame.mouse.get_pos()):
            screen.blit(Menu.EASY_G, easyCoord[:2])

        if pygame.Rect(mediumCoord).collidepoint(pygame.mouse.get_pos()):
            screen.blit(Menu.MEDIUM_G, mediumCoord[:2])

        if pygame.Rect(hardCoord).collidepoint(pygame.mouse.get_pos()):
            screen.blit(Menu.HARD_G, hardCoord[:2])

        if 50 < x < 120 and 550 < y < 600:
            screen.blit(BACK_G, (50, 550))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            elif event.type == pygame.MOUSEBUTTONDOWN:

                if pygame.Rect(50, 550, 120, 600).collidepoint(event.pos):
                    return 1

                if pygame.Rect(easyCoord).collidepoint(event.pos):
                    ret = play(screen, "single player", 1)
                    if ret == 0:
                        return ret

                if pygame.Rect(mediumCoord).collidepoint(event.pos):
                    ret = play(screen, "single player", 2)
                    if ret == 0:
                        return ret

                if pygame.Rect(hardCoord).collidepoint(event.pos):
                    ret = play(screen, "single player", 3)
                    if ret == 0:
                        return ret

        pygame.display.update()
