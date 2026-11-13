import math
import random
import arcade

CAR_COLORS = [
    arcade.color.BLUE
]

class Car:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = random.choice(CAR_COLORS)
        self.radius = 6
        self.speed = 50

    def move_toward(self, target_x, target_y, delta_time):
        # How far is the target
        dx = target_x - self.x
        dy = target_y - self.y
        distance = math.hypot(dx, dy)

        # are we there?
        if distance < 1:
            return

        # how can we move this frame?
        step = self.speed * delta_time
        if step > distance:
            step = distance

        self.x += dx / distance * step
        self.y += dy / distance * step

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.radius + 2, arcade.color.WHITE)
        arcade.draw_circle_filled(self.x, self.y, self.radius, self.color)


