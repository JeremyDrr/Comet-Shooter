import pygame
from game import Game
pygame.init()

# Handle the game window
pygame.display.set_caption("Comet Shooter")
window = pygame.display.set_mode((1080, 720))

# Import the background image
background = pygame.image.load("assets/bg.jpg")

# Load the game
game = Game()

running = True

while running:

    # Apply the background
    window.blit(background, (0, -200))

    # Apply the player image
    window.blit(game.player.image, game.player.rect)

    # Get all already thrown projectiles
    for projectile in game.player.all_projectiles:
        projectile.move()

    # Update the player's health bar
    game.player.update_health_bar(window)

    # Update the monsters
    for monster in game.all_monsters:
        monster.move()
        monster.update_health_bar(window)

    # Apply all the images from the projectile group
    game.player.all_projectiles.draw(window)

    # Apply all the images from the monster group
    game.all_monsters.draw(window)

    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < window.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

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
                game.player.throw_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

