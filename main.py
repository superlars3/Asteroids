import pygame
from constants import *
from player import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    gamespeed = pygame.time.Clock()
    dt = 0
    Ship = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        Ship.draw(screen)
        Ship.update(dt)
        pygame.display.flip()
        dt = gamespeed.tick(60) / 1000

if __name__ == "__main__":
    main()
