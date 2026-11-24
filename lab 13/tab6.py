items = [10, 20, 30]

try:
    index = int(input("Индекс: "))

    if 0 <= index < len(items):
        print(items[index])
    else:
        print("Ошибка: индекс вне диапазона")

except ValueError:
    print("Ошибка: введите целое число")