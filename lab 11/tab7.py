from collections import deque

graph = {
    1: [2, 3, 6],
    2: [1, 4],
    3: [1, 4, 5, 6],
    4: [2, 3, 5],
    5: [3, 4, 6],
    6: [1, 3, 5]
}

# Функция BFS
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    order = []

    visited.add(start)

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order

# Ввод стартовой вершины
start = int(input("Введите стартовую вершину: "))

# Проверка и выполнение обхода
if start in graph:
    result = bfs(graph, start)
    print("Порядок посещения вершин:", result)
else:
    print("Такой вершины нет в графе!")