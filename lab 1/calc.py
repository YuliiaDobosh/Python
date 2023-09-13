num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
operator = input("Введіть операцію (+, -, *, /): ")
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 == 0:
        result = "Помилка: ділення на нуль"
    else:
                result = num1 / num2
else:
    result = "Невідома операція"

print(f"Результат: {result}")