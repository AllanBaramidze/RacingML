import arcade
import math
from car import Car

WINDOW_WIDTH = 1400
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
        self.car = Car(345, 35)
        self.target_x = self.car.x
        self.target_y = self.car.y
        self.seconds_alive = 0
        arcade.schedule(self.tick, 0.01)
        self.timer_text = arcade.Text("", 10, WINDOW_HEIGHT - 30, arcade.color.BLACK, 16)
        self.color_text = arcade.Text("", 10, WINDOW_HEIGHT - 50, arcade.color.BLACK, 30)

    def tick(self, delta_time):
        self.seconds_alive += delta_time
        # print(self.seconds_alive)

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.target_x = x
        self.target_y = y

    def on_update(self, delta_time: float):
        self.car.move_toward(self.target_x, self.target_y, delta_time)
        # print(f'@: {self.car.x} | {self.car.y}, going to: {self.target_x} | {self.target_y}, time: {self.seconds_alive}')
        print (f'x:{self.get_coords_scaled_x(self.car.x)}, y:{self.get_coords_scaled_y(self.car.x)} | color: {self.get_pixel_color(self.get_coords_scaled_x(self.car.x), self.get_coords_scaled_y(self.car.y))}')


    def get_pixel_color(self, px: int, py: int):
        im = self.background.image
        return im.getpixel((px, py))

    def get_coords_scaled_x(self, x):
        img_w = self.background.width  # the loaded image's size
        win_w = WINDOW_WIDTH  # your constants at the top of main.py
        px = x / win_w * img_w

        return px

    def get_coords_scaled_y(self, y):
        img_h = self.background.height
        # y = img_h -
        win_h = WINDOW_HEIGHT
        py = y * img_h / win_h

        return py


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
        self.color_text.text = f"color: {self.get_pixel_color(self.get_coords_scaled_x(self.car.x), self.get_coords_scaled_y(self.car.y))}"
        self.color_text.draw()





def main():
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
    window.show_view(GameView())
    arcade.run()

if __name__ == "__main__":
    main()