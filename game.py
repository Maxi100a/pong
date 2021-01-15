"""
sys - system
random - for random numbers
pygame - for GUI
Player - the necessary player Class
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

def setup():
    """ Sets up the pygame """
    pygame.init()
    pygame.display.set_caption("Pong")

def start_screen():
    """ Presents the start screen, allowing user to specify settings """
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        SCREEN.fill((0, 0, 0))

        welcome_msg = TEXT_FONT.render("Welcome to Pong!", True, (255, 255, 255))
    
        SCREEN.blit(welcome_msg, )
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
        # handle quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        SCREEN.fill((0,0,0))
        paint_score(BALL.p1_score, BALL.p2_score)

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

def main():
    """ Main loop. """
    setup()
    start_screen()
    game_loop()

if __name__ == "__main__":
    main()
