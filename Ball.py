# pylint: disable=too-many-instance-attributes
"""
Required imports
    Pygame
    Height (from Utilities)
    Width (from Utilities)
"""
import random
import pygame

from Utilities import HEIGHT, WIDTH

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
            self.rect = self.surf.get_rect(center=(self.rect.centerx + 20, \
                random.randint(0, HEIGHT)))
            self.x_vel *= -1
            self.p2_score += 1
        elif self.rect.right >= WIDTH:
            self.rect = self.surf.get_rect(center=(self.rect.centerx - 20, \
                random.randint(0, HEIGHT)))
            self.x_vel *= -1
            self.p1_score += 1

        self.rect.move_ip(self.x_vel, self.y_vel)

    def collide(self, player):
        """Handling collision with the player's platform"""
        self.x_vel *= -1
        self.y_vel = abs(self.y_vel) * player.dir if player.dir != 0 else self.y_vel
