from player import Player

import pygame
import random


class AgentPlayer(Player):
    def __init__(self, x: int, y: int, momentum: str) -> None:
        super().__init__(x, y, momentum)

    def set_momentum(self, grid) -> None:
        directions = ["up", "left", "down", "right"]
        # Check up viablility
        if self.y == 0 or grid[self.y - 1][self.x] != 0:
            directions.remove("up")
        # Check down viablility
        if self.y >= len(grid) or grid[self.y + 1][self.x] != 0:
            directions.remove("down")
        # Check left viablility
        if self.x == 0 or grid[self.y][self.x - 1] != 0:
            directions.remove("left")
        # Check right viablility
        if self.x >= len(grid[0]) or grid[self.y][self.x + 1] != 0:
            directions.remove("right")

        if len(directions) == 0:
            return

        self.momentum = random.choice(directions)
