import pygame

class SoundManager:

    def __init__(self):
        self.sounds = {
            'click': pygame.mixer.Sound("assets/sounds/click.ogg"),
            'game_over': pygame.mixer.Sound("assets/sounds/game_over.ogg"),
            'meteor': pygame.mixer.Sound("assets/sounds/meteor.ogg"),
            'shoot': pygame.mixer.Sound("assets/sounds/shoot.ogg"),
        }

    def play(self, name):
        self.sounds[name].play()