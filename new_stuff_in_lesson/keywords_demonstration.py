def check_access_rules(age, has_ticket, is_vip):
    """
    Проверяет правила доступа, используя логические операторы.
    """
    print(f"\n--- Проверка для: возраст={age}, билет={has_ticket}, VIP={is_vip} ---")

    # 1. Оператор 'and' (И)
    # Условие истинно, только если ОБА под-условия истинны.
    # Аналогия: Чтобы войти в кино, нужно (иметь билет) И (фильм еще не начался).
    if age >= 18 and has_ticket:
        print("✅ [AND]: Проход на сеанс 18+ с билетом разрешен.")
    else:
        print("❌ [AND]: Проход на сеанс 18+ запрещен (не выполнено одно из условий).")

    # 2. Оператор 'or' (ИЛИ)
    # Условие истинно, если ХОТЯ БЫ ОДНО под-условие истинно.
    # Аналогия: Чтобы получить скидку, можно быть (студентом) ИЛИ (пенсионером).
    if is_vip or has_ticket:
        print("✅ [OR]: Доступ в здание разрешен (либо по билету, либо как VIP).")
    else:
        print("❌ [OR]: Доступ в здание запрещен (нет ни билета, ни VIP-статуса).")

    # 3. Оператор 'not' (НЕ)
    # Инвертирует (переворачивает) значение. True -> False, False -> True.
    # Аналогия: "Если НЕ идет дождь, то можно идти гулять".
    if not is_vip:
        print("ℹ️ [NOT]: Это обычный посетитель, не VIP-персона.")


def main():
    """Главная функция для запуска всех демонстраций."""
    # Сценарий 1: Совершеннолетний с билетом, не VIP
    # and: True, or: True, not: True
    check_access_rules(age=25, has_ticket=True, is_vip=False)

    # Сценарий 2: Несовершеннолетний с билетом, не VIP
    # and: False, or: True, not: True
    check_access_rules(age=16, has_ticket=True, is_vip=False)

    # Сценарий 3: Совершеннолетний VIP без билета
    # and: False, or: True, not: False
    check_access_rules(age=40, has_ticket=False, is_vip=True)

    # Сценарий 4: Совершеннолетний без билета и не VIP
    # and: False, or: False, not: True
    check_access_rules(age=30, has_ticket=False, is_vip=False)


if __name__ == "__main__":
    main()