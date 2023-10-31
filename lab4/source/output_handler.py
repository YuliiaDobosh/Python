from .interfaces.output_handler import OutputHandler

class OutputHandler(OutputHandler):
    def display(self, string: str):
        print(string, end='')