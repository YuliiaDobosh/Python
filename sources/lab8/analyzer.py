class Analyzer:
    def __init__(self, dataframe):
        """Initialize the Analyzer object.

        Args:
            dataframe: The input DataFrame for analysis.
        """
        self.dataframe = dataframe

    def find_extremes(self, column):
        """Find the maximum and minimum values in a specified column.

        Args:
            column (str): The column for which extremes need to be found.

        Returns:
            tuple: A tuple containing the maximum and minimum values in the specified column.
        """
        return self.dataframe[column].max(), self.dataframe[column].min()
