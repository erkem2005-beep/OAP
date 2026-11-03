# Задача 8. Подсчет количества листьев
    def count_leaves(self, node):
        if node is None:
            return 0

        if node.left is None and node.right is None:
            return 1

        return self.count_leaves(node.left) + self.count_leaves(node.right)