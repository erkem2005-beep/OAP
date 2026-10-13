def shift_right(row):
    new_row = [x for x in row if x != 0]
    zeros = [0] * (len(row) - len(new_row))
    return zeros + new_row


matrix = [
    [0, 2, 0, 4],
    [1, 0, 3, 0],
    [0, 0, 5, 6],
    [7, 0, 0, 8]
]

print("До сдвига:")
for row in matrix:
    print(row)

for i in range(4):
    matrix[i] = shift_right(matrix[i])

print("\nПосле сдвига вправо:")
for row in matrix:
    print(row)