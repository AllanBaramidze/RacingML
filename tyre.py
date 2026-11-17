from dataclasses import dataclass

import arcade


@dataclass(frozen=True)
class TyreBand:
    """One colour stage of tyre life. Each stat is (value at top of band, value at bottom)."""
    top: float
    bottom: float
    color: tuple
    acceleration: tuple[float, float]
    brake_power: tuple[float, float]
    grip: tuple[float, float]


class Tyre:
    MAX_HEALTH = 300

    BANDS = [
        TyreBand(300, 200, arcade.color.GREEN,  acceleration=(300, 200), brake_power=(150, 95), grip=(1.0, 0.85)),
        TyreBand(200, 50,  arcade.color.YELLOW, acceleration=(200, 100), brake_power=(95, 55), grip=(0.85, 0.6)),
        TyreBand(50,  0,   arcade.color.RED,    acceleration=(100, 0),   brake_power=(55, 0),  grip=(0.6, 0.3)),
    ]

    # Health lost per second at full speed
    WEAR_ROLLING = 2      # just driving
    WEAR_BRAKING = 8      # extra while braking
    WEAR_CORNERING = 6    # extra while steering

    def __init__(self):
        self.health = self.MAX_HEALTH

    def reset(self):
        self.health = self.MAX_HEALTH

    @property
    def band(self) -> TyreBand:
        for band in self.BANDS:
            if self.health >= band.bottom:
                return band
        return self.BANDS[-1]

    def _blend(self, stat: tuple[float, float]) -> float:
        """Slide smoothly from the band's start value to its end value."""
        band = self.band
        progress = (band.top - self.health) / (band.top - band.bottom)  # 0 at top → 1 at bottom
        start, end = stat
        return start + (end - start) * progress

    @property
    def color(self):
        return self.band.color

    @property
    def acceleration(self) -> float:
        return self._blend(self.band.acceleration)

    @property
    def brake_power(self) -> float:
        return self._blend(self.band.brake_power)

    @property
    def grip(self) -> float:
        return self._blend(self.band.grip)

    def wear(self, speed_ratio: float, braking: float, steering: float, delta_time: float):
        amount = (self.WEAR_ROLLING
                  + self.WEAR_BRAKING * braking
                  + self.WEAR_CORNERING * abs(steering)) * speed_ratio * delta_time
        self.health = max(0.0, self.health - amount)