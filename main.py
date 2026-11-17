from operator import contains

import arcade
import math
from car import Car
from track import Track
from controllers import KeyboardController

WHITE_CUTOFF = 200
START_X, START_Y = 770, 182
LINE = 1
EDGE_POINTS = 8
WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 800
WINDOW_TITLE = "Starting Template"


class GameView(arcade.View):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self):
        super().__init__()
        self.track = Track(WINDOW_WIDTH, WINDOW_HEIGHT, "Track.png", WHITE_CUTOFF, EDGE_POINTS)
        self.car = Car(START_X, START_Y)
        self.controller = KeyboardController()
        self.pixel_color = (0, 0, 0, 0)
        self.seconds_alive = 0
        arcade.schedule(self.tick, 0.01)
        self.timer_text = arcade.Text("", 10, WINDOW_HEIGHT - 30, arcade.color.BLACK, 16)
        self.color_text = arcade.Text("", 10, WINDOW_HEIGHT - 50, arcade.color.BLACK, 16)
        self.coords_text = arcade.Text("", 10, WINDOW_HEIGHT - 70, arcade.color.BLACK, 16)
        self.speed_text = arcade.Text("", 10, WINDOW_HEIGHT - 90, arcade.color.BLACK, 16)
        self.tyre_health = arcade.Text("", 10, WINDOW_HEIGHT - 110, arcade.color.BLACK, 16)

    def tick(self, delta_time):
        self.seconds_alive += delta_time
        # print(self.seconds_alive)


    def reset(self):
        self.car.reset(START_X, START_Y)
        self.seconds_alive = 0

    def on_key_press(self, symbol: int, modifiers: int):
        self.controller.on_key_press(symbol)

    def on_key_release(self, symbol: int, modifiers: int):
        self.controller.on_key_release(symbol)

    def on_update(self, delta_time: float):
        inputs = self.controller.get_inputs()
        self.car.update(inputs, delta_time)
        if self.track.touching_white(self.car.x, self.car.y, self.car.radius):
            self.reset()


    def on_draw(self):
        self.clear()
        self.track.on_draw()
        self.car.draw()
        self.timer_text.text = f"alive: {self.seconds_alive:.2f}s"
        self.timer_text.draw()
        self.color_text.text = f"color: {self.track.get_pixel_on_image(self.car.x, self.car.y)}"
        self.color_text.draw()
        self.coords_text.text = f"coords: x: {self.car.x}, y: {self.car.y}"
        self.coords_text.draw()
        self.speed_text.text = f"speed: {self.car.speed}"
        self.speed_text.draw()
        self.tyre_health.text = f"tyre: {self.car.tyre.health:.0f}"
        self.tyre_health.draw()






def main():
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
    window.show_view(GameView())
    arcade.run()

if __name__ == "__main__":
    main()