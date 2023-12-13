from .analyzer import Analyzer
from .exporter import Exporter
from .loader import Loader
from .visualizer import Visualizer
from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem

class VisualizationApplication:
    def __init__(self, file_path):
        """Initialize the VisualizationApplication.

        Args:
            file_path (str): The file path for loading the CSV data.
        """
        self.loader = Loader(file_path)
        self.dataframe = self.loader.load_csv()
        self.analyzer = Analyzer(self.dataframe)
        self.visualizer = Visualizer(self.dataframe)
        self.exporter = Exporter()
        self.menu = ConsoleMenu("Data Visualization Application", "Choose an option:")

        # Append menu items for different visualization options
        self.menu.append_item(FunctionItem("Show table", self.show_table))
        self.menu.append_item(FunctionItem("Show extremes", self.show_extremes))
        self.menu.append_item(FunctionItem("Show plot", self.show_plot))
        self.menu.append_item(FunctionItem("Export", self.export))

    def show_table(self):
        """Display the data table."""
        print(self.dataframe)
        input()

    def show_extremes(self):
        """Show extremes (max and min values) for a selected column."""
        column = input("Enter the column name for plotting: ")
        max_values, min_values = self.analyzer.find_extremes(column)
        print(f"Max Values:\n{max_values}\n\nMin Values:\n{min_values}")
        input()

    def show_plot(self):
        """Show a plot with predefined features."""
        features_info = [
            ('sepal length', 'bar'),
            ('sepal width', 'hist'),
            ('petal length', 'plot'),
            ('petal width', 'scatter')
        ]
        self.visualizer.plot_features(features_info)

    def export(self):
        """Export the current plot to a specified filename."""
        figure = self.visualizer.get_figure()
        filename = input("Enter the filename for export: ")
        self.exporter.export_plot(figure, filename)

    def run(self):
        """Run the application and display the menu."""
        self.menu.show()
