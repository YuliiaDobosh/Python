import pandas as pd

class Loader:
    def __init__(self, file_path):
        """Initialize the Loader.

        Args:
            file_path (str): The file path for loading the CSV data.
        """
        self.file_path = file_path

    def load_csv(self):
        """Load CSV data from the specified file path using pandas.

        Returns:
            pandas.DataFrame: The loaded DataFrame.
        """
        return pd.read_csv(self.file_path)
