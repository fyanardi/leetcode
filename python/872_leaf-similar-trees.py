from helpers.binarytree import (
    TreeNode,
    build_binary_tree,
    # print_binary_tree
)


class Solution:
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        if root1 is None:
            return root2 is None

        if root2 is None:
            return root1 is None

        nodes1 = []
        nodes2 = []

        leaves1 = []
        leaves2 = []

        nodes1.append(root1)
        nodes2.append(root2)

        while len(nodes1) > 0:
            node = nodes1.pop()

            if node.right is not None:
                nodes1.append(node.right)

            if node.left is not None:
                nodes1.append(node.left)

            if node.left is None and node.right is None:
                leaves1.append(node)

        while len(nodes2) > 0:
            node = nodes2.pop()

            if node.right is not None:
                nodes2.append(node.right)

            if node.left is not None:
                nodes2.append(node.left)

            if node.left is None and node.right is None:
                leaves2.append(node)

        return [l.val for l in leaves1] == [l.val for l in leaves2]


if __name__ == "__main__":
    solution = Solution()

    # print_binary_tree(build_binary_tree([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]), 0)
    # print_binary_tree(build_binary_tree([3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8]), 0)

    assert solution.leafSimilar(
        root1=build_binary_tree([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]),
        root2=build_binary_tree([3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8])
    ) == True
    assert solution.leafSimilar(root1=build_binary_tree([1,2,3]), root2=build_binary_tree([1,3,2])) == False
