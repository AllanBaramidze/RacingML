from operator import contains

import arcade
import math
from car import Car

WHITE_CUTOFF = 200
START_X, START_Y = 650, 185
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
        self.background = arcade.load_texture("Track.png")
        self.car = Car(770, 182)
        self.target_x = self.car.x
        self.target_y = self.car.y
        self.pixel_color = (0, 0, 0, 0)
        self.seconds_alive = 0
        arcade.schedule(self.tick, 0.01)
        self.timer_text = arcade.Text("", 10, WINDOW_HEIGHT - 30, arcade.color.BLACK, 16)
        self.color_text = arcade.Text("", 10, WINDOW_HEIGHT - 50, arcade.color.BLACK, 16)
        self.coords_text = arcade.Text("", 10, WINDOW_HEIGHT - 70, arcade.color.BLACK, 16)

    def tick(self, delta_time):
        self.seconds_alive += delta_time
        # print(self.seconds_alive)

    def is_white(self, color):  # NEW
        return color[0] > WHITE_CUTOFF

    def touching_white(self):
        r = self.car.radius + 2  # outer edge = the white ring
        for i in range(EDGE_POINTS):
            a = 2 * math.pi * i / EDGE_POINTS  # angle of this point
            x = self.car.x + r * math.cos(a)  # point on the circle
            y = self.car.y + r * math.sin(a)
            if self.is_white(self.get_pixel_color(x, y)):
                return True
        return False

    def reset(self):
        self.car.x = START_X
        self.car.y = START_Y
        self.target_x = START_X  # or it drives off again
        self.target_y = START_Y
        self.seconds_alive = 0

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.target_x = x
        self.target_y = y


    def on_update(self, delta_time: float):
        self.car.move_toward(self.target_x, self.target_y, delta_time)
        self.pixel_color = self.get_pixel_color(self.car.x, self.car.y)
        if self.touching_white() == True: # Loop reset
            self.reset()
        else:
            pass



    def get_pixel_color(self, x, y):
        img_w = self.background.width
        img_h = self.background.height

        px = x / WINDOW_WIDTH * img_w
        py = img_h - y * img_h / WINDOW_HEIGHT

        px = max(0, min(img_w - 1, int(px)))
        py = max(0, min(img_h - 1, int(py)))
        return self.background.image.getpixel((px, py))


    def on_draw(self):
        # Arcade calls this every frame. Without it, nothing is drawn.
        self.clear()  # wipe the previous frame
        arcade.draw_texture_rect(
            self.background,
            arcade.LBWH(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT),
        )
        self.car.draw()
        self.timer_text.text = f"alive: {self.seconds_alive:.2f}s"
        self.timer_text.draw()
        self.color_text.text = f"color: {self.get_pixel_color(self.car.x, self.car.y)}"
        self.color_text.draw()
        self.coords_text.text = f"coords: x: {self.car.x}, y: {self.car.y}"
        self.coords_text.draw()






def main():
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
    window.show_view(GameView())
    arcade.run()

if __name__ == "__main__":
    main()