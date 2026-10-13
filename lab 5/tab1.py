n = int(input("Введите количество элементов: "))

while n <= 0:
    print("Количество элементов должно быть больше 0.")
    n = int(input("Введите количество элементов: "))

array = []

for i in range(n):
    number = int(input(f"Введите элемент {i + 1}: "))
    array.append(number)

print("Массив:", array) 