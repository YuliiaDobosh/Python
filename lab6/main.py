import unittest
from lab2.calc import Calculator

class TestCalculatorMethods(unittest.TestCase):
    def test_init(self):
        calc = Calculator()
        self.assertEqual(0, calc._result)
    # Перевірка введених чисел - _num1 та _num2 повинні бути або типу float, або int.
    def test_input_nums(self):
        calc = Calculator()
        calc.input_numbers()

        self.assertIsInstance(calc._num1, float | int)
        self.assertIsInstance(calc._num2, float | int)
        
    # Перевірка введеного оператора - _operator повинен бути типу str.
    def test_input_operator(self):
        calc = Calculator()
        calc.input_operator()

        self.assertIsInstance(calc._operator, str)

    # Перевірка функціоналу додавання.
    def test_add(self):
        calc = Calculator()
        calc._num1 = 3
        calc._num2 = 11
        calc._operator = '+'
        calc.calculate()

        self.assertEqual(calc._result, 14)

    # Перевірка функціоналу віднімання.
    def test_subtract(self):
        calc = Calculator()
        calc._num1 = 15
        calc._num2 = 5
        calc._operator = '-'
        calc.calculate()

        self.assertEqual(calc._result, 10)

    # Перевірка функціоналу множення.
    def test_multiply(self):
        calc = Calculator()
        calc._num1 = 4
        calc._num2 = 5
        calc._operator = '*'
        calc.calculate()

        self.assertEqual(calc._result, 20)

    # Перевірка функціоналу ділення.
    def test_divide(self):
        calc = Calculator()
        calc._num1 = 20
        calc._num2 = 5
        calc._operator = '/'
        calc.calculate()

        self.assertEqual(calc._result, 4)

    # Тест на випадок ділення на нуль - має викликати ZeroDivisionError.
    def test_divide_by_zero(self):
        calc = Calculator()
        calc._num1 = 10
        calc._num2 = 0
        calc._operator = '/'
        
        with self.assertRaises(ZeroDivisionError):
            calc.calculate()

# Запуск тестів
def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculatorMethods)
    runner = unittest.TextTestRunner()
    runner.run(suite)
    input()

if __name__ == '__main__':
    main()