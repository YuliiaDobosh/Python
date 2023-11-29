from .analyzer import Analyzer
from .exporter import Exporter
from .loader import Loader
from .visualizer import Visualizer
from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem

class VisualizationApplication:
    def __init__(self, file_path):
        self.loader = Loader(file_path)
        self.dataframe = self.loader.load_csv()
        self.analyzer = Analyzer(self.dataframe)
        self.visualizer = Visualizer(self.dataframe)
        self.exporter = Exporter()
        self.menu = ConsoleMenu("Data Visualization Application", "Choose an option:")

        self.menu.append_item(FunctionItem("Show table", self.show_table))
        self.menu.append_item(FunctionItem("Show extremes", self.show_extremes))
        self.menu.append_item(FunctionItem("Show plot", self.show_plot))
        self.menu.append_item(FunctionItem("Export", self.export))

    def show_table(self):
        print(self.dataframe)
        input()

    def show_extremes(self):
        column = input("Enter the column name for plotting: ")
        max_values, min_values = self.analyzer.find_extremes(column)
        print(f"Max Values:\n{max_values}\n\nMin Values:\n{min_values}")
        input()

    def show_plot(self):
        column = input("Enter the column name for plotting: ")
        self.visualizer.plot_basic(column, f'graphic {column}/total count of iris', 'irises', column)

    def export(self):
        figure = self.visualizer.get_figure()  # Припускаючи, що у Visualizer є метод get_figure
        filename = input("Enter the filename for export: ")
        self.exporter.export_plot(figure, filename)

    def run(self):
        self.menu.show()

