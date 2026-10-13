n = int(input("Введите количество элементов: "))

while n <= 0:
    print("Количество элементов должно быть больше 0.")
    n = int(input("Введите количество элементов: "))

array = []

for i in range(n):
    number = int(input(f"Введите элемент {i + 1}: "))
    array.append(number)

positive = 0
negative = 0
even = 0

for number in array:
    if number > 0:
        positive += 1

    if number < 0:
        negative += 1

    if number % 2 == 0:
        even += 1

print("Массив:", array)
print("Количество положительных чисел:", positive)
print("Количество отрицательных чисел:", negative)
print("Количество чётных элементов:", even)