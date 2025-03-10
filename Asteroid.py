from constants import *
import pygame
import random
from circleshape import *
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    def draw(self, screen):
            pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
    
    
    def update(self, dt):
        # We can use self.velocity directly since it's initialized in the parent class
        # and inherited by this class. No need to use super().velocity
        self.velocity = self.velocity
        # Update position by adding velocity * time delta
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius<=ASTEROID_MIN_RADIUS:
            return 
        random_angle=random.uniform(20,50)
        one =self.velocity.rotate(random_angle)
        two=self.velocity.rotate(-random_angle)
        new_radius=self.radius-ASTEROID_MIN_RADIUS
        ast=Asteroid(self.position.x,self.position.y,new_radius)
        ast.velocity = one * 1.2
        ast=Asteroid(self.position.x,self.position.y,new_radius)
        ast.velocity = two * 1.2
    
    
    