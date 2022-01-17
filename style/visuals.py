
import os.path
import pygame


# headings and labels

pygame.font.init()
FONT = os.path.join("src", "fonts", "PostNoBillsColombo-Light.ttf")

header = pygame.font.Font(FONT, 105)
large = pygame.font.Font(FONT, 60)
medium = pygame.font.Font(FONT, 52)
small = pygame.font.Font(FONT, 40)
tiny = pygame.font.Font(FONT, 25)



# images

BACKGROUND = pygame.image.load(os.path.join("src", "img", "bg.jpg"))

