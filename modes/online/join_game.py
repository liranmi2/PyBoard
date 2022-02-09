
import pygame


from gui.menu_items import JoinGameScreen as Menu
from gui.menu_items import BACKGROUND, BACK, BACK_G, medium, SOON


def draw_screen(screen):
    screen.blit(BACKGROUND, (0, 0))
    screen.blit(Menu.ENTER,  (180, 250))
    s = pygame.Surface((750, 650))
    s.set_alpha(128)
    s.fill((0, 0, 0))
    screen.blit(s, (0, 0))
    screen.blit(SOON, (200, 270))
    screen.blit(BACK, (50, 550))


def main(screen):
    # user_text = ''
    #
    # input_rect = pygame.Rect(250, 330, 300, 75)
    # active_rect = pygame.Rect(251, 331, 298, 73)
    #
    # active = False
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

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 50 < x < 120 and 550 < y < 600:
                    return 1
        #         if input_rect.collidepoint(event.pos):
        #             active = True
        #         else:
        #             active = False
        #
        #     if event.type == pygame.KEYDOWN:
        #
        #         if event.key == pygame.K_BACKSPACE:
        #             user_text = user_text[:-1]
        #
        #         else:
        #             user_text += event.unicode
        #
        #
        # pygame.draw.rect(screen, (255, 255, 255), input_rect, border_radius=8)
        # if active:
        #     pygame.draw.rect(screen, pygame.Color('blue'), active_rect, 2, 8)
        # text_surface = medium.render(user_text, True, (0, 0, 0))
        # screen.blit(text_surface, (input_rect.x + 50, input_rect.y + 5))

        pygame.display.update()
