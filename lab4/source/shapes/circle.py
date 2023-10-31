from .shape import Shape
from ..graphic.graphic import Graphic
from math import sqrt

class Circle(Shape):
    def __init__(self, center_x: int, center_y: int, radius: int, color: str, symbol: str) -> None:
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        super().__init__(center_x - radius, center_y - radius, center_x + radius, center_y + radius, color, symbol)

    def display(self, graphic: Graphic):
        # Check each point in the bounding box of the circle
        for y in range(self.y1, self.y2 + 1):
            # Calculate the leftmost and rightmost x-coordinates for the current y-coordinate
            dx = int(sqrt(self.radius**2 - (y - self.center_y)**2))
            x_left = self.center_x - dx
            x_right = self.center_x + dx

            if self.color == "transparent":
                # Draw only the outline of the circle
                graphic.draw_point(x_left, y, self.color, self.symbol)
                graphic.draw_point(x_right, y, self.color, self.symbol)
            else:
                # Fill the circle with the specified symbol
                for x in range(x_left, x_right + 1):
                    graphic.draw_point(x, y, self.color, self.symbol)
