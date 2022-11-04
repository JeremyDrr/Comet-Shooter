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

    def start(self):
        self.is_playing = True

        self.spawn_monster()
        self.spawn_monster()

    def game_over(self):
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False

    def update(self, window):
        # Apply the player image
        window.blit(self.player.image, self.player.rect)

        # Get all already thrown projectiles
        for projectile in self.player.all_projectiles:
            projectile.move()

        # Update the player's health bar
        self.player.update_health_bar(window)

        # Update the monsters
        for monster in self.all_monsters:
            monster.move()
            monster.update_health_bar(window)

        # Apply all the images from the projectile group
        self.player.all_projectiles.draw(window)

        # Apply all the images from the monster group
        self.all_monsters.draw(window)

        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < window.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)
