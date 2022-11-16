import random
import pygame
import animation


class Monster(animation.AnimateSprite):

    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.game = game
        self.max_health = 100
        self.health = 100
        self.attack = random.uniform(0.1, 0.3)
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540 - offset
        self.start_animation()
        self.loot_amount = 1
        self.name = name

    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = random.uniform(1, self.default_speed)

    def set_loot_amount(self, amount):
        self.loot_amount = amount

    def damage(self, amount):
        # Inflict damage to the monster
        self.health -= amount

        # Check if the health is <= 0
        if self.health <= 0:
            # Respawn as a new monster to save memory
            self.rect.x = 1000 + random.randint(0, 300)
            if self.name == "alien":
                self.health = 250
            else:
                self.health = 100
            self.velocity = random.uniform(0.5, 2)
            self.game.add_score(self.loot_amount)

            # Check if the event bar is fully loaded
            if self.game.comet_event.is_full_loaded():
                # Remove the monster
                self.game.all_monsters.remove(self)
                # Try to trigger the comet fall
                self.game.comet_event.attempt_fall()

    def update_health_bar(self, surface):

        # Draw the health bar's background and the health bar
        pygame.draw.rect(surface, (59, 55, 55), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (22, 203, 24), [self.rect.x + 10, self.rect.y - 20, self.health, 5])

    def update_animation(self):
        self.animate(loop=True)

    def move(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        else:
            self.game.player.damage(self.attack)


class Mummy(Monster):
    def __init__(self, game):
        super().__init__(game, "mummy", (130, 130))
        self.set_speed(3)
        self.set_loot_amount(1)


class Alien(Monster):
    def __init__(self, game):
        super().__init__(game, "alien", (300, 300), 130)
        self.health = 250
        self.max_health = 250
        self.attack = 0.8
        self.set_speed(1)
        self.set_loot_amount(10)
