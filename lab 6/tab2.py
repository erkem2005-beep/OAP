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
    print(row)

print("\nСуммы элементов по строкам:")
row_sums = []

for i in range(rows):
    row_sum = sum(matrix[i])
    row_sums.append(row_sum)
    print(f"Сумма строки {i}: {row_sum}")

print("\nСуммы элементов по столбцам:")
for j in range(cols):
    col_sum = 0
    for i in range(rows):
        col_sum += matrix[i][j]
    print(f"Сумма столбца {j}: {col_sum}")

max_row_index = row_sums.index(max(row_sums))
print("Строка с максимальной суммой:", max_row_index)