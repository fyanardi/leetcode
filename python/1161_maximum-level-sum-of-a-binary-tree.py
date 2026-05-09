from helpers.binarytree import (
    TreeNode,
    parse_binary_tree,
)


class Solution:
    def maxLevelSum(self, root: TreeNode | None) -> int:
        if root is None:
            return 0

        from collections import deque
        nodes = deque()
        nodes.append(root)

        # -10^5 <= Node.val <= 10^5
        max_sum = -100001
        max_sum_level = 0
        level = 0

        while len(nodes) > 0:
            size = len(nodes)
            level += 1

            sum = 0

            while size > 0:
                node = nodes.popleft()
                sum += node.val


                if node.left is not None:
                    nodes.append(node.left)
                if node.right is not None:
                    nodes.append(node.right)

                size -= 1

            if sum > max_sum:
                max_sum = sum
                max_sum_level = level

        return max_sum_level


if __name__ == "__main__":
    solution = Solution()

    assert solution.maxLevelSum(parse_binary_tree([1, 7, 0, 7, -8, None, None])) == 2
    assert solution.maxLevelSum(parse_binary_tree([989, None, 10250, 98693, -89388, None, None, None, -32127])) == 2
    assert solution.maxLevelSum(parse_binary_tree([-100, -200, -300, -20, -5, -10, None])) == 3
