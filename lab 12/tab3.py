import json

students = []

# Чтение исходного файла
try:
    with open("data.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    for number, line in enumerate(lines, start=1):
        line = line.strip()

        if not line:
            continue

        parts = line.split(";")

        if len(parts) != 2:
            print(f"Ошибка в строке {number}: неверный формат")
            continue

        name = parts[0].strip()

        try:
            score = float(parts[1].strip())

            if not name or score < 0 or score > 100:
                print(f"Ошибка в строке {number}: неверные данные")
                continue

            students.append({
                "name": name,
                "score": score
            })

        except ValueError:
            print(f"Ошибка в строке {number}: балл не является числом")

except FileNotFoundError:
    print("Ошибка: файл data.txt не найден!")
    exit()

# Проверка наличия данных
if len(students) == 0:
    print("Нет корректных данных для обработки.")
    exit()

# Вычисление среднего балла
total = sum(student["score"] for student in students)
average = total / len(students)

# Поиск лучшего результата
best_student = max(students, key=lambda x: x["score"])

# Формирование результата
result = {
    "students": students,
    "statistics": {
        "number_of_students": len(students),
        "average_score": round(average, 2),
        "best_student": best_student
    }
}

# Запись в JSON
with open("result.json", "w", encoding="utf-8") as file:
    json.dump(result, file, ensure_ascii=False, indent=4)

print("Данные успешно сохранены в result.json")

# Повторная загрузка JSON
with open("result.json", "r", encoding="utf-8") as file:
    loaded_data = json.load(file)

# Вывод итоговой информации
print("\n========== РЕЗУЛЬТАТ ==========")

print("Количество студентов:",
      loaded_data["statistics"]["number_of_students"])

print("Средний балл:",
      loaded_data["statistics"]["average_score"])

print("Лучший студент:",
      loaded_data["statistics"]["best_student"]["name"])

print("Лучший балл:",
      loaded_data["statistics"]["best_student"]["score"])

print("===============================")