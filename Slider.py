""" The module required to create a slider """
import pygame
from Utilities import HEIGHT, WIDTH, MENU_FONT


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

    def draw(self, SCREEN):
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