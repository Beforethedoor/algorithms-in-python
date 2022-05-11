class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root: int) -> None:
        self.root = Node(root)

    def in_order_dfs(self) -> None:
        """Print out all tree nodes
        as they are visited in
        a in-order traversal."""
        current = self.root
        stack = []
        result = list()
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                result.append(current.value)
                current = current.right
            else:
                break
        return result


# Set up tree
tree = Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)


# Test
# Should be [4, 2, 5, 1, 3]
print(tree.in_order_dfs())
