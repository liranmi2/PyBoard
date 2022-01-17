import sys
import pygame
import style.visuals as vis

sys.stdout.flush()
pygame.init()

screen = pygame.display.set_mode((750, 650))

pygame.display.set_caption("PyBoard")

# pygame.display.set_icon(MAIN.ICON)

singleCoord = (450, 160, 220, 60)
multiCoord = (470, 240, 200, 60)

def drawMainMenu():

    screen.blit(vis.BACKGROUND, (0, 0))




