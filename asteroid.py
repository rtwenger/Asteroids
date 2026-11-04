from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
import pygame
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        direction = random.uniform(20, 50)
        angle_1 = self.velocity.rotate(direction)
        angle_2 = self.velocity.rotate(-direction)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        split_1 = Asteroid(self.position.x, self.position.y, new_radius)
        split_2 = Asteroid(self.position.x, self.position.y, new_radius)
        split_1.velocity = angle_1 * 1.2
        split_2.velocity = angle_2 * 1.2
