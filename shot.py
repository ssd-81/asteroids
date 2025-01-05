import pygame
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        # self.velocity = pygame.Vector2(0, 0)
    
    # not very certain if this should be here or not
    def draw(self, screen):
        # where to use the constants.SHOT_RADIUS
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius,2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    