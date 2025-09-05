def check_even_odd():

    user_input = input("Введите любое число, оно будет округлено: ")

    try:
        number = float(user_input)
        rounded_num = round(number)
        if rounded_num % 2 == 0:
            print(f"Число {rounded_num} является четным")
        else:
            print(f"Число {rounded_num} - нечётное")
    except ValueError:

        print("Ошибка! Вы ввели не целое число. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    check_even_odd()
