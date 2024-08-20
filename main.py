import pygame

from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    player1 = Player(x, y, PLAYER_RADIUS)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    updatable.add(player1)
    drawable.add(player1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for sprite in updatable:
            sprite.update(dt)
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