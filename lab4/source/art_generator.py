from .interfaces.input_handler import InputHandler
from .file_saver import FileSaver
from .graphic.graphic import Graphic
from .graphic.color import Color
from .interfaces.art_generator import ArtGenerate
from .shapes.circle import Circle
from .shapes.rectangle import Rectangle

class ArtGenerate(ArtGenerate):
    def __init__(self, input_handler: InputHandler, graphic: Graphic, file_saver: FileSaver) -> None:
        super().__init__(input_handler, graphic, file_saver)
        self.screens = []

    def generate_shape(self):
            shape_options = ['Rectangle', 'Circle', 'Exit']
            choice = self.input_handler.choose(shape_options)

            if choice == 'Rectangle':
                x1 = self.input_handler.get_number("Enter x1 for the rectangle: ")
                y1 = self.input_handler.get_number("Enter y1 for the rectangle: ")
                x2 = self.input_handler.get_number("Enter x2 for the rectangle: ")
                y2 = self.input_handler.get_number("Enter y2 for the rectangle: ")
                color = self.input_handler.choose(list(Color.COLORS.keys()))
                symbol = self.input_handler.write_answer("Enter the symbol for the rectangle: ")

                return Rectangle(x1, y1, x2, y2, color, symbol)

            elif choice == 'Circle':
                center_x = self.input_handler.get_number("Enter center x for the circle: ")
                center_y = self.input_handler.get_number("Enter center y for the circle: ")
                radius = self.input_handler.get_number("Enter radius for the circle: ")
                color = self.input_handler.choose(list(Color.COLORS.keys()))
                symbol = self.input_handler.write_answer("Enter the symbol for the circle: ")

                return Circle(center_x, center_y, radius, color, symbol)

            else:
                return None


    def generate_art(self):
        while True:
            shape = self.generate_shape()
            if shape:
                shape.load(self.graphic)
                self.graphic.render()
                self.screens.append(self.graphic.buffer)

            continue_prompt = "Would you like to generate another shape? (yes/no)"
            if not self.input_handler.yes_or_no(continue_prompt):
                break
        return self.graphic.buffer


    def start(self):
        while True:
            art = self.generate_art()
            
            save_art_prompt = "Would you like to save art? (yes/no)"
            if self.input_handler.yes_or_no(save_art_prompt):
                self.file_saver.save_to_file(art, "art.txt")

            continue_prompt = "Would you like to generate another art? (yes/no)"
            if not self.input_handler.yes_or_no(continue_prompt):
                break