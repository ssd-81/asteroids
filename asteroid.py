from circleshape import CircleShape

class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        # might need some changes
        self.x = x 
        self.y = y 
        self.radius = radius
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), (self.x, self.y),self.radius, 2)
    
    def update(self, dt):
        self.x += self.velocity * dt
        # not sure if this is right for particle to move in straight line
        self.y += self.velocity * dt