import pygame

class Sphere:
    def __init__(self, x, y, radius=20, color=(255, 50, 50), screen_width=400, screen_height=400):
        self.x = x
        self.y = radius
        self.radius = radius
        self.color = color
        self.direction = 1
        self.speed = 0
        self.gravity = 0.5
        self.bounce = 0.8
        self.ground_y = screen_height - self.radius

    def update(self):
        self.speed += self.gravity
        self.y += self.speed

        if self.y >= self.ground_y:
            self.y = self.ground_y
            self.speed = -self.speed * self.bounce
            if abs(self.speed) < 1:
                self.speed = 0

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)
