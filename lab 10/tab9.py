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