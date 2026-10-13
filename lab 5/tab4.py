n = int(input("Введите количество элементов: "))

while n <= 0:
    print("Количество элементов должно быть больше 0.")
    n = int(input("Введите количество элементов: "))

array = []

for i in range(n):
    number = int(input(f"Введите элемент {i + 1}: "))
    array.append(number)

search = int(input("Введите число для поиска: "))

found = False

for i in range(n):
    if array[i] == search:
        print("Число найдено. Индекс:", i)
        found = True
        break

if not found:
    print("Число не найдено.")

print("Массив:", array)