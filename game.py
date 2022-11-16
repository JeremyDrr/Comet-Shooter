import pygame
from player import Player
from monster import Monster, Mummy, Alien
from comet_event import CometFallEvent
from sounds import SoundManager


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
        # Set score to 0
        self.score = 0
        # Handle event manager
        self.comet_event = CometFallEvent(self)
        self.font = pygame.font.Font("assets/Kanit-Regular.ttf", 25)
        self.sound_manager = SoundManager()

    def start(self):
        self.is_playing = True

        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)

    def game_over(self):
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing = False
        self.score = 0
        self.sound_manager.play('game_over')

    def add_score(self, points=1):
        self.score += points

    def update(self, window):
        # Apply the player image
        window.blit(self.player.image, self.player.rect)

        # Display score on screen

        score_text = self.font.render(f"Score: {self.score}", True, (0, 0, 0))
        window.blit(score_text, (20, 20))

        # Get all already thrown projectiles
        for projectile in self.player.all_projectiles:
            projectile.move()

        # Update the player's health bar
        self.player.update_health_bar(window)
        self.player.update_animation()

        # Reload the event bar
        self.comet_event.update_bar(window)

        # Update the monsters
        for monster in self.all_monsters:
            monster.move()
            monster.update_health_bar(window)
            monster.update_animation()

        # Update the comets
        for comet in self.comet_event.all_comets:
            comet.fall()

        # Apply all the images from the projectile group
        self.player.all_projectiles.draw(window)

        # Apply all the images from the monster group
        self.all_monsters.draw(window)

        # Apply all the images from the comet group
        self.comet_event.all_comets.draw(window)

        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < window.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self, monster_class):
        self.all_monsters.add(monster_class.__call__(self))
