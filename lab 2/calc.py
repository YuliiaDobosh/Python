import math
from program import Program

class Calculator(Program ): ##наслідування
    def __init__(self):
        self._result = 0 ##інкапсуляція поля класу є захищеними protected

    def input_numbers(self):
        try:
            self._num1 = float(input("Введіть перше число: "))
            self._num2 = float(input("Введіть друге число: "))
        except ValueError:
            print("Помилка: Введені дані мають бути числовими.")
            self.input_numbers()

    def input_operator(self):
        self._operator = input("Введіть операцію (+, -, *, /, ^, sq, %): ")
        if self._operator not in ['+', '-', '*', '/', '^', 'sq', '%']:
            print("Помилка: Недійсна операція.")
            self.input_operator()

    def calculate(self):
        
        if self._operator == '+':
            self._result = self._num1 + self._num2
        elif self._operator == '-':
            self._result = self._num1 - self._num2
        elif self._operator == '*':
            self._result = self._num1 * self._num2
        elif self._operator == '/':
            if self._num2 == 0:
                print("Помилка: Ділення на нуль.")
            else:
                self._result = self._num1 / self._num2
        elif self._operator == '^':
            self._result = self._num1 ** self._num2
        elif self._operator == 'sq':
            if self._num1 < 0:
                print("Помилка: Корінь від'ємного числа.")
            else:
                self._result = math.sqrt(self._num1)
        elif self._operator == '%':
            self._result = self._num1 % self._num2

    def display_result(self):
        print(f"Результат: {self._result}")

    def run(self):
        while True:
            self.input_numbers()
            self.input_operator()
            self.calculate()
            self.display_result()
            choice = input("Бажаєте продовжити (так/ні)? ")
            if choice.lower() != 'так':
                break