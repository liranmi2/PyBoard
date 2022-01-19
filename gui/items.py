
import os.path
import pygame


pygame.font.init()

# headings and labels

HFONT = os.path.join("src", "fonts", "PostNoBillsColombo-Medium.ttf")
SHFONT = os.path.join("src", "fonts", "PostNoBillsColombo-Regular.ttf")
FONT = os.path.join("src", "fonts", "PostNoBillsColombo-Light.ttf")

heading = pygame.font.Font(HFONT, 105)
small_heading = pygame.font.Font(HFONT, 70)
large = pygame.font.Font(FONT, 60)
medium = pygame.font.Font(FONT, 55)
small = pygame.font.Font(FONT, 40)
tiny = pygame.font.Font(HFONT, 18)

WHITE = (255, 255, 255)
GRAY = (190, 190, 190)


# images
BACKGROUND = pygame.image.load(os.path.join("src", "img", "bg.jpg"))
ICON = pygame.image.load(os.path.join("src", "img", "icon.jpg"))

# buttons
BACK = small.render("Back", True, WHITE)
BACK_G = small.render("Back", True, GRAY)


class MainMenu:
    HEADING = heading.render("PyBoard", True, WHITE)
    SINGLE = large.render("Single player", True, WHITE)
    SINGLE_G = large.render("Single player", True, GRAY)
    MULTI = large.render("Multiplayer", True, WHITE)
    MULTI_G = large.render("Multiplayer", True, GRAY)
    COPY = tiny.render("© All rights reserved to Liran, Elad and Stav - Shenkar Software Engineering", True, WHITE)


class SinglePlayerMenu:
    LEVEL = small_heading.render("Choose Level", True, WHITE)
    EASY = medium.render("Easy", True, WHITE)
    EASY_G = medium.render("Easy", True, GRAY)
    MEDIUM = medium.render("Medium", True, WHITE)
    MEDIUM_G = medium.render("Medium", True, GRAY)
    HARD = medium.render("Hard", True, WHITE)
    HARD_G = medium.render("Hard", True, GRAY)


class MultiplayerMenu:
    LOCATE = small_heading.render("Choose Location", True, WHITE)
    LOCAL = large.render("Local", True, WHITE)
    LOCAL_G = large.render("Local", True, GRAY)
    ONLINE = large.render("Online", True, WHITE)
    ONLINE_G = large.render("Online", True, GRAY)


class OnlineMenu:
    HEADING = heading.render("Online", True, WHITE)
    CREATE = large.render("Create Game", True, WHITE)
    CREATE_G = large.render("Create Game", True, GRAY)
    JOIN = large.render("Join Game", True, WHITE)
    JOIN_G = large.render("Join Game", True, GRAY)


def ipaddress(address):
    ipadd = small.render(address, True, WHITE)
    return ipadd


class CreateGameScreen:
    WAIT = large.render("Waiting for opponent...", True, WHITE)
    IP = small.render("Your IP address is:", True, WHITE)


class JoinGameScreen:
    ENTER = large.render("Please enter IP address:", True, WHITE)


# class MultiplayerMenu:
#
#
#
# class OnlineMenu:
#
#
