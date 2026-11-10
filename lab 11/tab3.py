graph = {
    1: [2, 3, 6],
    2: [1, 4],
    3: [1, 4, 5, 6],
    4: [2, 3, 5],
    5: [3, 4, 6],
    6: [1, 3, 5]
}

# Функция вывода соседей вершины
def show_neighbors(graph, vertex):
    if vertex in graph:
        print("Соседи вершины", vertex, ":", graph[vertex])
    else:
        print("Такой вершины нет в графе")

# Проверка функции
show_neighbors(graph, 3)