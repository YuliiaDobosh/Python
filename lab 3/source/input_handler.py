from .interfaces import input_handler
import pyfiglet

class InputHandler(input_handler.InputHandler):

    def get_text(self):
        return input("Enter the word or phrase for ASCII art: ")
    
    def select_font(self):
        fonts = pyfiglet.FigletFont.getFonts()
        for i, font in enumerate(fonts):
            print(f"{i + 1}. {font}")
        choice = self.get_number("Select a font by number: ")
        return fonts[choice - 1]

    def select_color(self):
        colors = ["red", "green", "yellow", "blue", "grey", "cyan", "white"]
        for i, color in enumerate(colors):
            print(f"{i + 1}. {color}")
        choice = self.get_number("Select a color by number: ")
        return colors[choice - 1]

    def yes_or_no(self, question):
        answer = input(f"{question} (yes/no): ").strip().lower()
        return answer == 'yes'

    def choose(self, options):
        for i, option in enumerate(options):
            print(f"{i + 1}. {option}")
        choice = self.get_number("Make a choice by number: ")
        return options[choice - 1]

    def write_answer(self, prompt):
        return input(prompt)

    def get_number(self, prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a number.")