import random
import pygame


class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.max_health = 100
        self.health = random.randint(10, self.max_health)
        self.image = pygame.image.load("assets/mummy.png")
        self.attack = random.uniform(0.1, 0.3)
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540
        self.velocity = random.uniform(0.5, 2)

    def damage(self, amount):
        # Inflict damage to the monster
        self.health -= amount

        # Check if the health is <= 0
        if self.health <= 0:
            # Respawn as a new monster to save memory
            self.rect.x = 1000 + random.randint(0, 300)
            self.health = random.randint(10, self.max_health)
            self.velocity = random.uniform(0.5, 2)

    def update_health_bar(self, surface):

        # Draw the health bar's background and the health bar
        pygame.draw.rect(surface, (59, 55, 55), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (22, 203, 24), [self.rect.x + 10, self.rect.y - 20, self.health, 5])

    def move(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        else:
            self.game.player.damage(self.attack)
