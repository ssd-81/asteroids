import pygame
from constants import * 
from player import Player

def main():
    pygame.init()
    time_tracker = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # not sure if the player should be initialized here or within game loop
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0, 0))
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()
        # time in seconds
        dt = time_tracker.tick(60)/1000 

if __name__ == "__main__":
    main()