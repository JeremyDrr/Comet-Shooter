import pygame


# This class represents the projectile thrown by the player
class Projectile(pygame.sprite.Sprite):

    # Constructor
    def __init__(self, player):
        super().__init__()
        self.velocity = 2
        self.player = player
        self.image = pygame.image.load("assets/projectile.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0

    def rorate(self):
        self.angle += 3
        self.image = pygame.transform.rotate(self.origin_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rorate()

        # Check if the projectile is colliding with a monster
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            # Remove the projectile
            self.remove()
            monster.damage(self.player.attack)

        # Check if the projectile is offscreen
        if self.rect.x > 1080:
            # Delete the projectile
            self.remove()
