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
    fps_clock = pygame.time.Clock()
    fps_rate = 60
    dt = 0
    # Create two sprite groups: one for objects that need updating, one for objects that need drawing
    updatable = pygame.sprite.Group()  # Group to hold all game objects that need updating each frame
    drawable = pygame.sprite.Group()   # Group to hold all game objects that need to be drawn each frame
    asteroids = pygame.sprite.Group()
    shots=pygame.sprite.Group()
    # Assign containers for the classes
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    # Create instance of AsteroidField
    asteroid_field = AsteroidField()
    Player.containers = (updatable, drawable)
    
    
    
    # Set the display mode for the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Create a player object at the center of the screen
    player=Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)  # Automatically added to updatable and drawable groups
    
    # Main game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen with navy blue background
        screen.fill((0, 0, 128))
    
        # Update all game objects
        updatable.update(dt)
        
        # Loop through all drawable objects and draw them individually
        for drawable_object in drawable:
            drawable_object.draw(screen)
        
        # Check for collisions between player and asteroids
        for ast in asteroids:
            if ast.detect_collision(player):
                print("Game Over!")
                pygame.quit()
                sys.exit("Try Aagain")
        
        # Update the display
        pygame.display.flip()

        # Limit frame rate and calculate delta time
        dt = fps_clock.tick(fps_rate) / 1000

    # Clean up and quit
    pygame.quit()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()