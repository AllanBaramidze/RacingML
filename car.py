import math
import random

import arcade

from controllers import Inputs
from tyre import Tyre


CAR_COLORS = [
    arcade.color.BLUE
]
TYRE_COLORS = [
    arcade.color.RED,
    arcade.color.YELLOW,
    arcade.color.GREEN,
]

class Car:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0
        self.color = random.choice(CAR_COLORS)
        self.radius = 10
        self.speed = 0
        self.base_max_speed = 300
        self.base_turn_speed = 180
        self.drag = 2
        self.tyre = Tyre()

    @property
    def max_speed(self) -> float:
        return self.base_max_speed * self.tyre.grip

    @property
    def turn_speed(self) -> float:
        return self.base_turn_speed * self.tyre.grip

    def reset(self, x, y):
        self.x, self.y = x, y
        self.speed = 0
        self.angle = 0
        self.tyre.reset()



    def update(self, inputs: Inputs, delta_time):
        # throttle: add speed
        self.speed += self.tyre.acceleration * inputs.throttle * delta_time

        # braking: reduce speed
        self.speed -= self.tyre.brake_power * inputs.braking * delta_time

        # coast: no throttle, no braking
        if inputs.throttle == 0 and inputs.braking == 0:
            self.speed -= self.drag * delta_time

        # speed cap min, max
        self.speed = max(0, min(self.max_speed, self.speed))
        self.tyre.wear(self.speed / self.base_max_speed, inputs.braking, inputs.steering, delta_time)


        if self.speed > 0:
            self.angle += self.turn_speed * inputs.steering * delta_time

        distance = self.speed * delta_time
        rad = math.radians(self.angle)
        self.x += math.cos(rad) * distance
        self.y += math.sin(rad) * distance






    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.radius + 2, self.tyre.color)  # Outer # Outer
        arcade.draw_circle_filled(self.x, self.y, self.radius, self.color) # Inner

        rad = math.radians(self.angle)
        side = math.radians(self.angle + 90)

        base_x = self.x + math.cos(rad) * (self.radius + 1)
        base_y = self.y + math.sin(rad) * (self.radius + 1)

        tip_x = self.x + math.cos(rad) * (self.radius + 8)
        tip_y = self.y + math.sin(rad) * (self.radius + 8)

        left_x = base_x + math.cos(side) * 5
        left_y = base_y + math.sin(side) * 5

        right_x = base_x - math.cos(side) * 5
        right_y = base_y - math.sin(side) * 5

        arcade.draw_triangle_filled(tip_x, tip_y, left_x, left_y, right_x, right_y, arcade.color.BLUE)
