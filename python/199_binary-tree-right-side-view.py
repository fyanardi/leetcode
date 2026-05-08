from helpers.binarytree import (
    TreeNode,
    build_binary_tree,
)


class Solution:
    def rightSideView(self, root: TreeNode  | None) -> list[int]:
        if root is None:
            return []

        from collections import deque

        nodes = deque()
        nodes.append(root)

        results: list[int] = []

        while len(nodes) > 0:
            size = len(nodes)

            # this inner loops ensures that all nodes being evaluated belong to the same level
            # hence the size is populated once with the current size of the queue
            # the last node evaluated per level is the rightmost node for that level
            while size > 0:
                node: TreeNode = nodes.popleft()

                if node.left is not None:
                    nodes.append(node.left)

                if node.right is not None:
                    nodes.append(node.right)

                size -= 1
                if size == 0:
                    results.append(node.val)

        return results


if __name__ == "__main__":
    solution = Solution()

    assert solution.rightSideView(build_binary_tree([1, 2, 3, None, 5, None, 4])) == [1, 3, 4]
    assert solution.rightSideView(build_binary_tree([1, 2, 3, 4, None, None, None, 5])) == [1, 3, 4, 5]
    assert solution.rightSideView(build_binary_tree([1, None, 3])) == [1, 3]
    assert solution.rightSideView(build_binary_tree([])) == []
