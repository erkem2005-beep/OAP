from collections import deque

graph = {
    1: [2, 3, 6],
    2: [1, 4],
    3: [1, 4, 5, 6],
    4: [2, 3, 5],
    5: [3, 4, 6],
    6: [1, 3, 5]
}

# Алгоритм BFS через очередь
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Запуск BFS
print("Обход графа BFS через очередь:")
bfs(graph, 1)