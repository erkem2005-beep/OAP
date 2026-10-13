n = int(input("Введите число n: "))

while n < 1:
    n = int(input("Введите число n не меньше 1: "))

total = 0

for i in range(1, n + 1):
    total += i

print("Сумма чисел от 1 до", n, "равна:", total)