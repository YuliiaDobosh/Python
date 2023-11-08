from collections.abc import Callable, Mapping, Sequence
from typing import Any
from consolemenu import *
from consolemenu.console_menu import ConsoleMenu
from consolemenu.items import *

import lab1.calc
import lab2.main
import lab3.main
import lab4.main
import lab5.main
import lab6.main
import lab7.main

menu = ConsoleMenu("Runner of labs")
menu.append_item(FunctionItem("Simple Calculator", lab1.calc.main))
menu.append_item(FunctionItem("OOP Calculator", lab2.main.main))
menu.append_item(FunctionItem("ASCII Art", lab3.main))
menu.append_item(FunctionItem("2D ASCII Art(no libraries)", lab4.main.main))
menu.append_item(FunctionItem("3D ASCII Arts", lab5.main.main))
menu.append_item(FunctionItem("Unit tests of calculator", lab6.main.main))
menu.append_item(FunctionItem("API", lab7.main.main))

menu.show()