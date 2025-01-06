import pygame
import random
from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape


class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        # might need some changes
        super().__init__(x, y, radius)
        # self.radius = radius
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position,self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if(self.radius <= ASTEROID_MIN_RADIUS):
            return 
        new_angle = random.uniform(20, 50)
        bullet_one_velocity = self.velocity.rotate(new_angle)
        bullet_two_velocity = self.velocity.rotate(-new_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        sub_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        sub_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        sub_asteroid_1.velocity = bullet_one_velocity * 1.2
        sub_asteroid_2.velocity = bullet_two_velocity * 1.2
        