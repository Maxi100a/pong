"""
sys - system
random - for random numbers
pygame - for GUI
Player - the necessary player Class
Ball - the necessary ball class
Utilities: TEXT_FONT, HEIGHT, WIDTH
"""
import sys
import pygame
from Utilities import TEXT_FONT, HEIGHT, WIDTH
from Player import Player
from Ball import Ball

# Constants
BALL = Ball()
PLAYER1 = Player((WIDTH, HEIGHT / 2), 1)
PLAYER2 = Player((0, HEIGHT / 2), 2)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = pygame.time.Clock()

def quit_game():
    """ Shuts down the game """
    print("Good bye! :(")
    pygame.quit()
    sys.exit()

def setup():
    """ Sets up the pygame """
    pygame.init()
    pygame.display.set_caption("Pong")

def start_screen():
    """ Presents the start screen, allowing user to specify settings """
    start_button = Button("Start!", (WIDTH / 2 - 100, HEIGHT - 50), None, \
        bg=(69, 171, 0), hc=(41, 102, 0))
    quit_button = Button("Quit", ((WIDTH / 2) + 100, HEIGHT - 50), None, \
        bg=(240, 0, 0), hc=(143, 0, 0))

    sprites = pygame.sprite.Group()
    sprites.add(start_button)
    sprites.add(quit_button)

    start = True
    while start:
        # capture the mouse
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            # Handling quitting
            if event.type == pygame.QUIT:
                quit_game()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_button.rect.collidepoint(mouse_pos):
                    quit_game()

                if start_button.rect.collidepoint(mouse_pos):
                    start = False

        SCREEN.fill((0, 0, 0))

        welcome_msg = TEXT_FONT.render("Welcome to Pong!", True, (255, 255, 255))

        for sprite in sprites:
            sprite.draw()

        SCREEN.blit(welcome_msg, ((WIDTH / 2) - 130, 100))

        # update the display
        pygame.display.update()

def paint_score(p1_score, p2_score):
    """ Paints the score """
    score = TEXT_FONT.render(str(p1_score) + ' : ' +\
        str(p2_score), True, (255, 255, 255))

    SCREEN.blit(score, ((WIDTH / 2) - score.get_rect().center[0], \
            HEIGHT - score.get_rect().bottom ))

def game_loop():
    """ Loop to handle the actual game function"""
    # Create a sprite group
    sprites = pygame.sprite.Group()
    sprites.add(BALL)
    sprites.add(PLAYER1)
    sprites.add(PLAYER2)

    while True:
        SCREEN.fill((0,0,0)) # Paint screen black
        paint_score(BALL.p1_score, BALL.p2_score) # paint score method

        # handle quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # handle mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse)

        # paint the sprites
        for entity in sprites:
            SCREEN.blit(entity.surf, entity.rect)

        # check for collision
        if BALL.rect.colliderect(PLAYER1):
            BALL.collide(PLAYER1)
        elif BALL.rect.colliderect(PLAYER2):
            BALL.collide(PLAYER2)

        # handle moving each sprite
        PLAYER1.move()
        PLAYER2.move()
        BALL.move()

        pygame.display.update()
        FPS.tick(60)

class Button(pygame.sprite.Sprite):
    """
    The button class (Will handle default buttons)
    """

    def __init__(self, text, loc, action, size=(150, 50), bg=(255, 255, 255), hc=(0,0,0), tc=(255, 255, 255)):
        super().__init__()
   
        # other attributes
        self.size = size
        self.call_back = action
        self.bg = bg
        self.color = bg
        self.hover_color = hc

        # surface
        self.surf = pygame.surface.Surface(size)
        self.rect = self.surf.get_rect(center=loc)


        # button text
        self.text = text
        self.font = TEXT_FONT
        self.text_surf = self.font.render(self.text, True, tc)
        self.text_rect = self.text_surf.get_rect(center = [s//2 for s in self.size])

    def draw(self):
        self.mouseover()
        self.surf.fill(self.bg)
        self.surf.blit(self.text_surf, self.text_rect)
        SCREEN.blit(self.surf, self.rect)

    def mouseover(self):
        self.bg = self.color

        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.bg = self.hover_color
def main():
    """ Main loop. """
    setup()
    start_screen()
    game_loop()

if __name__ == "__main__":
    main()
