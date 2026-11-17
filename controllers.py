from dataclasses import dataclass
from typing import Any
import arcade


@dataclass
class Inputs:
    throttle: float = 0.0
    steering: float = 0
    braking:  float = 0

class KeyboardController:
    def __init__(self):
        self.pressed = set()

    def on_key_press(self, symbol: int):
        # if a key is pressed add it to the set of pressed
        self.pressed.add(symbol)

    def on_key_release(self, symbol: int):
        # if a key is released remove it from the set
        self.pressed.discard(symbol)

    def get_inputs(self) -> Inputs:

        # go forward
        throttle = 0
        if arcade.key.W in self.pressed:
            throttle = 1.0

        # brake
        braking = 0
        if arcade.key.S in self.pressed:
            braking = 1.0

        # Steer right
        steering = 0
        if arcade.key.D in self.pressed:
            steering = -1.0

        # Steer Left
        if arcade.key.A in self.pressed:
            steering = 1.0

        return Inputs(throttle=throttle, braking=braking, steering=steering)


