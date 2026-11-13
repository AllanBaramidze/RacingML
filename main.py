import arcade
import math
from car import Car

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
        self.car = Car(345, 35)
        self.target_x = self.car.x
        self.target_y = self.car.y

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.target_x = x
        self.target_y = y

    def on_update(self, delta_time: float):
        self.car.move_toward(self.target_x, self.target_y, delta_time)


    def on_draw(self):
        # Arcade calls this every frame. Without it, nothing is drawn.
        self.clear()  # wipe the previous frame
        arcade.draw_texture_rect(
            self.background,
            arcade.LBWH(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT),
        )
        self.car.draw()






def main():
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
    window.show_view(GameView())
    arcade.run()

if __name__ == "__main__":
    main()