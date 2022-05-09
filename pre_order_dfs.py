class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root: int) -> None:
        self.root = Node(root)

    def pre_order_dfs(self) -> None:
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        stack = list()
        stack.append(self.root)
        result = list()
        while stack:
            n = stack.pop()
            result.append(n.value)
            if n.right:
                stack.append(n.right)
            if n.left:
                stack.append(n.left)
        return result


# Set up tree
tree = Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)


# Test
# Should be [1, 2, 4, 5, 3]
print(tree.pre_order_dfs())
