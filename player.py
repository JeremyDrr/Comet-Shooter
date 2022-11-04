import pygame
from projectile import Projectile


# This class represents the player
class Player(pygame.sprite.Sprite):

    # Constructor
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 1
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load("assets/player.png")
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def damage(self, amount):

        if self.health-amount > amount:
            self.health -= amount

    def update_health_bar(self, surface):

        # Draw the health bar's background and the health bar
        pygame.draw.rect(surface, (59, 55, 55), [self.rect.x + 50, self.rect.y + 20, self.max_health, 7])
        pygame.draw.rect(surface, (22, 203, 24), [self.rect.x + 50, self.rect.y + 20, self.health, 7])

    def throw_projectile(self):
        # Create a new instance of the Projectile class
        self.all_projectiles.add(Projectile(self))

    # Method to move the character to the right
    def move_right(self):
        # If the player is not colliding with a monster entity
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    # Method to move the character to the left
    def move_left(self):
        self.rect.x -= self.velocity
