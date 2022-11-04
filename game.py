import pygame
from player import Player
from monster import Monster


# This class represents the game
class Game:

    def __init__(self):
        self.is_playing = False
        # Generate the player when a new game is created
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # Group of monster
        self.all_monsters = pygame.sprite.Group()
        # Dictionary of pressed keys
        self.pressed = {}

        self.spawn_monster()
        self.spawn_monster()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)
