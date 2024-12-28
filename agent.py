from player import Player

import pygame
import random


class AgentPlayer(Player):
    def __init__(self, x: int, y: int, momentum: str) -> None:
        super().__init__(x, y, momentum)

    @staticmethod
    def _is_space_free_and_valid(y, x, grid) -> bool:
        if x < 0 or x >= len(grid[0]):
            return False
        if y < 0 or y >= len(grid):
            return False

        if grid[y][x] != 0:
            return False

        return True

    def _get_free_space_by_direction(self, grid, direction) -> int:
        free_space = 0
        y, x = self.y, self.x
        dy, dx = 0, 0

        if direction == "up":
            dy = -1
        elif direction == "down":
            dy = 1
        elif direction == "left":
            dx = -1
        elif direction == "right":
            dx = 1

        while True:
            y += dy
            x += dx

            if self._is_space_free_and_valid(y, x, grid):
                free_space += 1
            else:
                return free_space

    def set_agent_momentum(self, grid) -> None:
        directions = ["up", "left", "down", "right"]
        # Check up viablility
        if not self._is_space_free_and_valid(self.y - 1, self.x, grid):
            directions.remove("up")
        # Check down viablility
        if not self._is_space_free_and_valid(self.y + 1, self.x, grid):
            directions.remove("down")
        # Check left viablility
        if not self._is_space_free_and_valid(self.y, self.x - 1, grid):
            directions.remove("left")
        # Check right viablility
        if not self._is_space_free_and_valid(self.y, self.x + 1, grid):
            directions.remove("right")

        direction_lengths = []
        for direction in directions:
            direction_lengths.append(
                (direction, self._get_free_space_by_direction(grid, direction))
            )

        direction_lengths.sort(reverse=True, key=lambda x: x[1])

        if len(direction_lengths) == 0:
            return

        self.momentum = direction_lengths[0][0]
