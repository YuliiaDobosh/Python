import logging
from .file_saver import FileSaver
from .graphic.graphic import Graphic, Figure, Color
from .interfaces.art_generator import ArtGenerate
from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem
import curses
import curses.ascii
from .graphic.point_3d import Point3D
from .graphic.figure_factory import FigureFactory

class ArtGenerate(ArtGenerate):
    """Concrete implementation of the ArtGenerate abstract class.

    This class provides methods for generating and displaying 3D ASCII art.
    """

    def __init__(self, graphic: Graphic, file_saver: FileSaver) -> None:
        """Initialize the ArtGenerate object."""
        super().__init__(graphic, file_saver)
        self.menu = ConsoleMenu()

        self.menu.append_item(FunctionItem("Generate 3D Art", self.generate_art))
        self.menu.append_item(FunctionItem("Show 3D Arts", self.show_arts))

        self.arts: list[list[Figure]] = []

    def __generate_art(self, window) -> str:
        """Generate 3D ASCII art with user interaction."""
        logging.info("Початок генерації 3D арту")

        def get_user_input(stdscr, prompt_string, height=0):
            """Get user input from the console."""
            stdscr.addstr(height, 0, prompt_string)
            curses.echo()
            stdscr.refresh()
            input_str = stdscr.getstr(height, len(prompt_string))
            curses.noecho()
            return input_str.decode('utf-8')

        while True:
            window.clear()

            symbol = get_user_input(window, "Enter symbol: ", 0)
            prmt = f'Enter color({", ".join([c.name for c in Color])}): '
            c = get_user_input(window, prmt, 1).upper()
            color = Color[c]

            figure_type = get_user_input(window, "Enter figure type(Cube, Piramid, Sphere): ", 2).lower()
            figure_graphic = FigureFactory()
            if figure_type == "cube":
                fig = figure_graphic.create_cube(Point3D(0, 0, 0))
            elif figure_type == 'piramid':
                fig = figure_graphic.create_pyramid(Point3D(0, 0, 0))
            elif figure_type == 'sphere':
                radius = float(get_user_input(window, "Enter radius: ", 3))
                fig = figure_graphic.create_sphere(Point3D(0, 0, 0), radius)

            fig.set_symbol(symbol)
            fig.set_color(color)

            self.graphic.add_figure(fig)

            dx, dy, dz = 0, 0, 0

            self.graphic.set_window(window)

            while True:
                window.clear()

                self.graphic.last_figure.translate(dx, dy, dz)

                self.graphic.render_figures()

                window.addstr(0, 0, f"{self.graphic.last_figure.local_transform}")
                window.addstr(self.graphic.height - 5, 0, "x - a/d")
                window.addstr(self.graphic.height - 4, 0, "y - w/s")
                window.addstr(self.graphic.height - 3, 0, "z - q/e")
                window.addstr(self.graphic.height - 2, 0, "ESC - Finish")

                key = window.getch()

                if key == curses.ascii.ESC:
                    window.clear()
                    break
                elif key == ord('a'):
                    dy, dz, dx = 0, 0, -0.08
                elif key == ord('d'):
                    dy, dz, dx = 0, 0, 0.08
                elif key == ord('w'):
                    dx, dz, dy = 0, 0, -0.08
                elif key == ord('s'):
                    dx, dz, dy = 0, 0, 0.08
                elif key == ord('q'):
                    dx, dy, dz = 0, 0, -0.08
                elif key == ord('e'):
                    dx, dy, dz = 0, 0, 0.08

                window.refresh()

            window.clear()
            self.graphic.render_figures()

            window.addstr(self.graphic.height - 3, 0, "Enter - Add figure")
            window.addstr(self.graphic.height - 2, 0, "ESC - Finish")

            key = window.getch()
            if key == curses.ascii.ESC:
                self.arts.append([f.copy() for f in self.graphic.figures])
                self.graphic.figures.clear()
                break

        logging.info("3D арт сгенеровано")

    def generate_art(self):
        """Wrapper function to initiate the generation of 3D ASCII art."""
        curses.wrapper(self.__generate_art)

    def __show_arts(self, window):
        """Display saved 3D ASCII arts."""
        logging.info("Відображення збережених 3D артів")

        self.graphic.is_init = False
        self.graphic.set_window(window)

        while True:
            window.clear()

            index = 0
            self.graphic.figures = self.arts[index]
            self.graphic.render_figures()

            window.addstr(self.graphic.height - 3, 0, "a/d - Move")
            window.addstr(self.graphic.height - 2, 0, "ESC - Finish")
            window.refresh()

            key = window.getch()

            if key == curses.ascii.ESC:
                break
            elif key == ord('a'):
                index -= 1 if index == 0 else 0
            elif key == ord('d'):
                index += 1 if index < len(self.arts) - 1 else 0

        self.graphic.figures = []

        logging.info("Відображення завершено")

    def show_arts(self):
        """Wrapper function to initiate the display of saved 3D ASCII arts."""
        curses.wrapper(self.__show_arts)

    def start(self):
        """Start the ArtGenerate application."""
        logging.info("Старт ArtGenerate")
        self.menu.show()
        logging.info("ArtGenerate завершено")
