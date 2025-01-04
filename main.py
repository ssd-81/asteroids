import pygame
from constants import * 
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    time_tracker = pygame.time.Clock()
    dt = 0
    
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    # asteroid field is only updatable
    AsteroidField.containers = (updatable, )
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0, 0))
        for sprite in updatable:
            sprite.update(dt)

        # might require changes; keep eye on this
        for asteroid in asteroids:
            if(asteroid.is_colliding(player)):
                print("Game over!")
                exit() # not sure if this will work
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = time_tracker.tick(60)/1000 
    

if __name__ == "__main__":
    main()