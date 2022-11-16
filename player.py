import pygame
from projectile import Projectile
import animation


# This class represents the player
class Player(animation.AnimateSprite):

    # Constructor
    def __init__(self, game):
        super().__init__('player')
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 3
        self.all_projectiles = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def damage(self, amount):

        if self.health-amount > amount:
            self.health -= amount
        else:
            self.game.game_over()

    def update_animation(self):
        self.animate()

    def update_health_bar(self, surface):

        # Draw the health bar's background and the health bar
        pygame.draw.rect(surface, (59, 55, 55), [self.rect.x + 50, self.rect.y + 20, self.max_health, 7])
        pygame.draw.rect(surface, (22, 203, 24), [self.rect.x + 50, self.rect.y + 20, self.health, 7])

    def throw_projectile(self):
        # Create a new instance of the Projectile class
        self.all_projectiles.add(Projectile(self))
        self.start_animation()
        self.game.sound_manager.play('shoot')

    # Method to move the character to the right
    def move_right(self):
        # If the player is not colliding with a monster entity
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    # Method to move the character to the left
    def move_left(self):
        self.rect.x -= self.velocity
