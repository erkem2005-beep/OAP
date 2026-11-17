with open("notes.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

print("Содержимое файла:")
for line in lines:
    print(line.strip())

print("Количество строк:", len(lines))
