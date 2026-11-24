try:
    with open("scores.txt", "r", encoding="utf-8") as f:
        content = f.read()

        if content == "":
            print("Файл пуст")
        else:
            print(content)

except FileNotFoundError:
    print("Файл не найден")

except PermissionError:
    print("Нет разрешения на чтение файла")