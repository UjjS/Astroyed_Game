import pygame
from constants import *
def main():
    # Initialize the pygame module
    pygame.init()
    # Set the display mode for the game window
    screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return
        # Define the color navy blue
        navy_blue=(0,0,128)
        # Fill the screen with navy blue color
        screen.fill(navy_blue)
        # Update the display to show the changes
        pygame.display.flip()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__=="__main__":
    main()