import matplotlib.pyplot as plt

class Visualizer:
    def __init__(self, dataframe):
        self.dataframe = dataframe
        self.last_figure = None

    def plot_basic(self, column, title, xlabel, ylabel):
        if self.last_figure is not None:
            plt.close(self.last_figure)

        self.last_figure, ax = plt.subplots()
        ax.plot(self.dataframe[column])

        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)

        plt.show()

    def plot_bar(self, categories, values, title='Bar Chart', xlabel='Category', ylabel='Value'):
        self.last_figure, ax = plt.subplots()
        ax.bar(categories, values)
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_histogram(self, column, bins=10):
        self.last_figure, ax = plt.subplots()
        ax.hist(self.dataframe[column], bins=bins)
        plt.show()

    def plot_scatter(self, column_x, column_y):
        self.last_figure, ax = plt.subplots()
        ax.scatter(self.dataframe[column_x], self.dataframe[column_y])
        plt.show()

    def plot_count_by_category(self, category):
        counts = self.dataframe[category].value_counts()
        self.plot_bar(counts.index, counts.values, title='Кількість осіб за країною', xlabel='Країна', ylabel='Кількість осіб')

    def get_figure(self):
        return self.last_figure

    def save_figure(self, filename):
        if self.last_figure:
            self.last_figure.savefig(filename)
