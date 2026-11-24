grades = [70, 80, 90]

if len(grades) == 0:
    print("Нет оценок")
else:
    average = sum(grades) / len(grades)
    print(average)