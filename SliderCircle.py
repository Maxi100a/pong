""" The class needed to create the circle on the slider """
import pygame
from Utilities import WIDTH

class SliderCircle(pygame.sprite.Sprite):
    def __init__(self, height):
        super().__init__()
        self.held = False
        self.rect = None
        self.center = ((WIDTH / 4), height)
        self.val = 0

    def move(self, PLAYER1, PLAYER2):
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

    def draw(self, SCREEN):
        self.rect = pygame.draw.circle(SCREEN, (0, 0, 255), self.center, 15, 20)
