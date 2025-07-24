import pygame
import sys
from player import *
from circleshape import *
from constants import * 
from asteroid import *
from asteroidfield import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Poopsteroids')
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updateables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    Player.containers = (updateables, drawables)
    Asteroid.containers = (asteroids, updateables, drawables)
    AsteroidField.containers = (updateables)
    Shot.containers = (shots, updateables, drawables)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updateables.update(dt)
        pygame.Surface.fill(screen,(0,0,0))
        for drawable in drawables:
            drawable.draw(screen)
        for asteroid in asteroids:
            if asteroid.collide(player):
                print("Game over!")
                pygame.quit()
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collide(shot):
                    asteroid.split()
                    shot.kill()
                    break
        pygame.display.flip()
        dt = clock.tick(60) / 1000
if __name__ == "__main__":
    main()
