import pygame, sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shooting import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    #Creating groups for updating and drawing
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    #Creating instance of a player
    player1 = Player(x, y, PLAYER_RADIUS)

    #Creating groups for asteroids 
    asteroid_cluster = pygame.sprite.Group()
    Asteroid.containers = (asteroid_cluster, updatable, drawable)
    AsteroidField.containers = (updatable)

    new_asteroid_field = AsteroidField()

    #Creating a group for shots
    bullets = pygame.sprite.Group()
    Shot.containers = (bullets, updatable, drawable)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for sprite in updatable:
            sprite.update(dt)
            if isinstance(sprite, Player):
                for asteroid in updatable:
                    if isinstance(asteroid, Asteroid) and sprite.check_collision(asteroid):
                        print("Game over!")
                        sys.exit()
                    else:
                        continue
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        # Limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
    print(
        " Starting asteroids!\n",
        f"Screen width: {SCREEN_WIDTH}\n",
        f"Screen height: {SCREEN_HEIGHT}"
        )


if __name__ == "__main__":
    main()