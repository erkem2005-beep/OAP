scores = {"A": 90, "B": 75}

name = input("Код: ").strip()

try:
    print(scores[name])

except KeyError:
    print("Ключ не найден")