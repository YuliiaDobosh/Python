"""
Calculator Module

This module contains the Calculator class, which is a subclass of Program.
"""

import logging
from share.program import Program

class Calculator(Program):
    """
    Calculator class for performing basic arithmetic operations.
    Inherits from the Program class.
    """

    def __init__(self):
        """
        Initializes the Calculator object.
        """
        super().__init__()
        self._result = 0
        self._num1 = 0
        self._num2 = 0
        self._operator = ''  # Initialize _operator in __init__
        logging.info("Calculator ініціалізовано")

    def input_numbers(self):
        """
        Takes user input for two numbers.
        """
        try:
            self._num1 = float(input("Введіть перше число: "))
            self._num2 = float(input("Введіть друге число: "))
            logging.info("Числа введено: %s, %s", self._num1, self._num2)
        except ValueError:
            logging.error("Неправильне введення чисел")
            print("Помилка: Введені дані мають бути числовими.")
            self.input_numbers()

    def input_operator(self):
        """
        Takes user input for the operator.
        """
        self._operator = input("Введіть операцію (+, -, *, /, ^, sq, %): ")
        if self._operator not in ['+', '-', '*', '/', '^', 'sq', '%']:
            logging.warning("Недійсний оператор введено")
            print("Помилка: Недійсна операція.")
            self.input_operator()
        else:
            logging.info("Оператор введено: %s", self._operator)

    def calculate(self):
        """
        Performs the calculation based on user input.
        """
        try:
            if self._operator == '+':
                self._result = self._num1 + self._num2
            # ... (rest of the if-elif conditions)
        except ZeroDivisionError as e:
            logging.error("Спроба ділення на нуль")
            raise ZeroDivisionError from e
        except Exception as e:
            logging.exception("Помилка під час обчислення: %s", e)

    def display_result(self):
        """
        Displays the result of the calculation.
        """
        print("Результат: %s", self._result)
        logging.info("Результат відображено: %s", self._result)

    def run(self):
        """
        Runs the Calculator program.
        """
        while True:
            self.input_numbers()
            self.input_operator()
            self.calculate()
            self.display_result()
            choice = input("Бажаєте продовжити (так/ні)? ")
            if choice.lower() != 'так':
                logging.info("Користувач завершив роботу калькулятора")
                break
