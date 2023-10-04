import math

class Calculator:
    def __init__(self):
        self.result = 0

    def input_numbers(self):
        try:
            self.num1 = float(input("Введіть перше число: "))
            self.num2 = float(input("Введіть друге число: "))
        except ValueError:
            print("Помилка: Введені дані мають бути числовими.")
            self.input_numbers()

    def input_operator(self):
        self.operator = input("Введіть операцію (+, -, *, /, ^, sq, %): ")
        if self.operator not in ['+', '-', '*', '/', '^', 'sq', '%']:
            print("Помилка: Недійсна операція.")
            self.input_operator()

    def calculate(self):
        pass

    def display_result(self):
        print(f"Результат: {self.result}")

    def run(self):
        while True:
            self.input_numbers()
            self.input_operator()
            self.calculate()
            self.display_result()
            choice = input("Бажаєте продовжити (так/ні)? ")
            if choice.lower() != 'так':
                break

class BasicCalculator(Calculator):
    def calculate(self):
        if self.operator == '+':
            self.result = self.num1 + self.num2
        elif self.operator == '-':
            self.result = self.num1 - self.num2
        elif self.operator == '*':
            self.result = self.num1 * self.num2
        elif self.operator == '/':
            if self.num2 == 0:
                print("Помилка: Ділення на нуль.")
            else:
                self.result = self.num1 / self.num2
        elif self.operator == '^':
            self.result = self.num1 ** self.num2
        elif self.operator == 'sq':
            if self.num1 < 0:
                print("Помилка: Корінь від'ємного числа.")
            else:
                self.result = math.sqrt(self.num1)
        elif self.operator == '%':
            self.result = self.num1 % self.num2

if __name__ == "__main__":
    calculator = BasicCalculator()
    calculator.run()