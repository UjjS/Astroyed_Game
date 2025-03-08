# Asteroid Field Simulation

## Overview
This project is a 2D asteroid field simulation built using Pygame. It features:
- Randomly generated asteroids that spawn from screen edges
- Asteroid splitting mechanics when hit
- Basic collision detection
- Smooth movement and physics

## Requirements
- Python 3.7+
- Pygame 2.0+

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/asteroid-field.git
   cd asteroid-field
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the simulation:
   ```bash
   python main.py
   ```

## Controls
- Arrow Keys: Move player
- Space: Shoot
- ESC: Quit game
## Project Structure
The project is organized into several key files:

- `main.py`: Entry point that initializes and runs the game loop
- `constants.py`: Contains game configuration and constants
- `circleshape.py`: Base class for circular game objects
- `Asteroid.py`: Implements asteroid behavior and rendering
- `asteroidfield.py`: Manages asteroid spawning and field behavior
- `player.py`: Handles player controls and ship behavior
- `projectile.py`: Manages projectile movement and collisions

The core game objects inherit from `CircleShape` which provides basic physics and collision detection capabilities. The `AsteroidField` class manages the spawning and updating of asteroids, while the player and projectile classes handle user interaction and shooting mechanics.





