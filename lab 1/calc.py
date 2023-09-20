import math

class Calculator:
    # Ініціалізуємо атрибути, які будуть використовуватися для операцій калькулятора
    def __init__(self): #Завд №2
        self.num1 = None
        self.num2 = None
        self.operator = None

    def get_user_input(self):
        # Запитуємо користувача про введення чисел і оператора
        try:
            self.num1 = float(input("Введіть перше число: "))
            self.operator = input("Введіть операцію (+, -, *, /, ^, √, %): ") 
            if self.operator not in ('+', '-', '*', '/', '^', '√', '%'): # Завд №4 + №9
                print("Помилка: Невідомий оператор.")
                return
            if self.operator in ('^', '√', '%'):
                if self.operator != '√':
                    self.num2 = float(input("Введіть друге число: "))
                else:
                    self.num2 = None
        except ValueError:
            print("Помилка: Введіть коректні числа.")

    def calculate(self): #Завд №5
        try:
            if self.operator == '+':
                result = self.num1 + self.num2
            elif self.operator == '-':
                result = self.num1 - self.num2
            elif self.operator == '*':
                result = self.num1 * self.num2
            elif self.operator == '/':
                if self.num2 != 0: #Завд №6
                    result = self.num1 / self.num2
                else:
                    print("Помилка: Ділення на нуль.")
                    return
            elif self.operator == '^':
                result = self.num1 ** self.num2
            elif self.operator == '√':
                result = math.sqrt(self.num1)
            elif self.operator == '%':
                result = self.num1 % self.num2
            else:
                print("Помилка: Невідомий оператор.")
                return

            print(f"Результат: {self.num1} {self.operator} {self.num2 if self.num2 is not None else ''} = {result:.2f}")
        except Exception as e:
            print(f"Помилка: {e}")

    def run(self):
        while True:
            self.get_user_input()
            self.calculate()
            choice = input("Бажаєте продовжити (так/ні)? ").lower() #Завд №7
            if choice != 'так':
                break

# Створюємо об'єкт класу Calculator і запускаємо програму
calc = Calculator()
calc.run()