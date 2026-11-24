try:
    price = float(input("Цена: "))
    discount = float(input("Скидка (%): "))

    if price < 0 or discount < 0 or discount > 100:
        print("Некорректные данные")
    else:
        result = price - price * discount / 100
        print(result)

except ValueError:
    print("Ошибка: введите число")