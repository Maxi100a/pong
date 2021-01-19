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
from Utilities import TEXT_FONT, HEIGHT, WIDTH, MENU_FONT
from Player import Player
from Ball import Ball
from Button import Button
from Slider import Slider
from SliderCircle import SliderCircle

# Constants
BALL = Ball()
PLAYER1 = Player((WIDTH, HEIGHT / 2), 1)
PLAYER2 = Player((0, HEIGHT / 2), 2)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT)) 
FPS = pygame.time.Clock()

start_button = Button("Start!", (WIDTH / 2 - 100, HEIGHT - 50), \
    bg=(69, 171, 0), hc=(41, 102, 0))
quit_button = Button("Quit", ((WIDTH / 2) + 100, HEIGHT - 50), \
    bg=(240, 0, 0), hc=(143, 0, 0))
slow_button = Button("Slow", ((WIDTH / 2) - 115, HEIGHT / 2 + 90), \
    bg=(255, 0, 0), hc=(200, 0, 0), font=MENU_FONT, size=(100, 35))
medium_button = Button("Medium", ((WIDTH / 2), HEIGHT / 2 + 90), \
    bg=(200, 200, 0), hc=(155, 155, 0), font=MENU_FONT, size=(100, 35))
fast_button = Button("Fast", ((WIDTH / 2) + 115, HEIGHT / 2 + 90), \
    bg=(0, 255, 0), hc=(0, 200, 0), font=MENU_FONT, size=(100, 35))

size_slider = Slider()
slider_circle = SliderCircle(size_slider.height)

def quit_game():
    """ Shuts down the game """
    print("Good bye! :(")
    pygame.quit()
    sys.exit()

def setup():
    """ Sets up the pygame """
    pygame.init()
    pygame.display.set_caption("Pong")

def add_sprites(sprites):
    """ Add the sprites to the passed sprite group """
    sprites.add(start_button)
    sprites.add(quit_button)
    sprites.add(slow_button)
    sprites.add(medium_button)
    sprites.add(fast_button)
    sprites.add(size_slider)
    sprites.add(slider_circle)

def change_speed(new_speed):
    """ Changes the speeds of the ball and both players """
    BALL.x_vel = new_speed
    BALL.y_vel = new_speed
    PLAYER1.vel = new_speed
    PLAYER2.vel = new_speed

def paint_messages():
    """ Paints the welcome and the game speed messages """
    welcome_msg = TEXT_FONT.render("Welcome to Pong!", True, (255, 255, 255))
    welcome_msg_rect = welcome_msg.get_rect(center=(WIDTH / 2, 100))
    ball_speed = MENU_FONT.render("Game Speed", True, (255, 255, 255))
    ball_speed_rect = ball_speed.get_rect(center=(WIDTH/2, HEIGHT / 2 + 50))

    SCREEN.blit(welcome_msg, welcome_msg_rect)
    SCREEN.blit(ball_speed, ball_speed_rect)

def start_screen():
    """ Presents the start screen, allowing user to specify settings """
    sprites = pygame.sprite.Group()
    add_sprites(sprites)

    start = True
    while start:
        SCREEN.fill((0, 0, 0)) # paint screen black

        # capture the mouse
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            # Handling quitting
            if event.type == pygame.QUIT:
                quit_game()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_button.rect.collidepoint(mouse_pos): # click quit
                    quit_game()

                if start_button.rect.collidepoint(mouse_pos): # click start
                    start = False

                if slow_button.rect.collidepoint(mouse_pos): # click slow
                    change_speed(5)

                if medium_button.rect.collidepoint(mouse_pos): # click medium
                    change_speed(7)

                if fast_button.rect.collidepoint(mouse_pos): # click fast
                    change_speed(10)

                if slider_circle.rect.collidepoint(mouse_pos): # holding the slider
                    slider_circle.held = True


            if event.type == pygame.MOUSEBUTTONUP:
                if slider_circle.held: # let go of the slider
                    slider_circle.held = False

        paint_messages()

        # Draw each sprite
        for sprite in sprites:
            sprite.draw(SCREEN)

        # Paint a player for displaying current length
        SCREEN.blit(PLAYER2.surf, PLAYER1.rect)

        # Handle slider_circle moving
        slider_circle.move(PLAYER1, PLAYER2)

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

    run = True
    while run:
        SCREEN.fill((0,0,0)) # Paint screen black
        paint_score(BALL.p1_score, BALL.p2_score) # paint score method

        # handle quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        # handle mouse click
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    PLAYER1.reset((WIDTH, HEIGHT / 2))
                    PLAYER2.reset((0, HEIGHT / 2))
                    run = False
                    main()

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
