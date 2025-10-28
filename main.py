import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    gamespeed = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    ship = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable,)
    field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        updatable.update(dt)
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

        for sprite in asteroids:
            if ship.collision(sprite):
                sys.exit("Game over!")
        dt = gamespeed.tick(60) / 1000

if __name__ == "__main__":
    main()
