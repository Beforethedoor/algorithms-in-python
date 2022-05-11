from collections import deque


class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root: int) -> None:
        self.root = Node(root)

    def bfs(self) -> None:
        """Print out all tree nodes
        as they are visited in
        a bfs traversal."""
        q = deque([self.root])
        result = []

        while q:
            node = q.popleft()
            result.append(node.value)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return result


# Set up tree
tree = Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)


# Test
# Should be [1, 2, 3, 4, 5]
print(tree.bfs())
