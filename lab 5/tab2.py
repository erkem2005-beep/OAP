n = int(input("Введите количество элементов: "))

while n <= 0:
    print("Количество элементов должно быть больше 0.")
    n = int(input("Введите количество элементов: "))

array = []

for i in range(n):
    number = int(input(f"Введите элемент {i + 1}: "))
    array.append(number)

total = 0
maximum = array[0]
minimum = array[0]

for number in array:
    total += number

    if number > maximum:
        maximum = number

    if number < minimum:
        minimum = number

average = total / n

print("Массив:", array)
print("Сумма элементов:", total)
print("Максимальный элемент:", maximum)
print("Минимальный элемент:", minimum)
print("Среднее арифметическое:", average)