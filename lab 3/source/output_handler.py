from .interfaces import output_handler
class OutputHandler(output_handler.OutputHandler):
    def display(self, art_text):
        print (art_text)