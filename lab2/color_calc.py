from .calc import Calculator 
from termcolor import *

class ColorCalculator (Calculator):
    def display_result(self):
        print(colored(f"Результат: {self._result}", "red")) #інкапсуляція , що ми можемо в класах нащадків використовувати захищені зміні 
 