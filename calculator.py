"""
Эта функция ищет введеную пользователем операцию
"""


def calculator(a, b, operation):
    """
    Внутри выполняются базовые арифметические операции для 2 чисел

    Args:
        a = int или float: Первое число
        b = int или float: Второе число
        operation = операция которую нужно выполнить
    """
    result = None
    try:
        if operation == "add":
            result = a + b
        if operation == "subtract":
            result = a - b
        if operation == "multiply":
            result = a * b
        if operation == "divide":
            if b != 0:
                result = a / b
            else:
                return "Cannot divide by zero"

        if operation == "modulus":
            if b != 0:
                result = a % b
            else:
                return "Cannot modulus by zero"

        if operation == "power":
            result = a**b

    except TypeError:
        result = "Invalid input. Please write the correct operation as in the example above"

    return result


input_a = float(input("Введите первое число: "))
input_b = float(input("Введите второе число: "))
input_oper = input(
    "\nВведите операцию, которую хотите выполнить(ввести нужно на английском):"
    "\nAdd(Плюс) \nSubtract(Минус)\nMultiply(Умножение) "
    "\nDivide(Деление) \nModulus(Остаток) \nPower(Степень) \n"
)
calc_operation = input_oper.lower()
print(calculator(input_a, input_b, calc_operation))
