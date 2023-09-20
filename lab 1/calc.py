import math

class Calculator: #Завд №1 
    # Ініціалізуємо атрибути, які будуть використовуватися для операцій калькулятора
    def __init__(self): #Завд №2
        self.num1 = None
        self.num2 = None
        self.operator = None

    def get_user_input(self):
        # Запитуємо користувача про введення чисел і оператора
        try:
            self.num1 = float(input("Введіть перше число: ")) # Завд №3 введення 2-ох значеннь та оператор
            self.operator = input("Введіть операцію (+, -, *, /, ^, √, %): ") 
            if self.operator not in ('+', '-', '*', '/', '^', '√', '%'): # Завд №4 + №9
                print("Помилка: Невідомий оператор.")
                return
            if self.operator in ('+', '-', '*', '/', '^', '√', '%'):
                if self.operator != '√':
                    self.num2 = float(input("Введіть друге число: "))
                else:
                    self.num2 = None
        except ValueError:
            print("Помилка: Введіть коректні числа.")

    def calculate(self): # Завд №5
        try:
            result = None
            if self.operator is not None:
                num1, num2 = self.num1, self.num2 if self.num2 is not None else 0

                match self.operator:
                    case '+':
                        result = num1 + num2
                    case '-':
                        result = num1 - num2
                    case '*':
                        result = num1 * num2
                    case '/':
                        if num2 != 0: #Завд №6
                            result = num1 / num2
                        else:
                            print("Помилка: Ділення на нуль.")
                            return
                    case '^':
                        result = num1 ** num2
                    case '√':
                        result = math.sqrt(num1)
                    case '%':
                        result = num1 % num2
                    case _:
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