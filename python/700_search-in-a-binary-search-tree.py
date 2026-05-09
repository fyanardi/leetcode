from helpers.binarytree import (
    TreeNode,
    parse_binary_tree,
    serialize_binary_tree,
)


class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if root is None:
            return None

        if root.val == val:
            return root

        if val > root.val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)


if __name__ == "__main__":
    solution = Solution()

    assert serialize_binary_tree(
        root=solution.searchBST(parse_binary_tree([4, 2, 7, 1, 3]), 2)
    ) == [2, 1, 3]

    assert serialize_binary_tree(
        root=solution.searchBST(parse_binary_tree([4, 2, 7, 1, 3]), 5)
    ) == []
