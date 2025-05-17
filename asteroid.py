from circleshape import CircleShape
import pygame

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
  
  def draw(self, screen):
    pygame.draw.circle(screen, "white", (self.x, self.y), self.radius)
  
  def update(self, dt):
    self.velocity *= dt