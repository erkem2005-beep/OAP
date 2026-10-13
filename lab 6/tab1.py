import random

rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(random.randint(1, 20))
    matrix.append(row)

print("\nМатрица:")
for row in matrix:
    for value in row:
        print(f"{value:4}", end="")
    print()

total = 0
maximum = matrix[0][0]

for row in matrix:
    for value in row:
        total += value
        if value > maximum:
            maximum = value

print("\nСумма элементов:", total)
print("Максимальный элемент:", maximum)