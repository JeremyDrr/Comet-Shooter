import pygame
import math
from game import Game

pygame.init()

# Define clock
clock = pygame.time.Clock()
FPS = 90

# Handle the game window
pygame.display.set_caption("Comet Shooter")
window = pygame.display.set_mode((1080, 720))
icon = pygame.image.load("assets/comet.png")
icon = pygame.transform.scale(icon, (16, 16))
pygame.display.set_icon(icon)

# Import the background image
background = pygame.image.load("assets/bg.jpg")

# Import the banner
banner = pygame.image.load("assets/banner.png")
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(window.get_width() / 4)

# Load the playing button
play_button = pygame.image.load("assets/button.png")
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(window.get_width() / 3.33)
play_button_rect.y = math.ceil(window.get_height() / 2)

# Load the game
game = Game()

running = True

while running:

    # Apply the background
    window.blit(background, (0, -200))

    # Check if the game has started
    if game.is_playing:
        game.update(window)
    else:
        window.blit(play_button, play_button_rect)
        window.blit(banner, banner_rect)

    # Refresh the window
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # Detect if the player released a key
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # Detect if the spacebar is pressed to throw a projectile
            if event.key == pygame.K_SPACE:
                if game.is_playing:
                    game.player.throw_projectile()
                else:
                        game.start()
                        game.sound_manager.play('click')

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse is colliding the play button
            if play_button_rect.collidepoint(event.pos):
                # Change the state of the game
                game.start()
                game.sound_manager.play('click')

    clock.tick(FPS)
