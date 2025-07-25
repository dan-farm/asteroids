import pygame
from circleshape import *
from constants import *

class Player(CircleShape):
    def __init__(self, x, y,):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), width=2)
    def rotate(self, dt):
        self.rotation += dt * PLAYER_TURN_SPEED
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if self.timer > 0:
            self.timer -= dt
        if keys[pygame.K_a]:
            self.rotate(-dt * PLAYER_TURN_SPEED)
        if keys[pygame.K_d]:
            self.rotate(dt * PLAYER_TURN_SPEED)
        if keys[pygame.K_w]:
            self.move(dt, True)
        if keys[pygame.K_s]:
            self.move(dt, False)
        if keys[pygame.K_SPACE]:
            shot = self.shoot()
    def move(self, dt, forward):
        direction = 1 if forward else -1
        forward_vec = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward_vec * PLAYER_SPEED * dt * direction
    
    def shoot(self):
        if self.timer <= 0:
            shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.timer = PLAYER_SHOOT_COOLDOWN
            return shot
        else:
            return None