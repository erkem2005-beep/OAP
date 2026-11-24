try:
    age = int(input("Возраст: "))

    if age < 0:
        print("Некорректный возраст")
    elif age >= 18:
        print("Доступ")
    else:
        print("Нет доступа")

except ValueError:
    print("Ошибка: введите целое число")