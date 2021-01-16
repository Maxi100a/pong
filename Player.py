#pylint: disable=invalid-name
"""
Required modules:
    pygame
"""
import pygame
from Utilities import HEIGHT

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
        self.x = pos[0]
        self.surf = pygame.Surface((40, 200))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(center = (pos[0], pos[1]))
        self.num = num
        self.dir = 1
        self.vel = 5

    def move(self):
        """Handling player movement"""
        pressed_keys = pygame.key.get_pressed()

        top = self.rect.top
        bottom = self.rect.bottom

        if self.num == 1:
            if pressed_keys[pygame.K_RIGHT]:
                if top > 0:
                    self.rect.move_ip(0, -1 * self.vel)
                    self.dir = -1
            elif pressed_keys[pygame.K_LEFT]:
                if bottom < HEIGHT:
                    self.rect.move_ip(0, self.vel)
                    self.dir = 1
            else:
                self.dir = 0

        elif self.num == 2:
            if pressed_keys[pygame.K_a]:
                if top > 0:
                    self.rect.move_ip(0, -1 * self.vel)
                    self.dir = -1
            elif pressed_keys[pygame.K_d]:
                if bottom < HEIGHT:
                    self.rect.move_ip(0, self.vel)
                    self.dir = 1
            else:
                self.dir = 0

    def change_length(self, length):
        """ Change the height of the player """
        width = self.surf.get_width()
        self.surf = pygame.Surface((width, length))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(center = (self.x, HEIGHT/2))

    def reset(self, pos):
        self.surf = pygame.Surface((40, 200))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(center = (pos[0], pos[1]))
