def simple_calculator():
    try:

        num1_str = input("Введите первое число: ")
        num1 = float(num1_str)

        num2_str = input("Введите второе число: ")
        num2 = float(num2_str)

        operation = input("Какую операцию вы хотите выполнить? (+, -, *, /): ")

        if operation == '+':
            result = num1 + num2
            print(f"Результат: {num1} + {num2} = {result}")
        elif operation == '-':
            result = num1 - num2
            print(f"Результат: {num1} - {num2} = {result}")
        elif operation == '*':
            result = num1 * num2
            print(f"Результат: {num1} * {num2} = {result}")
        elif operation == '/':
            # Дополнительная проверка: на ноль делить нельзя!
            if num2 == 0:
                print("Ошибка! Деление на ноль невозможно.")
            else:
                result = num1 / num2
                print(f"Результат: {num1} / {num2} = {result}")
        else:
            print("Неизвестная операция. Пожалуйста, используйте +, -, * или /.")

    except ValueError:
        print("Ошибка! Вы ввели не число. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    simple_calculator()