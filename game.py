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

    sprites = pygame.sprite.Group()
    sprites.add(start_button)
    sprites.add(quit_button)
    sprites.add(slow_button)
    sprites.add(medium_button)
    sprites.add(fast_button)
    sprites.add(size_slider)
    sprites.add(slider_circle)

    start = True
    while start:
        SCREEN.fill((0, 0, 0))

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

                if slow_button.rect.collidepoint(mouse_pos):
                    BALL.x_vel = 5
                    BALL.y_vel = 5
                    PLAYER1.vel = 5
                    PLAYER2.vel = 5
     
                if medium_button.rect.collidepoint(mouse_pos):
                    BALL.x_vel = 7
                    BALL.y_vel = 7
                    PLAYER1.vel = 7
                    PLAYER2.vel = 7

                if fast_button.rect.collidepoint(mouse_pos):
                    BALL.x_vel = 10
                    BALL.y_vel = 10
                    PLAYER1.vel = 10
                    PLAYER2.vel = 10

                if slider_circle.rect.collidepoint(mouse_pos):
                    slider_circle.held = True


            if event.type == pygame.MOUSEBUTTONUP:
                if slider_circle.held:
                    slider_circle.held = False


        welcome_msg = TEXT_FONT.render("Welcome to Pong!", True, (255, 255, 255))
        ball_speed = MENU_FONT.render("Game Speed", True, (255, 255, 255))
        ball_speed_rect = ball_speed.get_rect(center=(WIDTH/2, HEIGHT / 2 + 50))

        for sprite in sprites:
            sprite.draw()

        SCREEN.blit(welcome_msg, ((WIDTH / 2) - 130, 100))
        SCREEN.blit(ball_speed, ball_speed_rect)
        SCREEN.blit(PLAYER2.surf, PLAYER1.rect)
        
        slider_circle.move()

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

class Button(pygame.sprite.Sprite):
    """
    The button class (Will handle default buttons)
    """

    def __init__(self, text, loc, size=(150, 50), bg=(255, 255, 255), hc=(0,0,0), tc=(255, 255, 255), font=TEXT_FONT):
        super().__init__()

        # other attributes
        self.size = size
        self.bg = bg
        self.color = bg
        self.hover_color = hc

        # surface
        self.surf = pygame.surface.Surface(size)
        self.rect = self.surf.get_rect(center=loc)

        # button text
        self.text = text
        self.font = font
        self.text_surf = self.font.render(self.text, True, tc)
        self.text_rect = self.text_surf.get_rect(center = [s//2 for s in self.size])

    def draw(self):
        """ Handles drawing the button """
        self.mouseover()

        self.surf.fill(self.bg)
        self.surf.blit(self.text_surf, self.text_rect)
        SCREEN.blit(self.surf, self.rect)

    def mouseover(self):
        """ Handles mouse hovering over button """
        self.bg = self.color

        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.bg = self.hover_color

class SliderSlit(pygame.sprite.Sprite):
    """ The slits in the slider """
    def __init__(self, loc):
        super().__init__()
        self.surface = pygame.surface.Surface((5, 15))
        self.surface.fill((0, 0, 0))
        self.rect = self.surface.get_rect(center=loc)

class Slider(pygame.sprite.Sprite):
    """
    The slider class
    """
    def __init__(self, loc=(WIDTH / 2, HEIGHT / 2 - 50)):
        super().__init__()
        self.surface = pygame.surface.Surface((300, 15))
        self.surface.fill((255, 255, 255))
        self.rect = self.surface.get_rect(center = loc)
        self.height = loc[1]
        self.slits = self.create_slits()
        self.values = self.create_values()
        self.font = MENU_FONT

        self.title_surf = self.font.render("Choose Paddle Length", True, (255, 255, 255))
        self.title_rect = self.title_surf.get_rect(center=(WIDTH / 2, self.height - 30))

    def draw(self):
        SCREEN.blit(self.title_surf, self.title_rect)
        SCREEN.blit(self.surface, self.rect)
        for slit in self.slits:
            SCREEN.blit(slit.surface, slit.rect)

        for value in self.values:
            SCREEN.blit(value[0], value[1])

    def create_slits(self):
        slits = []
        for i in range(3):
            location = (100 * i) + (WIDTH / 4)
            slit = SliderSlit((location, self.height))
            slits.append(slit)

        return slits

    def create_values(self):
        values = []
        font = pygame.font.SysFont('Trebuchet MS', 20)

        smallest = font.render("Smallest", True, (255, 255, 255))
        small = font.render("Small", True, (255, 255, 255))
        big = font.render("Big", True, (255, 255, 255))
        biggest = font.render("Biggest", True, (255, 255, 255))

        start = self.rect.left
        height = 25
        smallest_rect = smallest.get_rect(center=(start, self.height + height))
        small_rect = smallest.get_rect(center=(start + 120, self.height + height))
        big_rect = smallest.get_rect(center=(start + 220, self.height + height))
        biggest_rect = smallest.get_rect(center=(start + 300, self.height + height))

        values.append([smallest, smallest_rect])
        values.append([small, small_rect])
        values.append([big, big_rect])
        values.append([biggest, biggest_rect])

        return values

class SliderCircle(pygame.sprite.Sprite):
    def __init__(self, height):
        super().__init__()
        self.held = False
        self.rect = None
        self.center = ((WIDTH / 4), height)
        self.val = 0

    def move(self):
        if self.held:
            start = int(WIDTH / 4)
            acceptable_x = [i for i in range(start, start + 400, 100)]
            mouse_pos = pygame.mouse.get_pos()
            for i in range (-5, 6):
                if mouse_pos[0] + i in acceptable_x:
                    self.center = (mouse_pos[0] + i, self.center[1])
                    self.val = acceptable_x.index(mouse_pos[0] + i)
                    PLAYER1.change_length(200 + 50 * self.val)
                    PLAYER2.change_length(200 + 50 * self.val)

    def draw(self):
        self.rect = pygame.draw.circle(SCREEN, (0, 0, 255), self.center, 15, 20)
        

def main():
    """ Main loop. """
    setup()
    start_screen()
    game_loop()

if __name__ == "__main__":
    main()
