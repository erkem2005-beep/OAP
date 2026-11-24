values = [3, 8, 5]

if len(values) == 0:
    print("Список пуст")
else:
    maximum = values[0]

    for v in values:
        if v > maximum:
            maximum = v

    print(maximum)