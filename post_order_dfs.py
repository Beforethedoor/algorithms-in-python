class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root: int) -> None:
        self.root = Node(root)

    def post_order_dfs(self) -> None:
        """Print out all tree nodes
        as they are visited in
        a post-order traversal."""
        current = self.root
        visited = set()
        result = list()
        while (current and current not in visited):
            if (current.left and current.left not in visited):
                current = current.left
            elif (current.right and current.right not in visited):
                current = current.right
            else:
                result.append(current.value)
                visited.add(current)
                current = self.root
        return result


# Set up tree
tree = Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

# Test
# Should be [4, 5, 2, 6, 7, 3, 1]
print(tree.post_order_dfs())
