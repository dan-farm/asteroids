from circleshape import CircleShape
import pygame
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, width=2)

    def update(self, dt):
        CircleShape.update(self, dt)
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if  self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            for new_asteroid in (new_asteroid1, new_asteroid2):
                for container in self.containers:
                    new_asteroid.add(container)
            new_asteroid1.velocity = self.velocity.rotate(random_angle) * 1.2
            new_asteroid2.velocity = self.velocity.rotate(-random_angle) * 1.2
            return new_asteroid1, new_asteroid2