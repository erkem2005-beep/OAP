graph = {
    1: [2, 3, 6],
    2: [1, 4],
    3: [1, 4, 5, 6],
    4: [2, 3, 5],
    5: [3, 4, 6],
    6: [1, 3, 5]
}

# Функция подсчёта достижимых вершин
def count_reachable(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)

    return len(visited) - 1

# Ввод стартовой вершины
start = int(input("Введите стартовую вершину: "))

if start in graph:
    result = count_reachable(graph, start)
    print("Количество достижимых вершин:", result)
else:
    print("Такой вершины нет в графе!")