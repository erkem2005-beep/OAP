graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 4, 5],
    4: [2, 3, 5],
    5: [3, 4]
}

# Добавляем новую вершину 6
graph[6] = [1, 3, 5]

# Соединяем новые вершины с существующими
graph[1].append(6)
graph[3].append(6)
graph[5].append(6)

print("Обновлённый граф:")
for vertex in graph:
    print(vertex, "->", graph[vertex])