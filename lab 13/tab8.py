try:
    temperature = float(input("Температура: "))

    if temperature >= 37.5:
        print("Повышена")
    else:
        print("Норма")

except ValueError:
    print("Ошибка: введите число")