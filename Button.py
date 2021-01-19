""" The button class. It's used to create different buttons. """

import pygame
from Utilities import TEXT_FONT

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

    def draw(self, SCREEN):
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
