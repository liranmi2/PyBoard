import sys
import pygame

from gui.menu_items import MainMenu as Main
from gui.menu_items import BACKGROUND, ICON
from modes.single_player import main as singleplayermenu
from modes.multiplayer import main as multiplayermenu
from engine.moves import play

sys.stdout.flush()
pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((750, 650))

pygame.display.set_caption("PyBoard")
pygame.display.set_icon(ICON)

# pygame.display.set_icon(MAIN.ICON)

singleCoord = (250, 250, 255, 70)
multiCoord = (270, 350, 220, 70)


def draw_main_menu():
    screen.blit(BACKGROUND, (0, 0))
    screen.blit(Main.HEADING, (220, 40))
    screen.blit(Main.SINGLE, singleCoord[:2])
    screen.blit(Main.MULTI, multiCoord[:2])
    screen.blit(Main.COPY, (140, 600))
    # pygame.draw.rect(screen, (255, 255, 255), (350, 300, 70, 70), 4, 8)


if __name__ == "__main__":
    run = True
    while run:
        clock.tick(30)
        draw_main_menu()
        x, y = pygame.mouse.get_pos()

        # Menu items will turn gray while hovering them
        if pygame.Rect(singleCoord).collidepoint(pygame.mouse.get_pos()):
            screen.blit(Main.SINGLE_G, singleCoord[:2])

        if pygame.Rect(multiCoord).collidepoint(pygame.mouse.get_pos()):
            screen.blit(Main.MULTI_G, multiCoord[:2])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                if pygame.Rect(singleCoord).collidepoint(event.pos):
                    ret = singleplayermenu(screen)
                    if ret == 0:
                        run = False

                elif pygame.Rect(multiCoord).collidepoint(event.pos):
                    ret = multiplayermenu(screen)
                    if ret == 0:
                        run = False

        pygame.display.flip()

