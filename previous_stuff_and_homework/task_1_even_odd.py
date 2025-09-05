def check_even_odd():

    user_input= input("Введите любое целое число: ")

    try:
        number = int(user_input)

        if number % 2 == 0:
            print(f"Число {number} - чётное")

        else:
            print(f"Число {number} - нечётное")

    except ValueError:

        print("Ошибка! Вы ввели не целое число. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    check_even_odd()