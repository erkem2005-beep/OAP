n = int(input("Введите количество элементов: "))

while n <= 0:
    print("Количество элементов должно быть больше 0.")
    n = int(input("Введите количество элементов: "))

array = []

for i in range(n):
    number = int(input(f"Введите элемент {i + 1}: "))
    array.append(number)

print("Массив:", array)

if n < 2:
    print("Недостаточно элементов для поиска второго по величине.")
else:
    maximum = array[0]
    second_maximum = array[1]

    if second_maximum > maximum:
        maximum, second_maximum = second_maximum, maximum

    for i in range(2, n):
        if array[i] > maximum:
            second_maximum = maximum
            maximum = array[i]
        elif array[i] > second_maximum:
            second_maximum = array[i]

    print("Второй по величине элемент:", second_maximum)