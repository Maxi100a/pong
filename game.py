"""
sys - system
random - for random numbers
pygame - for GUI
"""
import sys
import random
import pygame


# Constants
HEIGHT = 600
WIDTH = 600
VEC = pygame.math.Vector2 # 2 for 2-D

def main():
    """ Main method."""
    p1_score = p2_score = 0
    # Initializing the module
    pygame.init()

    # Initialize important classes
    ball = Ball()
    player1 = Player((0, HEIGHT / 2), 1)
    player2 = Player((WIDTH, HEIGHT / 2), 2)

    score_font = pygame.font.SysFont('Comic Sans MS', 32)

    # Create a sprite group
    sprites = pygame.sprite.Group()
    sprites.add(ball)
    sprites.add(player1)
    sprites.add(player2)

    # Set the caption
    pygame.display.set_caption("Pong")

    # Creating the initial screen, and the time clock
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    fps = pygame.time.Clock()

    # Main loop
    while True:
        score = score_font.render(str(ball.p1_score) + ' : ' + \
            str(ball.p2_score), True, (255, 255, 255))

        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0,0,0))

        for entity in sprites:
            screen.blit(entity.surf, entity.rect)

        if ball.rect.colliderect(player1):
            ball.collide(player1)
        elif ball.rect.colliderect(player2):
            ball.collide(player2)

        screen.blit(score, ((WIDTH / 2) - score.get_rect().center[0], \
            HEIGHT - score.get_rect().bottom ))

        player1.move()
        player2.move()
        ball.move()

        pygame.display.update()
        fps.tick(60)

# pylint: disable=too-many-instance-attributes
class Ball(pygame.sprite.Sprite):
    """Class to keep track of the ball."""

    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((20, 20))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(center = (50, HEIGHT / 2))
        self.x_vel = self.y_vel = 3
        self.p1_score = self.p2_score = 0

    def move(self):
        """Handling the movement of the ball"""

        # Handling the bouncing off bottom or top
        if self.rect.bottom >= HEIGHT or self.rect.top <= 0:
            self.y_vel *= -1

        # Scoring
        if self.rect.left <= 0:
            self.rect = self.surf.get_rect(center=(random.randint(50, WIDTH - 50), \
                random.randint(0, HEIGHT)))
            self.x_vel *= -1
            self.p2_score += 1
            print(self.p2_score)
        elif self.rect.right >= WIDTH:
            self.rect = self.surf.get_rect(center=(random.randint(50, WIDTH - 50), \
                random.randint(0, HEIGHT)))
            self.p1_score += 1
            print(self.p1_score)

        self.rect.move_ip(self.x_vel, self.y_vel)

    def collide(self, player):
        """Handling collision with the player's platform"""
        self.x_vel *= -1
        self.y_vel = abs(self.y_vel) * player.dir


# pylint: disable=too-few-public-methods
class Player(pygame.sprite.Sprite):
    """The player class.
        Attributes
            surf - pygame
            rect - pygame
            num - player number
            dir - indicates the current direction
    """
    def __init__(self, pos, num):
        super().__init__()
        self.surf = pygame.Surface((40, 200))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(center = (pos[0], pos[1]))
        self.num = num
        self.dir = 1

    def move(self):
        """Handling player movement"""
        pressed_keys = pygame.key.get_pressed()

        top = self.rect.top
        bottom = self.rect.bottom

        if self.num == 1:
            if pressed_keys[pygame.K_LEFT]:
                if top != 0:
                    self.rect.move_ip(0, -5)
                    self.dir = -1
            elif pressed_keys[pygame.K_RIGHT]:
                if bottom != HEIGHT:
                    self.rect.move_ip(0, 5)
                    self.dir = 1
            else:
                self.dir = 0

        elif self.num == 2:
            if pressed_keys[pygame.K_d]:
                if top != 0:
                    self.rect.move_ip(0, -5)
                    self.dir = -1

            if pressed_keys[pygame.K_a]:
                if bottom != HEIGHT:
                    self.rect.move_ip(0, 5)
                    self.dir = 1     


if __name__ == "__main__":
    main()
