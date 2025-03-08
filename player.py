# Import necessary classes and constants
from circleshape import *
from constants import *
from shot import *

class Player(CircleShape):
    def __init__(self,x,y):
        # Initialize the Player as a CircleShape with PLAYER_RADIUS from constants
        super().__init__(x,y,PLAYER_RADIUS)
        # Initialize rotation angle to 0 (facing upwards)
        self.rotation = 0
        self.timer=0
    
    def triangle(self):
        # Calculate forward direction vector based on current rotation
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        # Calculate right direction vector (90 degrees from forward) and scale it
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        
        # Calculate three points of the triangle:
        # a: Point at the front of the player (forward direction)
        a = self.position + forward * self.radius
        # b: Point at the back-left of the player
        b = self.position - forward * self.radius - right
        # c: Point at the back-right of the player
        c = self.position - forward * self.radius + right
        
        # Return the three points as a list to form a triangle
        return [a, b, c]
    def draw(self, screen):
        # Draw the player's triangle using the calculated points
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle())
    def rotate(self, dt):
        # Update the player's rotation based on turn speed and time delta
        self.rotation += PLAYER_TURN_SPEED * dt
    def update(self, dt):
    # Check for key presses to handle player movement
        keys = pygame.key.get_pressed()
        self.timer-=dt
        if keys[pygame.K_a]:
            # Rotate player counter-clockwise when 'A' key is pressed
            self.rotate(-dt)
        if keys[pygame.K_d]:
            # Rotate player clockwise when 'D' key is pressed
            self.rotate(dt)
        # Move forward when 'W' key is pressed
        if keys[pygame.K_w]:
            self.move(dt)
        # Move backward when 'S' key is pressed
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        
    def move(self,dt):
        # Calculate forward direction vector based on current rotation
        # This creates a vector pointing up (0,1) and rotates it by the player's current rotation angle
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        
        # Update player's position by moving in the forward direction
        # Multiply by PLAYER_SPEED (pixels/second) and dt (time since last frame in seconds)
        # This gives us the distance to move this frame while maintaining consistent speed
        self.position += forward * PLAYER_SPEED * dt
    def shoot(self):
        if self.timer >0:
            return
        self.timer=PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED


        
