import pygame
import sys
from constants import *
from player import Player
from Asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    # Initialize the pygame module
    pygame.init()
    # Create a clock object to control frame rate
    fps_clock = pygame.time.Clock()
    # Set desired frame rate to 60 FPS
    fps_rate = 60
    # Initialize delta time (time since last frame) to 0
    dt = 0
    
    # Create sprite groups for game objects
    # Group for objects that need updating each frame
    updatable = pygame.sprite.Group()
    # Group for objects that need to be drawn each frame
    drawable = pygame.sprite.Group()
    # Separate group for asteroids to handle collisions
    asteroids = pygame.sprite.Group()
    # Separate group for shots to handle collisions
    shots = pygame.sprite.Group()
    
    # Assign container groups to game object classes
    # Shots will be added to shots, updatable, and drawable groups
    Shot.containers = (shots, updatable, drawable)
    # Asteroids will be added to asteroids, updatable, and drawable groups
    Asteroid.containers = (asteroids, updatable, drawable)
    # AsteroidField will only be added to updatable group
    AsteroidField.containers = updatable
    # Create the asteroid field instance
    asteroid_field = AsteroidField()
    # Player will be added to updatable and drawable groups
    Player.containers = (updatable, drawable)
    
    # Set up the game window with specified dimensions
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Create player object at center of screen
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    
    # Main game loop
    running = True
    while running:
        # Handle events in the event queue
        for event in pygame.event.get():
            # Check for window close event
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen with navy blue background
        screen.fill((0, 0, 128))
    
        # Update all game objects in the updatable group
        updatable.update(dt)
        
        # Draw all objects in the drawable group
        for drawable_object in drawable:
            drawable_object.draw(screen)

        # Handle collisions
        for ast in asteroids:
            # Check for collision between player and asteroid
            if ast.detect_collision(player):
                print("Game Over!")
                pygame.quit()
                sys.exit("Try Again")
            # Check for collision between shots and asteroids
            for sht in shots:
                if ast.detect_collision(sht):
                    # Remove both shot and asteroid on collision
                    sht.kill()
                    ast.split()

        # Update the display
        pygame.display.flip()

        # Limit frame rate and calculate delta time
        dt = fps_clock.tick(fps_rate) / 1000

    # Clean up pygame and exit
    pygame.quit()
    # Print startup messages
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()