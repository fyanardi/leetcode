from helpers.binarytree import (
    TreeNode,
    build_binary_tree,
)


class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        if root is None:
            return 0

        def path_sum(node: TreeNode | None, target_sum: int, prev_sum: int | None) -> int:
            if node is None:
                return 0

            # possible number of paths from combination of:
            # 1. started from one of the parent node
            # 2. started from this node, disregarding the parent node (and all previous parents)
            # 3. started from the left node, disregarding current node
            # 4. started from the right node, disregarding current node
            num_paths: int = 0

            if prev_sum is not None:
                if prev_sum + node.val == target_sum:
                    num_paths += 1
            else:
                if node.val == target_sum:
                    num_paths += 1

            if node.left is not None:
                if prev_sum is not None:
                    # if prev_sum is specified, find paths starting from one of the grandparent node
                    num_paths += path_sum(node.left, target_sum, prev_sum + node.val)
                else:
                    # if prev_sum is not specified, start a new path from this node
                    num_paths += path_sum(node.left, target_sum, node.val)
                    # Also try a new path starting from the left node
                    num_paths += path_sum(node.left, target_sum, None)

            if node.right is not None:
                if prev_sum is not None:
                    num_paths += path_sum(node.right, target_sum, prev_sum + node.val)
                else:
                    num_paths += path_sum(node.right, target_sum, node.val)
                    num_paths += path_sum(node.right, target_sum, None)

            return num_paths

        return path_sum(root, targetSum, None)


if __name__ == "__main__":
    solution = Solution()

    assert solution.pathSum(build_binary_tree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]), 8) == 3
    assert solution.pathSum(build_binary_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]), 22) == 3
    assert solution.pathSum(build_binary_tree([1, 2]), 2) == 1
    assert solution.pathSum(build_binary_tree([1, None, 2, None, 3, None, 4, None, 5]), 3) == 2
