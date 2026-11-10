from collections import deque

graph = {
    1: [2, 3, 6],
    2: [1, 4],
    3: [1, 4, 5, 6],
    4: [2, 3, 5],
    5: [3, 4, 6],
    6: [1, 3, 5]
}

# Проверка существования пути между двумя вершинами
def has_path(graph, start, end):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node == end:
            return True

        if node not in visited:
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return False

# Ввод двух вершин
start = int(input("Введите первую вершину: "))
end = int(input("Введите вторую вершину: "))

# Проверка
if start in graph and end in graph:
    if has_path(graph, start, end):
        print("Путь между вершинами существует!")
    else:
        print("Путь между вершинами не существует!")
else:
    print("Такой вершины нет в графе!")