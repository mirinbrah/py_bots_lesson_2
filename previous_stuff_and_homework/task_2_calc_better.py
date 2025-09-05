def simple_calculator_flat():
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        operation = input("Какую операцию вы хотите выполнить? (+, -, *, /): ")

        if operation not in ['+', '-', '*', '/']:
            print("Неизвестная операция. Пожалуйста, используйте +, -, * или /.")
            return

        if operation == '/' and num2 == 0:
            print("Ошибка! Деление на ноль невозможно.")
            return

        result = 0
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            result = num1 / num2

        # Вывод результата вынесен в одно место, что тоже хорошо
        print(f"Результат: {num1} {operation} {num2} = {result}")

    except ValueError:
        print("Ошибка! Вы ввели не число. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    simple_calculator_flat()