from helpers.binarytree import (
    TreeNode,
    parse_binary_tree,
)


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # Non-recursive solution
    #def maxDepth(self, root: TreeNode | None) -> int:
    #    if root is None:
    #        return 0

    #    from collections import deque

    #    nodes = deque()
    #    nodes.append(root)

    #    depths: dict[TreeNode, int] = {}
    #    depths[root] = 1
    #    max_depth: int = 1

    #    while len(nodes) > 0:
    #        node = nodes.popleft()
    #        depth = depths[node]

    #        if node.right is not None:
    #            nodes.append(node.right)
    #            right_depth = depth + 1
    #            depths[node.right] = right_depth
    #            max_depth = max(max_depth, right_depth)

    #        if node.left is not None:
    #            nodes.append(node.left)
    #            left_depth = depth + 1
    #            depths[node.left] = left_depth
    #            max_depth = max(max_depth, left_depth)

    #    return max_depth


if __name__ == "__main__":
    solution = Solution()

    assert solution.maxDepth(parse_binary_tree([3, 9, 20, None, None, 15, 7])) == 3
    assert solution.maxDepth(parse_binary_tree([1, None, 3])) == 2
