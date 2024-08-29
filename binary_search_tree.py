class BSTNode:
    def __init__(self, value = None):
        self.left = None
        self.right = None
        self.value = value

    def __repr__(self):
        lines = []
        self.format_tree_string(lines)
        return "\n".join(lines)

    def format_tree_string(self, lines, level = 0):
        if self.right is not None:
            self.right.format_tree_string(lines, level + 1)

        lines.append(" " * 4 * level + "> " + str(self.value))

        if self.left is not None:
            self.left.format_tree_string(lines, level + 1)

    def insert(self, value):
        if self.value is None:
            self.value = value
            return

        if self.value == value:
            return

        if self.value < value:
            if self.right:
                self.right.insert(value)
                return

            self.right = BSTNode(value)
            return

        if self.value > value:
            if self.left:
                self.left.insert(value)
                return

            self.left = BSTNode(value)
            return

    def delete(self, value):
        if self.value is None:
            return None

        if value < self.value:
            if self.left:
                self.left = self.left.delete(value)
            return self

        if value > self.value:
            if self.right:
                self.right = self.right.delete(value)
            return self

        if self.right is None:
            return self.left

        if self.left is None:
            return self.right

        min_larger_node = self.right
        while min_larger_node.left is not None:
            min_larger_node = min_larger_node.left

        self.value = min_larger_node.value
        self.right = self.right.delete(min_larger_node.value)

        return self

    def preorder(self, visited: list):
        if self.value is not None:
            visited.append(self.value)

        if self.left is not None:
            self.left.preorder(visited)

        if self.right is not None:
            self.right.preorder(visited)

        return visited

    def postorder(self, visited: list):
        if self.left is not None:
            self.left.postorder(visited)

        if self.right is not None:
            self.right.postorder(visited)

        if self.value is not None:
            visited.append(self.value)

        return visited

    def inorder(self, visited: list):
        if self.left is not None:
            self.left.inorder(visited)

        if self.value is not None:
            visited.append(self.value)

        if self.right is not None:
            self.right.inorder(visited)

        return visited

    def exists(self, value):
        if self.value == value:
            return True

        if self.value < value:
            if self.right:
                return self.right.exists(value)

        if self.value > value:
            if self.left:
                return self.left.exists(value)

        return False
