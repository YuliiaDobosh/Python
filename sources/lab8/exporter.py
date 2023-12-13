class Exporter:
    def export_plot(self, figure, filename):
        """Export a matplotlib figure to a file.

        Args:
            figure: The matplotlib figure to export.
            filename (str): The filename (including extension) for the exported file.
        """
        figure.savefig(filename)
