import pygame
from comet import Comet


class CometFallEvent:

    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 5
        self.game = game
        self.fall_mode = False

        self.all_comets = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def reset_percent(self):
        self.percent = 0

    def update_bar(self, surface):

        # Add percentage to the bar
        self.add_percent()

        pygame.draw.rect(surface, (0, 0, 0), [
            0,  # X axis
            surface.get_height() - 20,  # Y axis
            surface.get_width(),  # Width of the window
            10  # Bar thickness
        ])

        pygame.draw.rect(surface, (206, 45, 10), [
            0,  # X axis
            surface.get_height() - 20,  # Y axis
            (surface.get_width() / 100) * self.percent,  # Width of the window
            10  # Bar thickness
        ])

    def is_full_loaded(self):
        return self.percent >= 100

    def meteor_fall(self):

        for i in range(1, 10):
            self.all_comets.add(Comet(self))

    def attempt_fall(self):

        # If the bar is fully loaded and all monsters are killed
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            self.meteor_fall()

            # Trigger the event
            self.fall_mode = True

