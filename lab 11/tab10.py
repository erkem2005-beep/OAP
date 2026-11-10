from collections import deque

graph = {
    1: [2, 3, 6],
    2: [1, 4],
    3: [1, 4, 5, 6],
    4: [2, 3, 5],
    5: [3, 4, 6],
    6: [1, 3, 5]
}

# Поиск кратчайшего пути с помощью BFS
def shortest_path(graph, start, end):
    visited = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == end:
            return path

        if node not in visited:
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    queue.append(new_path)

    return None

# Ввод вершин
start = int(input("Введите начальную вершину: "))
end = int(input("Введите конечную вершину: "))

# Проверка
if start in graph and end in graph:
    result = shortest_path(graph, start, end)

    if result:
        print("Кратчайший путь:", result)
        print("Длина пути:", len(result) - 1)
    else:
        print("Путь не существует!")
else:
    print("Такой вершины нет в графе!")