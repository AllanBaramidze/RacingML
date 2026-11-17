import math

import arcade


class Track:
    def __init__(self, window_width, window_height, img_path, white_cutoff, edge_points):
        self.window_width = window_width
        self.window_height = window_height
        self.img_path = img_path
        self.white_cutoff = white_cutoff
        self.edge_points = edge_points
        self.background = arcade.load_texture(img_path)

    def get_pixel_on_image(self, x, y):
        img_w = self.background.width
        img_h = self.background.height

        px = x / self.window_width * img_w
        py = img_h - y * img_h / self.window_height

        px = max(0, min(img_w - 1, int(px)))
        py = max(0, min(img_h - 1, int(py)))
        return self.background.image.getpixel((px, py))

    def touching_white(self, x, y, radius) -> bool:
        for i in range(self.edge_points):
            a = 2 * math.pi * i / self.edge_points  # angle of this point
            x_target = x + radius * math.cos(a)  # point on the circle
            y_target = y + radius * math.sin(a)
            if self.is_white(self.get_pixel_on_image(x_target, y_target)):
                return True
        return False

    def is_white(self, color: object) -> bool:  # NEW
        if not isinstance(color, tuple):
            return False
        return color[0] > self.white_cutoff

    def on_draw(self):
        # Arcade calls this every frame. Without it, nothing is drawn.
        arcade.draw_texture_rect(
            self.background,
            arcade.LBWH(0, 0, self.window_width, self.window_height),
        )