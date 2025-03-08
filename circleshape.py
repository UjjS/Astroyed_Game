import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self,x,y,radius):
        # Initialize the sprite, checking if it has containers (for sprite groups)
        if hasattr(self,"containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        # Set initial position as a Vector2 at (x,y)
        self.position=pygame.Vector2(x,y)
        # Initialize velocity as a Vector2 starting at (0,0)
        self.velocity=pygame.Vector2(0,0)
        # Set the radius of the circle shape
        self.radius=radius
    
    def draw(self,screen):
        # Placeholder method for drawing the shape (to be implemented by subclasses)
        pass
    
    def update(self,dt):
        # Placeholder method for updating the shape's state (to be implemented by subclasses)
        # dt represents the time delta since last update
        pass
    def detect_collision(self, other):
        return self.position.distance_to(other.position) <= self.radius + other.radius