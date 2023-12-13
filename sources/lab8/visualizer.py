import matplotlib.pyplot as plt

class Visualizer:
    def __init__(self, dataframe):
        self.dataframe = dataframe
        self.last_figure = None

    def plot_features(self, features_info, title='Multi-Feature Comparison'):
        num_plots = len(features_info)
        self.last_figure, axes = plt.subplots(1, num_plots, figsize=(5 * num_plots, 4))
        if num_plots == 1:  # Якщо лише один графік, axes не буде масивом
            axes = [axes]
        
        for ax, (column, plot_type) in zip(axes, features_info):
            if plot_type == 'bar':
                ax.bar(self.dataframe.index, self.dataframe[column])
            elif plot_type == 'hist':
                ax.hist(self.dataframe[column])
            elif plot_type == 'plot':
                ax.plot(self.dataframe[column])
            elif plot_type == 'scatter':
                # Для scatter plot потрібно дві величини; припустимо, що ми використовуємо дві послідовні колонки
                next_col_index = self.dataframe.columns.get_loc(column) + 1
                next_col_name = self.dataframe.columns[next_col_index % len(self.dataframe.columns)]
                ax.scatter(self.dataframe[column], self.dataframe[next_col_name])
            
            ax.set_title(f'{plot_type.capitalize()} of {column}')
            ax.set_xlabel(column)
            ax.set_ylabel('Count')
        
        plt.tight_layout()
        plt.show()


    def plot_basic(self, column):
        self.last_figure, ax = plt.subplots()
        a = self.dataframe[column]
        ax.plot(a)
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

    def get_figure(self):
        return self.last_figure

    def save_figure(self, filename):
        if self.last_figure:
            self.last_figure.savefig(filename)