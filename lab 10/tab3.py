 # Задача 3. Прямой обход (Preorder)
    def preorder(self, node):
        if node is not None:
            print(node.value, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)
