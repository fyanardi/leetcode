# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        max_value = root.val
        return 1 + self.__good_nodes(max_value, root.left) + self.__good_nodes(max_value, root.right)


    def __good_nodes(self, max_value, node):
        if node is None:
            return 0
        good_nodes = 0
        if max_value <= node.val:
            good_nodes = good_nodes + 1
        good_nodes = good_nodes + self.__good_nodes(max(max_value, node.val), node.left)
        good_nodes = good_nodes + self.__good_nodes(max(max_value, node.val), node.right)
        return good_nodes

