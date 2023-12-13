"""
Main Module

This module contains the Runner class, which orchestrates the execution of various
labs using a menu system.
"""
import unittest
import json
import logging
import logging.config
from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem
from sources.lab1.calc import Calculator
from sources.lab2.color_calc import ColorCalculator
from sources.lab3.source.input_handler import InputHandler as Lab3InputHandler
from sources.lab3.source.file_saver import FileSaver as Lab3FileSaver
from sources.lab3.source.output_handler import OutputHandler as Lab3OutputHandler
from sources.lab3.source.ascii_art_generator import ASCIIArtGenerator as Lab3ASCIIArtGenerator
from sources.lab4.source.input_handler import InputHandler as Lab4InputHandler
from sources.lab4.source.graphic.graphic import Graphic as Lab4Graphic
from sources.lab4.source.file_saver import FileSaver as Lab4FileSaver
from sources.lab4.source.art_generator import ArtGenerate as Lab4ArtGenerate
from sources.lab5.source.file_saver import FileSaver as Lab5FileSaver
from sources.lab5.source.graphic.graphic import Graphic as Lab5Graphic
from sources.lab5.source.art_generator import ArtGenerate as Lab5ArtGenerate
from sources.lab6.tests_calculator import TestCalculatorMethods
from sources.lab7.api import API
from sources.lab8.app import VisualizationApplication

class Runner:
    """
    Runner class for orchestrating the execution of various labs using a menu system.
    """
    def __init__(self) -> None:
        """
        Initializes the Runner class with a menu.
        """
        self.menu = ConsoleMenu("Runner of labs")
        self.menu.append_item(FunctionItem("Simple Calculator", self.simple_calc))
        self.menu.append_item(FunctionItem("OOP Calculator", self.oop_calc))
        self.menu.append_item(FunctionItem("ASCII Art", self.ascii_art))
        self.menu.append_item(FunctionItem("2D ASCII Art (no libraries)", self.ascii_art_2d_no_lib))
        self.menu.append_item(FunctionItem("3D ASCII Arts", self.ascii_art_3d))
        self.menu.append_item(FunctionItem("Unit tests of calculator", self.unit_tests))
        self.menu.append_item(FunctionItem("API", self.api))
        self.menu.append_item(FunctionItem("CSV", self.csv_plot))

    def simple_calc(self):
        """
        Run the Simple Calculator lab.
        """
        calc = Calculator()
        calc.run()

    def oop_calc(self):
        """
        Run the OOP Calculator lab.
        """
        calculator = ColorCalculator()
        calculator.run()

    def ascii_art(self):
        """
        Run the ASCII Art lab.
        """
        input_handler = Lab3InputHandler()
        output_handler = Lab3OutputHandler()
        file_saver = Lab3FileSaver()
        art_generator = Lab3ASCIIArtGenerator(input_handler, output_handler, file_saver)
        art_generator.run()

    def ascii_art_2d_no_lib(self):
        """
        Run the 2D ASCII Art (no libraries) lab.
        """
        art_generator = Lab4ArtGenerate(Lab4InputHandler(), Lab4Graphic(), Lab4FileSaver())
        art_generator.start()

    def ascii_art_3d(self):
        """
        Run the 3D ASCII Arts lab.
        """
        art_generator = Lab5ArtGenerate(Lab5Graphic(), Lab5FileSaver())
        art_generator.start()

    def unit_tests(self):
        """
        Run the unit tests of the calculator.
        """
        suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculatorMethods)
        test_runner = unittest.TextTestRunner()  # Renamed to test_runner
        test_runner.run(suite)
        input()

    def api(self):
        """
        Run the API lab.
        """
        api = API()
        api.run()

    def csv_plot(self):
        """
        Run the CSV Plot lab.
        """
        path = "c:\\Users\\HP\\Downloads\\iris.csv"
        app = VisualizationApplication(path)
        app.run()

    def show(self):
        """
        Show the menu.
        """
        self.menu.show()


with open('config.json', 'r', encoding='utf-8') as config_file:
    config = json.load(config_file)

logging.config.dictConfig(config)

runner = Runner()
runner.show()
