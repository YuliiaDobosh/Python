from ..output_handler import OutputHandler
from .color import Color
from .cell import Cell
import os

class Graphic(OutputHandler):
    def __init__(self) -> None:
        super().__init__()
        c, l = os.get_terminal_size()
        self.width = c
        self.height = l
        self.buffer: list[list[Cell]] = [[Cell(' ') for _ in range(self.width)] for _ in range(self.height)]
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def draw_line(self, x1, y1, x2, y2, color = 'transparent', symbol="*"):
        # Implementing Bresenham's Line Algorithm
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1

        if dx > dy:
            err = dx / 2.0
            while x1 != x2:
                self.draw_point(x1, y1, color, symbol)
                err -= dy
                if err < 0:
                    y1 += sy
                    err += dx
                x1 += sx
        else:
            err = dy / 2.0
            while y1 != y2:
                self.draw_point(x1, y1, color, symbol)
                err -= dx
                if err < 0:
                    x1 += sx
                    err += dy
                y1 += sy

        self.draw_point(x2, y2, color, symbol)

    def draw_point(self, x, y, color = 'transparent', symbol="*"):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.buffer[y][x].color = color
            self.buffer[y][x].symbol = symbol

    def fill(self, x1, y1, x2, y2, color='transparent', symbol="*"):
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                self.draw_point(x, y, color, symbol)

    def render(self):
        for row in self.buffer:
            for cell in row:
                self.display(Color.colored(cell.symbol, cell.color))
            self.display('\n')

    def clear(self):
        os.system('cls')