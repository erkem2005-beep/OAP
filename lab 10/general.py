# Задача 1. Создание класса Node

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Задание 2 Класс бинарного дерева

class BinaryTree:
    def __init__(self):
        self.root = None

    # Добавление элемента в дерево
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert(current.left, value)
        else:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert(current.right, value)

    # Задача 3. Прямой обход (Preorder)
    def preorder(self, node):
        if node is not None:
            print(node.value, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    # Задача 4. Симметричный обход (Inorder)
    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)

    # Задача 5. Обратный обход (Postorder)
    def postorder(self, node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end=" ")

    # Задача 6. Подсчет количества узлов
    def count_nodes(self, node):
        if node is None:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

    # Задача 7. Определение высоты дерева
    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    # Задача 8. Подсчет количества листьев
    def count_leaves(self, node):
        if node is None:
            return 0

        if node.left is None and node.right is None:
            return 1

        return self.count_leaves(node.left) + self.count_leaves(node.right)

    # Задача 9. Поиск значения в дереве
    def search(self, node, value):
        if node is None:
            return False

        if node.value == value:
            return True

        if value < node.value:
            return self.search(node.left, value)
        else:
            return self.search(node.right, value)


# Задача 10. Главная программа

tree = BinaryTree()

# Создание дерева из значений
values = [20, 10, 30, 5, 15, 25, 35]

for value in values:
    tree.insert(value)
