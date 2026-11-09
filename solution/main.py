import pygame as pg
import sys
import classes


# Initialize Pygame and create the shared display used by every screen.
pg.init()


SCREEN = pg.display.set_mode((1280,720))
pg.display.set_caption("Main Menu")

# Load the image used as the main-menu background.
BG = pg.image.load("background.jpg")


def play():
    """Display the game placeholder screen until the user returns or exits."""
    pg.display.set_caption("Game Screen")

    while True:

        # Redraw the screen and update the back button's hover state each frame.
        PLAY_MOUSE_POS = pg.mouse.get_pos()

        SCREEN.fill('black')

        PLAY_TEXT = pg.font.SysFont('comicsans', 45).render("This is the Game Screen", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = classes.Button(image=None, pos=(640, 460), text_input="BACK", font=pg.font.SysFont('comicsans', 75), base_colour="#d7fcd4", hovering_colour="White")
        
        PLAY_BACK.change_colour(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        # Handle window-close and back-button input.
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if PLAY_BACK.check_for_input(PLAY_MOUSE_POS):
                    main_menu()

        pg.display.update()


def options():
    """Display the options placeholder screen and its return button."""
    pg.display.set_caption("Options Screen")

    while True:

        # Redraw the screen and update the back button's hover state each frame.
        OPTIONS_MOUSE_POS = pg.mouse.get_pos()

        SCREEN.fill('black')

        OPTIONS_TEXT = pg.font.SysFont('comicsans', 45).render("This is the Options Screen", True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = classes.Button(image=None, pos=(640, 460), text_input="BACK", font=pg.font.SysFont('comicsans', 75), base_colour="#d7fcd4", hovering_colour="White")
        
        OPTIONS_BACK.change_colour(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        # Handle window-close and back-button input.
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.check_for_input(OPTIONS_MOUSE_POS):
                    main_menu()

        pg.display.update()


def main_menu():
    """Show the main menu and route button clicks to the selected screen."""
    pg.display.set_caption("MAZE RAIDER")

    while True:
        # Draw the background, title, and buttons for the current frame.
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pg.mouse.get_pos()

        MENU_TEXT = pg.font.SysFont('comicsans', 100).render("MAZE RAIDER", True, "#f0eeeb")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = classes.Button(image=None, pos=(640, 250), text_input="PLAY", font=pg.font.SysFont('comicsans', 75), base_colour="#d7fcd4", hovering_colour="White")
        OPTIONS_BUTTON = classes.Button(image=None, pos=(640, 350), text_input="OPTIONS", font=pg.font.SysFont('comicsans', 75), base_colour="#d7fcd4", hovering_colour="White")
        QUIT_BUTTON = classes.Button(image=None, pos=(640, 450), text_input="QUIT", font=pg.font.SysFont('comicsans', 75), base_colour="#d7fcd4", hovering_colour="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.change_colour(MENU_MOUSE_POS)
            button.update(SCREEN)

        # Dispatch menu selections or exit when the window is closed.
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.check_for_input(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.check_for_input(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.check_for_input(MENU_MOUSE_POS):
                    pg.quit()
                    sys.exit()

        pg.display.update()


# Start the application on the main menu.
main_menu()
