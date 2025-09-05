def demonstrate_variables_and_f_strings():
    """Блок 1: Переменные и f-строки"""
    print("--- Блок 1: Переменные и f-строки ---")
    my_name = "Алекс"
    my_age = 25
    print(f"Меня зовут {my_name}, и мне {my_age} лет.")

def demonstrate_user_input():
    '''Блок 2: Пользовательский ввод'''
    print("\n--- Блок 2: Пользовательский ввод ---")
    user_name = input("Как тебя зовут? ")
    print(f"Приятно познакомиться, {user_name}!")

def demonstrate_math_operations():
    """Блок 3: Математические операции"""
    print("\n--- Блок 3: Математические операции ---")
    a = 20
    b = 8
    print(f"Даны два числа: a = {a}, b = {b}")
    print(f"Сложение (a + b): {a + b}")
    print(f"Вычитание (a - b): {a - b}")
    print(f"Умножение (a * b): {a * b}")
    print(f"Деление (a / b): {a / b}")

def demonstrate_type_casting():
    """Блок 4 и 5: Преобразование типов и обработка ошибок"""
    print("\n--- Блок 4 и 5: Преобразование типов и обработка ошибок ---")
    age_str = input("Введи свой возраст: ")
    try:
        age = int(age_str)
        print(f"Через год тебе будет {age + 1}.")
    except ValueError:
        print("Ошибка! Ты ввел не число.")

def demonstrate_string_methods():
    """Блок 6: Работа со строками"""
    print("\n--- Блок 6: Работа со строками ---")
    sentence = "Я изучаю язык Python"
    print(f"Предложение: '{sentence}'")
    print(f"Длина этого предложения: {len(sentence)} символов.")
    words = sentence.split()
    print(f"Предложение, разрезанное на слова: {words}")

def demonstrate_conditions():
    """Блок 7: Условные операторы"""
    print("\n--- Блок 7: Условные операторы ---")
    temperature_str = input("Какая сейчас температура на улице? ")
    try:
        temperature = float(temperature_str)
        if temperature > 25:
            print("Очень жарко! Надень футболку.")
        elif temperature > 15:
            print("Тепло. Можно пойти в кофте.")
        else:
            print("Прохладно, лучше надеть куртку.")
    except ValueError:
        print("Ошибка! Введите температуру числом.")

def demonstrate_loops():
    """Блок 8: Циклы"""
    print("\n--- Блок 8: Циклы ---")
    print("Начинаю обратный отсчет (цикл FOR):")
    for number in range(3, 0, -1):
        print(number)
    print("Старт!")

    print("\nПовторяю, пока не скажешь 'стоп' (цикл WHILE):")
    user_word = ""
    while user_word.lower() != "стоп":
        user_word = input("Скажи 'стоп', чтобы закончить: ")
        if user_word.lower() != "стоп":
            print("...снова и снова...")
    print("Цикл завершен.")

def main():
    print("--- Стартуем демонстрацию всех блоков урока ---")
    demonstrate_variables_and_f_strings()
    demonstrate_user_input()
    demonstrate_math_operations()
    demonstrate_type_casting()
    demonstrate_string_methods()
    demonstrate_conditions()
    demonstrate_loops()
    print("\n--- Демонстрация завершена ---")

if __name__ == "__main__":
    main()