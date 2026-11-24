try:
    a = float(input("Сумма: "))
    b = float(input("Количество: "))

    if b <= 0:
        print("Ошибка: количество должно быть больше нуля")
    else:
        print("Среднее:", a / b)

except ValueError:
    print("Ошибка: введите число")