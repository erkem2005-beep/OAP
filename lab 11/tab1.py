graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 4, 5],
    4: [2, 3, 5],
    5: [3, 4]
}

print("Список смежности графа:")
for vertex in graph:
    print(vertex, "->", graph[vertex])